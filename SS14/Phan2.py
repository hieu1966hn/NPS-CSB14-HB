### Ban đầu;
storage = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30,
}

tong = 0
for key in storage:
    tong = tong + storage[key]
    # print(storage[key]) ##? key đại diện cho: khóa bên trong dict đó.
print(tong)
