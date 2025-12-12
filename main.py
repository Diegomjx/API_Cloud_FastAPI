import os
import numpy as np
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import tensorflow as tf
from tensorflow import keras
from pydantic import BaseModel

app = FastAPI(
    title="Modelo Tabular API",
    description="API para predecir una condición (simulación) con tus datos tabulares",
    version="1.0.0"
)

# Modelo global
model = None

# ASUME que tu variable objetivo está en dependent_variables
dependent_variables = ["diabetes", "obesidad", "colesterol"]
TARGET = "diabetes"              # <- variable que quieres convertir a 0/1
target_index = dependent_variables.index(TARGET)

class InputData(BaseModel):
    features: list


def load_model():
    global model
    model_path = "Diabetes.keras"

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Modelo no encontrado en {model_path}")

    model = keras.models.load_model(model_path)
    print("✓ Modelo cargado exitosamente")


@app.on_event("startup")
async def startup_event():
    try:
        load_model()
    except Exception as e:
        print(f"Error al cargar modelo: {e}")


@app.post("/predict")
async def predict(data: InputData):

    if model is None:
        raise HTTPException(status_code=500, detail="Modelo no cargado")

    # Convertir a numpy array con forma (1, N)
    try:
        X = np.array(data.features, dtype=np.float32).reshape(1, -1)
    except:
        raise HTTPException(status_code=400, detail="Formato de features inválido")

    # Hacer predicción
    pred = model.predict(X)
    prob = float(pred[0][target_index])

    # Convertir probabilidad -> 1 o 0
    output = 1 if prob >= 0.5 else 0

    return {
        "target": TARGET,
        "probability": prob,
        "prediction": output
    }


@app.get("/")
async def root():
    return {
        "message": "Modelo Tabular API",
        "status": "active",
        "input_format": {"features": "[list of N numeric values]"},
        "output": "1 or 0"
    }
    
@app.get("/Health")
async def root():
    return {
        "message": "Modelo Tabular API",
        "status": "active",
        "input_format": {"features": "[list of N numeric values]"},
        "output": "1 or 0"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

