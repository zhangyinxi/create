  1 
  2 class Stmcu:
  3     def saveparam(self,arg):
  4         f       = open("stmcu.txt",'w')
  5         f.write(arg)
  6         f.close()
  7     def getparam(self):
  8         f2      = open("stmcu.txt",'r')
  9         content = f2.read()
 10         f2.close()
 11         return content
