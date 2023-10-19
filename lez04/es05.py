"""
1! = 1
2! = 1*2 = 1! * 2
3! = 1*2*3 = 2! * 3
4! = 1*2*3*4 = 3! * 4
"""

def fattoriale(n):
    if n <= 1:
        return 1
    else:
        return fattoriale(n-1) * n

def fattorialeBello(n):
    return 1 if n <= 1 else fattorialeBello(n-1)*n

print(fattorialeBello(10))