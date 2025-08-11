from fastapi import FastAPI

app = FastAPI(title="Mi API de Canción Favorita")

name = "Bruce Carbonell Castillo Cifuentes"
album = "Interstellar"

@app.get("/info")
def info():
    return {
        "nombre": name,
        "album": album
    }

