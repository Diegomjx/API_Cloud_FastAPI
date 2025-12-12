# Horse vs Human Classifier API

#Virtualizaciòn
```arduino
python3 -m venv venv
source venv/bin/activate
```


API simple de FastAPI para clasificar imágenes entre caballos y humanos usando una CNN entrenada con TensorFlow.

## Instalación

1. Instalar dependencias:
```bash
pip install -r requirements.txt
```

2. Colocar el archivo del modelo `horse_human_classifier.h5` en el mismo directorio que `main.py`

3. Ejecutar la API:
```bash
python main.py
```

O usando uvicorn directamente:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## Uso

### Endpoints disponibles:

- **GET /** - Información general de la API
- **GET /health** - Health check
- **POST /predict** - Clasificar imagen

### Ejemplo de uso con curl:

```bash
# Health check
curl http://localhost:8000/health

# Predecir imagen
curl -X POST "http://localhost:8000/predict"  -H "Content-Type: application/json" -d '{ "features": [5.1, 130, 75, 0, 1, 0, 0, 1]}'
```

### Ejemplo de respuesta:

```json
{
    "target": "diabetes",
    "probability": 0.9552638530731201,
    "prediction": 1
}
```

## Clases:
- **0**: Sin Diabetes
- **1**: Con Diabetes

## Documentación interactiva:
Una vez ejecutada la API, visita:
- http://localhost:8000/docs (Swagger UI)
- http://localhost:8000/redoc (ReDoc)

## Estructura del proyecto:
```
horse_human_api/
├── main.py                    # API de FastAPI
├── requirements.txt           # Dependencias
├── horse_human_classifier.h5  # Modelo entrenado (debes colocarlo aquí)
└── README.md                  # Esta documentación

```

