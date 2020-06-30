import xml.dom.minidom


def url(doc: xml.dom.minidom.Document):
    def _1():
        raise Exception("cannot get document url")

    return _1


def documentURI(doc: xml.dom.minidom.Document):
    def _1():
        return doc.documentURI

    return _1


def origin(doc: xml.dom.minidom.Document):
    def _1():
        raise Exception("cannot get document origin")

    return _1


def compatMode(doc: xml.dom.minidom.Document):
    def _1():
        raise Exception("cannot get document compatMode")

    return _1


def characterSet(doc: xml.dom.minidom.Document):
    def _1():
        raise Exception("cannot get document characterSet")

    return _1


def contentType(doc: xml.dom.minidom.Document):
    def _1():
        raise Exception("cannot get document contentType")

    return _1


def _doctype(doc: xml.dom.minidom.Document):
    def _1():
        return doc.doctype

    return _1


def _documentElement(doc: xml.dom.minidom.Document):
    def _1():
        return doc.documentElement

    return _1


def getElementsByTagName(localName: str):
    def _1(doc: xml.dom.minidom.Document):
        def _2():
            return doc.getElementsByTagName(localName)

        return _2

    return _1


def _getElementsByTagNameNS(ns: str):
    def _1(localName: str):
        def _2(doc: xml.dom.minidom.Document):
            def _3():
                return doc.getElementsByTagNameNS(ns, localName)

            return _3

        return _2

    return _1


def _returnIfHasClassNames(classNames: str, n: xml.dom.minidom.Element):
    try:
        classes = n.getAttribute("class").split(" ")
        return [n] if False not in [x in classes for x in classNames.split(" ")] else []
    except:
        return []


def _classRecurser(classNames: str, n: xml.dom.minidom.Element):
    _returnIfHasClassNames(classNames, n) + sum(
        [_classRecurser(x) for x in n.childNodes], []
    )


def getElementsByClassName(classNames):
    def _1(doc: xml.dom.minidom.Document):
        def _2():
            return _classRecurser(classNames, doc.documentElement)

        return _2

    return _1


def createElement(localName: str):
    def _1(doc: xml.dom.minidom.Document):
        def _2():
            return doc.createElement(localName)

        return _2

    return _1


def _createElementNS(ns: str):
    def _1(localName: str):
        def _2(doc: xml.dom.minidom.Document):
            def _3():
                return doc.createElementNS(ns, localName)

            return _3

        return _2

    return _1


def createDocumentFragment(doc: xml.dom.minidom.Document):
    def _1():
        return doc.createDocumentFragment()

    return _1


def createTextNode(data: str):
    def _1(doc: xml.dom.minidom.Document):
        def _2():
            return doc.createTextNode(data)

        return _2

    return _1


def createComment(data: str):
    def _1(doc: xml.dom.minidom.Document):
        def _2():
            return doc.createComment(data)

        return _2

    return _1


def createProcessingInstruction(target):
    def _1(data: str):
        def _2(doc: xml.dom.minidom.Document):
            def _3():
                return doc.createProcessingInstruction(target, data)

            return _3

        return _2

    return _1


def importNode(node):
    def _1(deep):
        def _2(doc: xml.dom.minidom.Document):
            def _3():
                return doc.importNode(node, deep)

            return _3

        return _2

    return _1


def adoptNode(node):
    def _1(doc: xml.dom.minidom.Document):
        def _2():
            return node  # do nothing, just return

        return _2

    return _1

