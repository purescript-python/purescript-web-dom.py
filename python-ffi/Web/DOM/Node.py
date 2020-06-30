import xml.dom.minidom


def nodeTypeIndex(node: xml.dom.minidom.Element):
    return node.nodeType


def nodeName(node: xml.dom.minidom.Element):
    return node.nodeName


def baseURI(node: xml.dom.minidom.Element):
    def _1():
        raise Exception("cannot get baseURI in python")

    return _1


def ownerDocument(node: xml.dom.minidom.Element):
    def _1():
        return node.ownerDocument

    return _1


def _parentNode(node: xml.dom.minidom.Element):
    def _1():
        return node.parentNode

    return _1


def _parentElement(node: xml.dom.minidom.Element):
    def _1():
        return node.parentNode

    return _1


def hasChildNodes(node: xml.dom.minidom.Element):
    def _1():
        return node.hasChildNodes()

    return _1


def childNodes(node: xml.dom.minidom.Element):
    def _1():
        return node.childNodes

    return _1


def _firstChild(node: xml.dom.minidom.Element):
    def _1():
        return node._get_firstChild()

    return _1


def _lastChild(node: xml.dom.minidom.Element):
    def _1():
        return node._get_lastChild()

    return _1


def _previousSibling(node: xml.dom.minidom.Element):
    def _1():
        return node.previousSibling

    return _1


def _nextSibling(node: xml.dom.minidom.Element):
    def _1():
        return node.nextSibling

    return _1


def _nodeValue(node: xml.dom.minidom.Element):
    def _1():
        return node.nodeValue

    return _1


def setNodeValue(v):
    def _1(node: xml.dom.minidom.Element):
        def _2():
            node.nodeValue = v
            return {}

        return _2

    return _1


def textContent(node: xml.dom.minidom.Element):
    def _1():
        raise Exception("Cannot (yet) get text content of python nodes. Make a PR!")

    return _1


def setTextContent(a):
    def _1(b):
        def _2():
            raise Exception("Cannot (yet) set text content of python nodes. Make a PR!")

        return _2

    return _1


def noramlize(n: xml.dom.minidom.Element):
    def _1():
        return n.normalize()

    return _1


def clone(n: xml.dom.minidom.Element):
    def _1():
        return n.cloneNode(False)

    return _1


def deepClone(n: xml.dom.minidom.Element):
    def _1():
        return n.cloneNode(True)

    return _1


def isEqualNode(n0: xml.dom.minidom.Element):
    def _1(n1: xml.dom.minidom.Element):
        def _2():
            return n0.isSameNode(n1)

        return _2

    return _1


def compareDocumentPositionBits(n0: xml.dom.minidom.Element):
    def _1(n1: xml.dom.minidom.Element):
        def _2():
            raise Exception("Cannot compare document precision bits")

        return _2

    return _1


def _contains_recurser(needle, n: List[xml.dom.minidom.Element]):
    return (
        False
        if len(n) == 0
        else needle is n[0]
        or (
            _contains_recurser(needle, n[0].childNodes)
            if n[0].childNodes
            else _contains_recurser(needle, n[1:])
        )
    )


def contains(n0: xml.dom.minidom.Element):
    def _1(n1: xml.dom.minidom.Element):
        def _2():
            return _contains_recurser(n1, [n0])

        return _2

    return _1


def _lookupPrefix(prefix):
    def _1(n0: xml.dom.minidom.Element):
        def _2():
            raise Exception("Cannot lookup prefix in python")

        return _2

    return _1


def _lookupNamespaceURI(prefix):
    def _1(n0: xml.dom.minidom.Element):
        def _2():
            raise Exception("Cannot lookup namespace uri in python")

        return _2

    return _1


def isDefaultNamespace(prefix):
    def _1(n0: xml.dom.minidom.Element):
        def _2():
            raise Exception("Cannot isDefaultNamespace in python")

        return _2

    return _1


def insertBefore(node1: xml.dom.minidom.Node):
    def _1(node2: xml.dom.minidom.Node):
        def _2(parent: xml.dom.minidom.Node):
            def _3():
                return parent.insertBefore(node1, node2)

            return _3

        return _2

    return _1


def appendChild(node1: xml.dom.minidom.Node):
    def _1(parent: xml.dom.minidom.Node):
        def _2():
            return parent.appendChild(node1)

        return _2

    return _1


def replaceChild(newChild: xml.dom.minidom.Node):
    def _1(oldChild: xml.dom.minidom.Node):
        def _2(parent: xml.dom.minidom.Node):
            def _3():
                return parent.insertBefore(newChild, oldChild=oldChild)

            return _3

        return _2

    return _1


def removeChild(node1: xml.dom.minidom.Node):
    def _1(parent: xml.dom.minidom.Node):
        def _2():
            return parent.removeChild(node1)

        return _2

    return _1
