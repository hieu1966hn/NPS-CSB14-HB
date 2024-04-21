# for index in range(10, 21 ):
# print(index) # 10, 11, ... 20

# i = 1
# while i <= 10:
#     if i == 5:
#         i = i + 1
#         continue
#     # else:
#     print(i)
#     i = i + 1
#     # i += 1


# Chữa bài tập
### Câu 1
# n = int(input("Mời nhập số nguyên n"))
# m = int(input("Mời nhập số nguyên m. Biế m > n"))

# for i in range(n,m):
#     if(n>m):
#         print("không hợp lệ")
#         break
#     if(i % 2 == 0):
#         if(i%3 ==0):
#             print(f"số đầu tiên chia hết cho 3 là: {i}")
#         if(i == 6):
#             print("Bỏ qua số 6")
#             continue

#         print(i)


### Bài 2:
# i1 = 0
# while(i1<7):
#     print(i1)
#     i1 += 1


# i2 = 100
# while(i2 <106):
#     print(i2)
#     i2 += 1

# i3 = 9
# while(i3 >0):
#     if(i3 < 7 and i3 >3):
#         i3 -= 1
#         continue
#     print(i3)
#     i3 -= 1


# i4 = 0
# while i4 < 21:
#     if i4 % 3 != 0:
#         i4 += 1
#         continue
#     print(i4)
#     i4 += 1

# n = int(input("Nhập n: "))
# i5 = 0
# while(i5< n+1):
#     print(i5)
#     i5 += 1

### C1
# n = (input("Nhập n: ")) # 1500
# print(str(len(n)))


### C2
# n = (input("Nhập n: ")) # 1500
# n = 15000
# count = 0
# while(n>1):
#     n = n/10
#     count += 1
# print(count)