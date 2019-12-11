import imageio
import numpy as np
rgbweights=[0.3,0.59,0.11]
def greyImage(imageObj):
    if isinstance(imageObj,str):
        imageObj=imageio.imread(imageObj)
    shape=imageObj.shape
    greyimage=np.zeros((shape[0],shape[1],1))
    for i in range(shape[0]):
        for j in range(shape[1]):
            greyimage[i][j][0]=rgbweights[0]*imageObj[i][j][0]+\
                rgbweights[1]*imageObj[i][j][1]+rgbweights[2]*imageObj[i][j][2]
    return greyimage
def testgreyImage():
    path=r'/home/patrick/PatrickWorkspace/ClassicalVision/Lena.png'
    greyimage=greyImage(path)
    imageio.imwrite('/home/patrick/PatrickWorkspace/ClassicalVision/Lena_grey.png',greyimage)
if __name__=='__main__':
    testgreyImage()