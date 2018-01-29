'''
Date: 29.01.2018
Author: Kinga Slowik
Program: Cisco Python Excercise nr 2

Source:
https://stackoverflow.com/questions/27715213/test-if-value-exists-in-several-lists

'''
import re

f=open("commands.txt","r")

text=f.readlines()
mode = "switchport trunk allowed vlan"

List_1=[]
List_2=[]

all_vlans=[]
for data in text:
    if re.match(mode,data) != None:
        all_vlans.append([int(x) for x in re.search(r'(\d+\,?\s*)+',data).group(0).strip().split(",")])

# Checking for common vlans
for i in all_vlans[0]:
    #print(all_vlans[i])
    same = all(i in x for x in [m for m in all_vlans])
    if same==True:
        List_1.append(i)
List_1.sort()
print("List_1=",[str(x) for x in List_1])

# Checking unique vlans
table=[]
# One, big list to count
for data in all_vlans:
    table.extend(data)
# Adding to List_2 only unique
for i in table:
    if table.count(i)==1:
        List_2.append(i)
List_2.sort()
print("List_2=",[str(x) for x in List_2])
