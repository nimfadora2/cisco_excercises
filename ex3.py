'''
Date: 29.01.2018
Author: Kinga Slowik
Program: Cisco Python Excercise nr 3

Source:
'''

import re

f = open("ShowIproute.txt","r")

text = f.readlines()

for i in range(12,len(text)):
    current = text[i].strip().strip("\n").split()
    if len(current)==0:
        continue
    if current[0]=='D':
        print("%-20s" %"Protocol:"+"EIGRP")
    elif current[0]=='R':
        print("%-20s" % "Protocol:" + "RIP")
    elif current[0][0] == 'O':
        print("%-20s" % "Protocol:" + "OSPF")
    print("%-20s" % "Prefix:" + current[1].strip().strip(","))
    print("%-20s" % "AD/Metric:" + current[2][1:(len(current[2])-1)])
    print("%-20s" % "Next-hop:" + current[4].strip(","))
    print("%-20s" % "Last update:" + current[5].strip(","))
    print("%-20s" % "Outbound interface:" + current[6].strip(","))
    print()


