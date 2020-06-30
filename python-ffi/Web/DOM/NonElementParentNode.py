import xml.dom.minidom
from typing import List


def _returnNodeIfId(myId: str, n: xml.dom.minidom.Element):
    try:
        _id = n.getAttribute("id")
        return n if _id == myId else None
    except:
        return None


def _id_recurser(myId: str, n: List[xml.dom.minidom.Element]):
    return (
        None
        if len(n) == 0
        else _returnNodeIfId(myId, n[0])
        or (_id_recurser(myId, n[0].childNodes) if n[0].childNodes else None)
        or _id_recurser(myId, n[1:])
    )


def _getElementById(_id):
    def _1(node):
        def _2():
            return _id_recurser(_id, [node])

        return _2

    return _1

