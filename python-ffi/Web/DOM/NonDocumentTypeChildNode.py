import xml.dom.minidom


def _previousElementSibling(node: xml.dom.minidom.Node):
    def _1():
        return node.previousSibling

    return _1


def _nextElementSibling(node: xml.dom.minidom.Node):
    def _1():
        return node.nextSibling

    return _1
