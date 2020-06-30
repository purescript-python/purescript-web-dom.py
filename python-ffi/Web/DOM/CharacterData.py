import xml.dom
import xml.dom.minidom


def data_(t: xml.dom.minidom.CharacterData):
    def _1():
        return t.data

    return _1


def length(t: xml.dom.minidom.CharacterData):
    def _1():
        return len(t.data)

    return _1


def substringData(offset):
    def _1(count):
        def _2(cd: xml.dom.minidom.CharacterData):
            def _3():
                return cd.substringData(offset, count)

            return _3

        return _2

    return _1


def appendData(data):
    def _1(cd: xml.dom.minidom.CharacterData):
        def _2():
            return cd.appendData(data)

        return _2

    return _1


def insertData(offset):
    def _1(data):
        def _2(cd: xml.dom.minidom.CharacterData):
            def _3():
                return cd.insertData(offset, data)

            return _3

        return _2

    return _1


def deleteData(offset):
    def _1(count):
        def _2(cd: xml.dom.minidom.CharacterData):
            def _3():
                cd.deleteData(offset, count)

            return _3

        return _2

    return _1


def replaceData(offset):
    def _1(count):
        def _2(data):
            def _3(cd: xml.dom.minidom.CharacterData):
                def _4():
                    cd.replaceData(offset, count, data)

                return _4

            return _3

        return _2

    return _1

