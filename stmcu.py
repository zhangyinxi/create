class Stmcu:
    def saveparam(self,arg):
        f       = open("/usr/bin/stmcu.txt",'w')
        f.write(arg)
        f.close()

    def getparam(self):
        f2      = open("/usr/bin/stmcu.txt",'r')
        content = f2.read()
        f2.close()
        return content
