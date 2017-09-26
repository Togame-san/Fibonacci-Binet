# Binet's Formula Verification
import sys
import math

def Fib_rec(a, b, n):
    if(n == 0):
        #sys.stdout.write(str(a))
        return a
    #Determine F_n
    F_n = a + b
    #sys.stdout.write(str(a) + ", ")
    a = b
    b = F_n
    n = n - 1
    Fib_rec(a, b, n)

Fib_rec(0,1, 0)

sys.stdout.write("\nBinet's Formula\n")
def Binet(n):
    for x in range(0, n + 1):
        F_n = 1/math.sqrt(5)*(((1+math.sqrt(5))/2)**x - ((1-math.sqrt(5))/2)**x)
        if(x == n):
            #sys.stdout.write(str(F_n) + ", ")
            return int(F_n)

def testMachine(tol):
    n = 0
    while True:
        Fib_result = Fib_rec(0,1,n)
        Binet_result = Binet(n)
        if(abs(Fib_result - Binet_result) > tol or n == 1000):
            sys.stdout.write("\nThis machine retains acceptable accuracy until the " + str(n) + "th term in the Fib sequence\n")
            break

testMachine(.00000000000000001)
        
