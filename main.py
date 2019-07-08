from PIL import Image
from texture import loadpng
import os 

srcPath = "C:/Users/lidachuizi/Desktop/xxx/SplitImage/plist"
outPath = "C:/Users/lidachuizi/Desktop/xxx/SplitImage/out"
PngNames = []
# PngNames = ["plist_skill_effect_1004hit","plist_skill_effect_1004hit1"]
def eachFile(filepath):
    fileNames = os.listdir(filepath)  
    for file in fileNames:
        newDir = filepath + '/' + file 
        if os.path.isfile(newDir): 
            splitext = os.path.splitext(newDir)
            # print(os.path.splitext(file)[0]) 
            if splitext[1] == ".plist": 
                PngNames.append(splitext[0])

def splitImg(PngName):

    im = Image.open(PngName +'.png')
    image_list = loadpng(PngName)
    for img in image_list:
        png_name = img['png']    
        pos = img['pos']        
        if img['rotated'] == 'true':
            box = ( int(pos['x']), int(pos['y']),  int(pos['x'])+int(pos['h']) ,int(pos['y']) + int(pos['w']) )
        else:
            box = ( int(pos['x']), int(pos['y']), int(pos['x']) + int(pos['w']), int(pos['y'])+int(pos['h']))
        region  = im.crop(box)

        if img['rotated'] == 'true':
            region = region.transpose(Image.ROTATE_90)

        [dirname,filename] = os.path.split(PngName +'.plist')
        print(os.path.basename(PngName))
        filename = os.path.splitext(filename)[0]
        savepath = outPath + '/'+ filename
        if os.path.exists(savepath) == False:
            os.mkdir(savepath)
        region.save(savepath + '/' + png_name)


if __name__ == '__main__':
    eachFile(srcPath)
    for PngName in PngNames:
        splitImg(PngName)
