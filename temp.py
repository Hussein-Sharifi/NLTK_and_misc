import fibo

M = [
      [-1, 5, 9, 13, 20, 0, 13],
      [5, 12, -3, 11, 5, 13, 1],
      [1, 2, 3, 4, 5, 6, 70, 8]
                                ]
"""Mt = [[row[i] for row in M] for i in range(7)]

t = (Mt, M, 'yo')
a = t[0]
(a,b) = t[0:2]

d = {(3,5): [1,2,3], (4,6): "yess", (5,7): "yesss", (1,1): fibo.fib2(20)}

e = {x: x**2 for x in range(10)}"""

def test():
    test.M = 55
    print(test.M)

test()
print(M)
    
class ThePlace:
    i = 'Hussein'
    u = 'Alejandra'

    @staticmethod
    def Us():
        print(ThePlace.i, "+", ThePlace.u)
ThePlace.Us()
x = ThePlace()
x.Us()