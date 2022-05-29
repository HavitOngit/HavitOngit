def longdivision(x):
    n = 2
    mlist = []
    while True:
        oldx = x
        x = x / n
        if x != int(x):
            x = oldx
            # print(x, 'now x is oldx', n)
            n += 1
            continue
        elif int(x) == 1.0:
            mlist.append(n)
            print('last', x, n)
            break
        mlist.append(n)
        print('%s / %s = %s' % (oldx, n, x))

    return print(mlist), mlist

longdivision(78)
