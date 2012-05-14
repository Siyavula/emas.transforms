def getLogger(string):
    class X:
        def info(self, string):
            print string
    return X()
