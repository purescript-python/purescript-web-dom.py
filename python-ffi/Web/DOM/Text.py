import xml.dom.minidom


def splitText(offset):
    def _1(t: xml.dom.minidom.Text):
        def _2():
            s = xml.dom.minidom.parseString("<doc><foo/></doc>")

            pn = t.parentNode
            n0 = s.createTextNode(t.data[:offset])
            n1 = s.createTextNode(t.data[offset:])
            pn.insertBefore(n1, t)
            pn.insertBefore(n0, n1)
            pn.removeChild(t)
            return t

        return _2

    return _1


def wholeText(t: xml.dom.minidom.Text):
    def _1():
        return t._get_wholeText()

    return _1

