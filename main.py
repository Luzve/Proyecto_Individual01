# save this as app.py
from fastapi import FastAPI

app = FastAPI(title='Proyecto Individual 01')


#@app.get('/')
#async def read_root():
#    return {'Primera API 00'}

@app.get("/")
async def index():
    return 'Hola mundo'

@app.get('/about')
async def about():
    return 'Estamos en el about'


