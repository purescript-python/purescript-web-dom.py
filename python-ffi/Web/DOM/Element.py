import xml.dom.minidom


def _namespaceURI(e: xml.dom.minidom.Element):
    def _1():
        return e.namespaceURI

    return _1


def _prefix(e: xml.dom.minidom.Element):
    def _1():
        return e.prefix

    return _1


def localName(e: xml.dom.minidom.Element):
    def _1():
        return e._get_localName()

    return _1


def tagName(e: xml.dom.minidom.Element):
    def _1():
        return e.tagName

    return _1


def id(e: xml.dom.minidom.Element):
    def _1():
        return e.getAttribute("id")

    return _1


def setId(_id):
    def _1(e: xml.dom.minidom.Element):
        def _2():

            return e.setAttribute("id", _id)

        return _2

    return _1


def className(e: xml.dom.minidom.Element):
    def _1():
        return e.getAttribute("class")

    return _1


def classList(e: xml.dom.minidom.Element):
    def _1():
        return e.getAttribute("class").split(" ")

    return _1


def setClassName(_kls):
    def _1(e: xml.dom.minidom.Element):
        def _2():

            return e.setAttribute("class", _kls)

        return _2

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


def setAttribute(name):
    def _1(value):
        def _2(e: xml.dom.minidom.Element):
            def _3():
                e.setAttribute(name, value)
                return {}

            return _3

        return _2

    return _1


def _getAttribute(name):
    def _1(e: xml.dom.minidom.Element):
        def _2():
            return e.getAttribute(name)

        return _2

    return _1


def hasAttribute(name):
    def _1(e: xml.dom.minidom.Element):
        def _2():
            return e.hasAttribute(name)

        return _2

    return _1


def removeAttribute(name):
    def _1(e: xml.dom.minidom.Element):
        def _2():
            return e.removeAttribute(name)

        return _2

    return _1


def scrollTop(*args):
    def _1(*args1):
        raise Exception("Cannot call this function in purescript.")

    return _1


def setScrollTop(*args):
    def _1(*args1):
        def _2(*args2):
            raise Exception("Cannot call this function in purescript.")

        return _2

    return _1


def scrollLeft(*args):
    def _1(*args1):
        raise Exception("Cannot call this function in purescript.")

    return _1


def setScrollLeft(*args):
    def _1(*args1):
        def _2(*args2):
            raise Exception("Cannot call this function in purescript.")

        return _2

    return _1


def scrollWidth(*args):
    def _1(*args1):
        raise Exception("Cannot call this function in purescript.")

    return _1


def scrollHeight(*args):
    def _1(*args1):
        raise Exception("Cannot call this function in purescript.")

    return _1


def clientTop(*args):
    def _1(*args1):
        raise Exception("Cannot call this function in purescript.")

    return _1


def clientLeft(*args):
    def _1(*args1):
        raise Exception("Cannot call this function in purescript.")

    return _1


def clientWidth(*args):
    def _1(*args1):
        raise Exception("Cannot call this function in purescript.")

    return _1


def clientHeight(*args):
    def _1(*args1):
        raise Exception("Cannot call this function in purescript.")

    return _1

