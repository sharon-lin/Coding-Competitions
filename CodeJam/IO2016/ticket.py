#!/usr/bin/env python
def most_common(lst):
    return max(set(lst), key=lst.count)

for case in range(int(raw_input())):
    map1 = [map(int, raw_input().split())]
    total = []
    for value in range(map1[0][0]):
        map2 = [map(int, raw_input().split())]
        if map2[0] not in total and [map2[0][1], map2[0][0]] not in total:
            total.append(map2[0])
    nums = []
    for i in total:
        if i[0] == i[1]:
            nums.append(i[0])
        else:
            nums.append(i[0])
            nums.append(i[1])
    common =  most_common(nums)
    ans = 0
    for i in total:
        if common in i:
           ans += 1
    print "Case #%d: %s" % (case+1,ans)

            
