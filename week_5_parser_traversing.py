from xml.dom import minidom

# Open XML document using minidom parser
DOMTree = minidom.parse("bookstore.xml")

# print(DOMTree.toxml())


print("Node type is: ", DOMTree.nodeType) # Number 9 means DOCUMENT_NODE

print("The list of nodes for the root:")
print(DOMTree.firstChild.childNodes)

print("")
for node in DOMTree.firstChild.childNodes:
	# Process only element nodes (type 1)
	if node.nodeType == 1:
		print("Find one element with the name: " + node.nodeName)
		for n in node.childNodes:
			if n.nodeType == 1:
				print("Find one element with the name: " + n.nodeName)
				print("   and its value is: " + n.childNodes[0].nodeValue)


                
