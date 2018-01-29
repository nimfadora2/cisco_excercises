access_template = ['switchport mode access',
'switchport access vlan {}',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
'switchport mode trunk',
'switchport trunk allowed vlan {}']

# Choosing the mode - only access or trunk acceptable
while True:
    mode = input("Enter interface mode (access/trunk): ")
    if mode != "access" and mode != "trunk":
        continue
    break

# Input of interface
inter = input("Enter interface type and number: ")


# Input of vlan
if mode=="access":
    number = input("Enter VLAN number: ")
else:
    number = input("Enter allowed VLANs: ")

# Printing appropriate message
print("Interface "+inter)

# access mode
if mode == "access":
    for text in access_template:
        if text != access_template[1]:
            print(text)
        else:
            print(text.format(number))
else:                   # trunk mode
    for text in trunk_template:
        if text != trunk_template[2]:
            print(text)
        else:
            print(text.format(number))