from convert import convertToImage
from asciiRender import AsciiRender


async def convertToAscii(data):
    img = convertToImage(data)
    ar = AsciiRender(img) 
    result = await ar.render()
    



    return result

