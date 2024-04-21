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
n = int(input("Mời nhập số nguyên n"))
m = int(input("Mời nhập số nguyên m. Biế m > n"))

for i in range(n,m):
    if(n>m):
        print("không hợp lệ")
        break
    if(i % 2 == 0):
        if(i%3 ==0):
            print(f"số đầu tiên chia hết cho 3 là: {i}")
        if(i == 6):
            print("Bỏ qua số 6")
            continue
        
        print(i)
    
    

