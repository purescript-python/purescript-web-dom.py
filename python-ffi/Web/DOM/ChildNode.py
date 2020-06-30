import xml.dom.minidom


def remove(node: xml.dom.minidom.Node):
    def _1():
        return node.parentNode.removeChild(node)

    return _1

