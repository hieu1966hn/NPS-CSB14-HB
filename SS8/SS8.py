### khai báo một hàm tính tổng 2 số: Trong đó a,b được gọi là tham số khi khai báo hàm.
# def sum1(a, b):
#     # c = a+ b
#     print("Đây là đoạn code trong hàm")
#     return a + b


### gọi hàm: trong đó 1, 2 -> được gọi là đối số truyền vào
# print(sum1(2, 3))

#### Viết hàm tìm số lớn hơn trong 2 số truyền vào
def so_lon_hon(a, b):
    if a > b:
        return a
    else:
        return b


## Gọi hàm
# print(so_lon_hon(1, 3))  # 3

year = 2023

def kt_nam_nhuan(year):
    print(year) ## ?
    if year % 4 == 0:
        return True
    elif year % 100 == 0 and year % 400 == 0:
        raise True
    else:
        return False

### Gọi hàm kt năm nhuận
print(kt_nam_nhuan(2028))


