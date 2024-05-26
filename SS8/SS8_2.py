import SS8

# year = 2024
## Thử kiểm tra năm nhuận với hàm ở file SS8.py
# print(
#     SS8.kt_nam_nhuan(year)
# )

### Thử kiểm tra số lớn hơn và in ra với hàm  ở file SS8
# print(SS8.so_lon_hon(1, 10))


###### Chữa bài
a = input("Mời người dùng nhập vào số nguyên")

def kt_chan_le(a):
    ### Kiểm tra a đã là số nguyên hay chưa
    if(a == int(a)):
        if(a%2 == 0):
            return f"{a} là số chẵn"
        else:
            return f"{a} là số lẻ"
    ### Trường hợp a không phải là số nguyên
    else:
        return "a is not integer"
        
print(kt_chan_le(a))