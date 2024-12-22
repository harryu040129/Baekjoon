while True:
    length = list(map(int, input().split()))

    asqbsq = 0

    hy = max(length)

    if length[0] == length[1] == length[2] == 0:
        break

    for x in length:
        if x != hy:
            asqbsq += x**2

    if asqbsq == hy**2:
        print('right')
    else:
        print('wrong')
