#!/usr/bin/env python                                                                                                                   
for case in range(int(raw_input())):
    b = int(raw_input())
    distance = []
    for i in range(b-2):
        num = 1
        if num < i:
            for j in range(num):
                num++
                distance += raw_input
