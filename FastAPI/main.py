from fastapi import FastAPI

app = FastAPI()

@app.get("/")

async def root():
    return "Hola mundo"

@app.get("/cursos")
async def cursos():
    return {"cursos": ["Programacion", "Ingenieria", "Matematicas"]}

#iniciar servidor: uvicorn main:app --reload
#detener servidor: CTRL+C