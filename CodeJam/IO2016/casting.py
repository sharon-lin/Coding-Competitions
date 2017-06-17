#!/usr/bin/env python 

for case in range(int(raw_input())):
    n = int(raw_input())
    map1 = [map(float, raw_input().split())][0]
    map_sorted = sorted(map1, reverse=True)
    actors = map_sorted[0:n]
    under = map_sorted[n:]
    total = []
    for i in range(len(actors)):
        if actors[i] == 1.0000:
            total.append(1-under[n-1-i])
        else:
            total.append(1-(actors[i]*under[n-1-i]))
    ans = 1.00
    for i in total:
        ans = ans * i
    ans = format(ans, '.8f')
    print "Case #%d: %s" % (case+1,ans)
