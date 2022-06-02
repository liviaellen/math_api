from fastapi import FastAPI


app= FastAPI()

@app.get('/')
def index():
    return{'value': True }


@app.get('/multiply')
def multiply(a,b):
    return{'result': int(a)*int(b)}

@app.get('/sum')
def multiply(a,b):
    return{'result': int(a)+int(b)}
