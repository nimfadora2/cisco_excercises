'''
Date: 28.01.2018
Author: Kinga Slowik
Program: Cisco Python Excercise nr 1
'''

ip="10.1.1.0"
# Input of proper ip address
while True:
    try:
        ip=[int(x) for x in input("Enter IP address: ").strip().split(".")]
    except:
        print("Invalid IP address format")
    else:
        if len(ip)!=4:
            print("Invalid IP address format")
            continue
        for i in ip:
            if  0 > i  or i > 255:
                print("Invalid IP address format")
                continue
        break

# Input od proper mask
while True:
    try:
        mask=int(input("Enter subnet mask in decimal format: ").lstrip('/'))
    except:
        print("Subnet mask is invalid")
    else:
        if 0< mask <=32 :
            break
        print("Subnet mask is invalid")

mask_bin=mask*"1"+(32-mask)*"0"
negated_mask_bin=mask*"0"+(32-mask)*"1"

# Printing ip address in binary
for i in ip:
    print("%10s" %i, end="")
print()
for i in ip:
    print("%10s" %format(i,'08b'), end="")
print()

# Printing network address
print("network address is: ", end="")
for i in range(len(ip)):
    if i!=3:
        print(ip[i]&int(mask_bin[0+i*8:8+i*8],2), end=".")
    else:
        print(str(ip[i] & int(mask_bin[0 + i * 8:8 + i * 8], 2))+"/"+str(mask))

# Printing broadcast address
print("broadcast address is: ", end="")
for i in range(len(ip)):
    if i!=3:
        print((ip[i]&int(mask_bin[0+i*8:8+i*8],2))|(ip[i]|int(negated_mask_bin[0+i*8:8+i*8],2)), end=".")
    else:
        print(str((ip[i]&int(mask_bin[0+i*8:8+i*8],2))|(ip[i]|int(negated_mask_bin[0+i*8:8+i*8],2)))+"/"+str(mask))

