import xml.dom.minidom


def children(node: xml.dom.minidom.Node):
    def _1():
        return node.childNodes

    return _1


def _firstElementChild(node: xml.dom.minidom.Node):
    def _1():
        return node._get_firstChild()

    return _1


def _lastElementChild(node: xml.dom.minidom.Node):
    def _1():
        return node._get_lastChild()

    return _1


def childElementCount(node: xml.dom.minidom.Node):
    def _1():
        return len(node.childNodes.count)

    return _1


def _querySelector(selector):
    def _1(node):
        def _2():
            raise Exception("no querySelector method in pythong")

        return _2

    return _1


def querySelectorAll(selector):
    def _1(node):
        def _2():
            raise Exception("no querySelector method in pythong")

        return _2

    return _1

