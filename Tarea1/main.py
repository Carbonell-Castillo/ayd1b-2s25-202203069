from fastapi import FastAPI

app = FastAPI(title="Mi API de Canción Favorita")

name = "Bruce Carbonell Castillo Cifuentes"
song = "Cornfield Chase"

@app.get("/info")
def info():
    return {
        "nombre": name,
        "cancion_favorita": song
    }

