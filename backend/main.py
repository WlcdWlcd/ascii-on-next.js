from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

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
    sliceSize:int
    invert: bool

class convertOutData(BaseModel):
    status:int


@app.post('/convert')
async def convert(data:covertInData):

    ascii = await convertToAscii(data.base64_data,slice_size = data.sliceSize,invert=data.invert)
    result = {
            'status':1,
            'ascii':ascii,
            
              }

    return result

if __name__ == "__main__":
  uvicorn.run("server.api:app", host="0.0.0.0", port=8000, reload=True)

