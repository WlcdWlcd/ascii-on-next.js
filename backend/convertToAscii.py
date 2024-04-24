from convert import convertToImage
from asciiRender import AsciiRender


async def convertToAscii(data,slice_size=8,invert=False):
    img = convertToImage(data)
    ar = AsciiRender(img) 
    ar.setSlice(slice_size)
    ar.setInvert(invert)

    result = await ar.render()
    



    return result

