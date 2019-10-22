from xml.dom import minidom

# Open XML document using minidom parser
DOMTree = minidom.parse("bookstore.xml")

# print(DOMTree.toxml())

# get a list of elements whose tag name is "book"
books = DOMTree. getElementsByTagName("book")


# books is a list, so we can access to a specific element
# The following code helps to test the code
print(books[0].toxml())

for book in books:
        category = book.getAttribute("category")
        title = book.getElementsByTagName("title")[0]
        author = book.getElementsByTagName("author")[0]
        year = book.getElementsByTagName("year")[0]
        price = book.getElementsByTagName("price")[0]
        print("category:%s, title:%s, author:%s, year:%s , price:%s" % (category, title.firstChild.nodeValue, author.firstChild.nodeValue, year.firstChild.nodeValue, price.firstChild.nodeValue))
