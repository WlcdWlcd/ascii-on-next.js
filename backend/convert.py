import cv2
import numpy as np
import base64


def convertToImage (data):
    data = data.split(',')[1]
    decoded_data = base64.b64decode(data)
    np_data = np.fromstring(decoded_data,np.uint8)
    img = cv2.imdecode(np_data,cv2.IMREAD_UNCHANGED)

    return img



if __name__ == "__main__":
    
    convertToImage()