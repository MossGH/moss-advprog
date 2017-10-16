import sys

def fib(n):
    if n==1: c=0
    else: a,b,c=0,1,1
    for i in range(n-2):
        c=a+b
        a,b=b,c
    print c

if __name__ == "__main__":
    fib(int(sys.argv[1]))
