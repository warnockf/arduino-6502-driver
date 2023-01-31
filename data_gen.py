import math
data = []

address_range = int(math.pow(2, 15) - 1)

for i in range(address_range):
    if i % 2:
        data.append(0xEA)
    else:
        data.append(0xFF)

with open("mem.hex", "wb") as f:
    for i in range(address_range):
        f.write(data[i].to_bytes(1, 'big'))

