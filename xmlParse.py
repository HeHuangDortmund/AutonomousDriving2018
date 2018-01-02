import  xml.dom.minidom

def getTagText(root, tag):  
    node = root.getElementsByTagName(tag)[0]  
    rc = ""  
    for node in node.childNodes:  
        if node.nodeType in (node.TEXT_NODE, node.CDATA_SECTION_NODE):  
            rc = rc + node.data  
        return rc  

def getOutput(xmlfile):  
    dom = xml.dom.minidom.parse(xmlfile)
    root = dom.documentElement
    Obj = root.getElementsByTagName( "object" )[0]
    name = getTagText(Obj, "name")

    # One-Hot dealing
    if name == 'ten':  
        intersection = 0
    if name == 'T':  
        intersection = 1

    size = root.getElementsByTagName('size')[0]
    width = int(getTagText(size,'width'))
    height = int(getTagText(size, 'height'))

    box = Obj.getElementsByTagName('bndbox')[0]
    xmin = int(getTagText(box, 'xmin'))
    ymin = int(getTagText(box, 'ymin'))
    xmax = int(getTagText(box, 'xmax'))
    ymax = int(getTagText(box, 'ymax'))
    y = [xmin/width, ymin/height, xmax/width, ymax/height, intersection]
    return y
'''
if __name__ == '__main__':  
    getOutput()
'''