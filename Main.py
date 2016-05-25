import random, ipaddress, urllib

# IPv6 addressing and CABA addressing

RLOCs = ['2001:1726:c363:d36e:2ab7:630a:d9d8:1',
         '2001:1726:c363:d36e:2ab7:630a:d9d8:2',
         '2001:1726:c363:d36e:2ab7:630a:d9d8:3',
         '2001:1726:c363:d36e:2ab7:630a:d9d8:4',
         '2001:1726:c363:d36e:2ab7:630a:d9d8:5',
         '2001:1726:c363:d36e:2ab7:630a:d9d8:6',
         '2001:1726:c363:d36e:2ab7:630a:d9d8:7',
         '2001:1726:c363:d36e:2ab7:630a:d9d8:8']

for i in range(0, 100):
    RES = '00000000'
    ASN = '00000000' + str(bin(random.randint(0, 16777216)))[2:]
    SNID = str(bin(random.randint(0, 16777216)))[2:]
    IID = str(bin(random.randint(0, 16777216)))[2:] + str(bin(random.randint(0, 16777216)))[2:] + str(bin(random.randint(0, 16777216)))[2:]
    EID = RES + ASN + SNID + IID
# b = int('00000101111111111111111100000', 2)
    print()

    RLOC = RLOCs[random.randint(0, 7)]
    print(ipaddress.IPv6Address(int(EID, 2)), RLOC)