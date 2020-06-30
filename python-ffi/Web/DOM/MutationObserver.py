def mutationObserver(cb):
    def _1():
        raise Exception("Cannot call mutationObserver in MutationObserver")

    return _1


def _observe(node):
    def _1(config):
        def _2(mo):
            def _3():
                raise Exception("Cannot call _observe in MutationObserver")

            return _3

        return _2

    return _1


def disconnect(cb):
    def _1():
        raise Exception("Cannot call disconnect in MutationObserver")

    return _1


def takeRecords(cb):
    def _1():
        raise Exception("Cannot call takeRecords in MutationObserver")

    return _1
