from xml.dom import minidom, Node
import sys

def scanNode(node, file=sys.stdout, level = 0):
    if node.hasChildNodes():
        for child in node.childNodes:
                scanNode(child, file, level + 1)
    else:
        if node.nodeValue.strip() != "":
            file.write(node.nodeValue + ',') 

    if node.nodeType == Node.ELEMENT_NODE:
        if node.hasAttributes():
            file.write(node.attributes.item(0).nodeValue + ',')
        if level == 2:
            file.write("\n")


        
DOMTree = minidom.parse('bookstore.xml')

file = open('bookstore.csv', 'w')

file.write("title,lang,author,year,price,category\n")
scanNode(DOMTree, file)

file.close()
