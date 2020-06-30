import xml.dom.minidom


def target(pi: xml.dom.minidom.ProcessingInstruction):
    def _1():
        return pi.target
    return _1

