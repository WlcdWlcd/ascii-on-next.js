import numpy as np
from cv2 import cvtColor,COLOR_BGR2GRAY,imshow,waitKey

from functools import reduce

from os import chdir, getcwd

class AsciiRender():
    def __init__(self,img):
        # self.img = cvtColor(img,COLOR_RGB2GRAY)
        self.img = cvtColor(img,COLOR_BGR2GRAY)
        self.width,self.height = self.img.shape
        self.slice = 8
        self.keyboard = '    .:-=+*#%@'[::1]
        self.coef = (len(self.keyboard)-1)/255
        
        
    def setSlice(self,size):
        self.slice=size

    def setInvert(self,inverted):
        if not inverted:
            self.keyboard = self.keyboard[::-1]


    def chooseSymbol(self,scale):
        return self.keyboard[int(scale*self.coef)]
        
    def sliceAvg(self,slice):
        count = slice.size
        sum = np.sum(slice)
        return sum/count


    async def render(self):
        result = ''
        for row in range(0,self.width,self.slice):
            for column in range(0,self.height,int(self.slice/2.6)):


                slice = self.img[row:row+self.slice, column:column+self.slice]
                avgOfSlice = self.sliceAvg(slice) 
                sym = self.chooseSymbol(avgOfSlice)
                result+=sym
            result+='\n'
        return result

    def showAsciiImg(self,array):        
        pass

    
if __name__ == '__main__':
    render = AsciiRender()
