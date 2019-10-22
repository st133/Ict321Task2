
from xml.dom import minidom, Node

DOMTree = minidom.parse('bookstore.xml')

# function to get the Author name as an array
def get_author_name(authorName):
    # print("authorName: %s" %  authorName)
    # take the dot out of the authorName
    a = authorName.replace(".", "")
    authorArray = a.split()
    return authorArray

for child in DOMTree.childNodes:
    # Print the First level node name
    if child.nodeType == 1: # 1 is the name node
        print(child.nodeName, ", ", child.childNodes[0].nodeValue)
        # See how many children in the first level
        print(child.childNodes.length)
        # Print the Second level
        for child2 in child.childNodes:
            if child2.nodeType == 1:  # 1 is the name node
                # See how many children in the first level
                # print(child2.childNodes.length)
                print(" ", child2.nodeName, ", ", child2.childNodes[0].nodeValue)
                # Print the third level
                for child3 in child2.childNodes:
                    if child3.nodeType == 1:  # 1 is the name node
                        # print(child3.childNodes.length)
                        print("   ", child3.nodeName, ", ", child3.childNodes[0].nodeValue)
                        if child3.nodeName == "author":
                            # Split the Author's name into firstname, middlename and lastname
                            # create an array of the fist, middle and last names
                            aArray = get_author_name(child3.childNodes[0].nodeValue)
                            # print(aArray)
                            # Create the new elements
                            firstname = minidom.parseString("<firstname>%s</firstname>" % aArray[0]).documentElement
                            middlename = minidom.parseString("<middlename>%s</middlename>" % aArray[1]).documentElement
                            lastname = minidom.parseString("<lastname>%s</lastname>" % aArray[2]).documentElement
                            # print(firstname)
                            # print(middlename)
                            # print(lastname)
                            # We could append the new elements into the parent node
                            child3.parentNode.appendChild(firstname)
                            child3.parentNode.appendChild(middlename)
                            child3.parentNode.appendChild(lastname)
                            # for child4 in child3.childNodes:
                            #     print(child4.childNodes.length)
                            #     # Print the node name and value
                            #     print("     ", child4.nodeName, ", ", child4.childNodes[0].nodeValue)


for node in DOMTree.firstChild.childNodes:
    # Process only element nodes (type 1)
    if node.nodeType == 1:
        print("Found one element with the name: " + node.nodeName)
        for n in node.childNodes:
            if n.nodeType == 1:
                print("Node name: " + n.nodeName + ', Value: ' + n.childNodes[0].nodeValue)
                # print("and its value is: " + n.childNodes[0].nodeValue)
