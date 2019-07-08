try: 
    import xml.etree.cElementTree as ET 
except ImportError: 
    import xml.etree.ElementTree as ET 
import re
import sys

png_list = []
def loadpng(PngName):
    tree = ET.parse(PngName+ '.plist')
    root = tree.getroot()

    for kk in root.findall('dict'):
        for i in range(len(kk)):
            if kk[i].text == "frames":
                pngv = kk[i+1]

                for j in  range(len(pngv)):
                    png_dict = {}
                    if pngv[j].tag == 'key':
                        png_dict['png'] = pngv[j].text
                        png_list.append(png_dict)

                        frame = pngv[j+1]
                        for k in range(len(frame)):
                            if frame[k].text == 'frame':
                                png_dict['pos'] = frame[k+1].text
                            if frame[k].text == 'rotated':
                                png_dict['rotated'] = frame[k+1].tag
    return splitpng()

def splitpng():
    m = re.compile(u'[^{}]+')
    image_list = []

    for d in png_list:
        tmp = {}
        tmp['png'] = d['png']
        tmp['rotated'] = d['rotated']
        pos = d['pos'].split(',')
        pos_dict = {}
        for i in range(len(pos)):
            cn = m.findall(pos[i] )
            if i == 0:
                pos_dict['x'] = cn[0]
            elif i == 1:
                pos_dict['y'] = cn[0]
            elif i == 2:
                pos_dict['w'] = cn[0]
            elif i == 3:
                pos_dict['h'] = cn[0]
        tmp['pos'] = pos_dict
        image_list.append(tmp)

    return image_list