import xml.dom.minidom


def length(nl: xml.dom.minidom.NodeList):
    def _1():
        return nl.length

    return _1


def toArray(nl: xml.dom.minidom.NodeList):
    def _1():
        return nl

    return _1


def _item(index):
    def _1(nl: xml.dom.minidom.NodeList):
        def _2():
            return nl.item(index)

        return _2

    return _1

