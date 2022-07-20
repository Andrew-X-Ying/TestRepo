def Factor(n):
    i = 1
    while n > 1:
        i = i * n
        n = n - 1
    return i

def test():
    print(f"Factor(5)={Factor(5)}")

if __name__=="__main__":
    test()