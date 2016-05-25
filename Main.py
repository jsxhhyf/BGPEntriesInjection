import random, ipaddress, urllib.parse, urllib.request, json, time

# IPv6 addressing and CABA addressing

RLOCs = ['2001:1726:c363:d36e:2ab7:630a:d9d8:1',
         '2001:1726:c363:d36e:2ab7:630a:d9d8:2',
         '2001:1726:c363:d36e:2ab7:630a:d9d8:3',
         '2001:1726:c363:d36e:2ab7:630a:d9d8:4',
         '2001:1726:c363:d36e:2ab7:630a:d9d8:5',
         '2001:1726:c363:d36e:2ab7:630a:d9d8:6',
         '2001:1726:c363:d36e:2ab7:630a:d9d8:7',
         '2001:1726:c363:d36e:2ab7:630a:d9d8:8']

for i in range(0, 50):
    RES = '00000000'
    ASN = '00000000' + str(bin(random.randint(0, 16777216)))[2:]
    SNID = str(bin(random.randint(0, 16777216)))[2:]
    IID = str(bin(random.randint(0, 16777216)))[2:] + str(bin(random.randint(0, 16777216)))[2:] + str(bin(random.randint(0, 16777216)))[2:]
    EID_b = RES + ASN + SNID + IID

    RLOC = RLOCs[random.randint(0, 7)]
    EID = ipaddress.IPv6Address(int(EID_b, 2))

    url = 'http://10.114.2.33:8080/wm/mappingtablemanager/json'
    value = "{\"dst_eid\":\"" + str(EID) + "\", \"dst_rloc\":\"" + RLOC + "\"}"
    # value = "\"dst_eid\":\"" + str(EID) + "\", \"dst_rloc\":\"" + RLOC + "\""
    print(value)
    # data = urllib.parse.urlencode(value)
    binary_data = value.encode('utf8')
    req = urllib.request.Request(url, binary_data)
    response = urllib.request.urlopen(req)
    print(response.read())
    time.sleep(1)