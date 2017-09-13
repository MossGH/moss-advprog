def pal(num):
    if str(num) == str(num)[::-1]: return True
    else: return False

def main():
    prod =0
    for i in range(100,1000):
        for j in range(i,1000):
            if pal(i*j) and i*j>prod:
                prod=i*j
    print prod,"is the largest palindromic product."
main()
