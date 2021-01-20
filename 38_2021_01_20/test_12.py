for n in range(101, 201):
    s = "1" * n
    while s.count("111"):
        s = s.replace("111", "22", 1).replace("222", "11", 1)
    print(n, s)