def main():
    L = [2,7,12,5,10,15,23]
    for i in L:
        if i % 2 == 0:
            L.remove(i)
    print(L)
main()
