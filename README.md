# Diabetes o no diabetes
API simple construida con **FastAPI** para predecir si un paciente tiene o no diabetes, basada en un conjunto de características numéricas (*simulación*).  
El modelo consumido es un archivo **Keras (.keras)** entrenado previamente.

---

## 🚀 Virtualización (opcional)

### Linux / Mac
```bash
python3 -m venv venv
source venv/bin/activate
```
### Windows
```bash
python -m venv venv
venv\Scripts\activate
```
### Instalaciòn
1. Instalar dependencias: 
```bash
pip install -r requirements.txt

```
2. Asegúrate de colocar el archivo del modelo:
```bash
Diabetes.keras
```
en el mismo directorio donde está main.py.
3. Ejecutar la API:
```bash
python main.py

```
O usando uvicorn directamente:
```bash
uvicorn main:app --host 0.0.0.0 --port=8000 --reload

```
## 📡 Endpoints Disponibles
| Método | Ruta       | Descripción                               |
| ------ | ---------- | ----------------------------------------- |
| GET    | `/`        | Información general de la API             |
| GET    | `/health`  | Health Check de la API                    |
| POST   | `/predict` | Realiza una predicción basada en features |

## 🧠 Formato de Entrada (JSON)
```bash
{
  "features": [NUMERO, NUMERO, NUMERO, ...]
}

```
## 🧪 Ejemplos de Uso
### ✔ Health Check
```bash
curl http://localhost:8000/health

```
### ✔ Predicción (Linux / Mac)
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{ "features": [5.1, 130, 75, 0, 1, 0, 0, 1] }'

```
### ✔ Predicción (Windows PowerShell)
```bash
curl -X POST "http://localhost:8000/predict" `
  -H "Content-Type: application/json" `
  -d "{ \"features\": [5.1, 130, 75, 0, 1, 0, 0, 1] }"

```
### 📥 Ejemplo de Respuesta
```bash
{
    "target": "diabetes",
    "probability": 0.9552638530731201,
    "prediction": 1
}

```
### 🧾 Interpretación
 - target: variable objetivo predicha.
 - probability: probabilidad entre 0.0 y 1.0.
 - prediction:
     - 0 = sin diabetes
     - 1 = con diabetes
       
### Estructura del Proyecto
```bash
diabetes_api/
├── main.py              # API de FastAPI
├── requirements.txt     # Dependencias
├── Diabetes.keras       # Modelo entrenado
└── README.md            # Esta documentación

```
