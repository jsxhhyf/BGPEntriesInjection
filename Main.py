import random, ipaddress, urllib

# IPv6 addressing and CABA addressing

# print random.randint(10, 16777216)

for i in range(0, 3):
    RES = '00000000'
    ASN = '00000000' + str(bin(random.randint(0, 16777216)))[2:]
    SNID = str(bin(random.randint(0, 16777216)))[2:]
    IID = str(bin(random.randint(0, 16777216)))[2:] + str(bin(random.randint(0, 16777216)))[2:] + str(bin(random.randint(0, 16777216)))[2:]
    EID = RES + ASN + SNID + IID
# b = int('00000101111111111111111100000', 2)
    print(ipaddress.IPv6Address(int(EID, 2)))