# -*- coding=utf-8 -*-
import source.City as city
import csv

citylist = []
filename = './source/citydata.csv'
with open(filename) as f:
    reader = csv.reader(f)
    i = 0
    rowlist = []
    while i < 17:
        row = next(reader)
        rowlist.append(row)
        i = i + 1
    j = 0
    while j < 17:
        ci = rowlist[j][0]
        cx = rowlist[j][1]
        cy = rowlist[j][2]
        cn = rowlist[j][3]
        cc = rowlist[j][4]
        cbl = rowlist[j][5]
        cq = rowlist[j][6]
        cic = rowlist[j][7]
        acity = city.City(ci,cx,cy,cn,cc,cbl,cq,cic)
        citylist.append(acity)
        j = j + 1
