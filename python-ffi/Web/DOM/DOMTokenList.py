import xml.dom.minidom


def add(l: list):
    def _1(token):
        def _2():
            return l.append(token)

        return _2

    return _1


def remove(l: list):
    def _1(token):
        def _2():
            return l.remove(token)

        return _2

    return _1


def contains(l: list):
    def _1(token):
        def _2():
            return token in l

        return _2

    return _1


def toggle(l: list):
    def _1(token):
        def _2():
            if token in l:
                l.remove(token)
                return False
            l.append(token)
            return True

        return _2

    return _1


def toggleForce(l: list):
    def _1(token):
        def _2(force):
            def _3():
                if not force and (token in l):
                    l.remove(token)
                elif force and (token not in l):
                    l.append(token)
                return force

            return _3

        return _2

    return _1


def _item(l: list):
    def _1(idx):
        def _2():
            return l[idx]

        return _2

    return _1
