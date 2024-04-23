from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from convertToAscii import convertToAscii


# origins = [
#     "http://localhost:3000",
#     "http://localhost",
#     "http://localhost:8080",
# ]
def initCORS():
    origins=['*']
    app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)
    

app = FastAPI()
initCORS()





@app.get('/')
def root():
    return {'hello':'world'}



class covertInData(BaseModel):
    base64_data:str

class convertOutData(BaseModel):
    status:int


@app.post('/convert')
async def convert(data:covertInData):

    ascii = await convertToAscii(data.base64_data)
    print(ascii)
    result = {
            'status':1,
            'ascii':ascii,
            
              }

    return result



