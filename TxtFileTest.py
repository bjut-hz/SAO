__author__ = 'hz'
#
# f = open( r'11.txt', 'r' )
# line = f.readline()
# line = line.strip()
# s = []
# s.append( line )
# while line:
#     line = f.readline()
#     line = line.strip()
#     s.append( line )
#
# print( s )
class A:
    def __init__(self):
        self.s = self.test()

    def test(self):
        return 'dd'

if __name__ == '__main__':
    a = A()
    print(a.s)