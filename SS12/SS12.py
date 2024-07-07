# f = open("./SS12/demofile.txt")
# print(f.readline())
# print(f.readline())

### Dùng vòng lặp để line by line (giống readline())
# for x in f:
#     print(x)


##### Write to Existing File
# f = open("./SS12/demofile.txt", "a")
# f.write("Now the file has more content!")
# f.close()


### Mở và đọc file sau khi thêm nội dung:
# f = open("./SS12/demofile.txt", "r")
# print(f.read())
### Có open thì phải có close
# f.close()


##### Mở file demofile2.txt và ghi đè nội dung bên trong nó.
# f = open("./SS12/demofile2.txt", "w")
# f.write("Woop! I have deleted the content!")
# f.close()

### Mở file và đọc sau khi ghi đè file vừa rồi
# f = open("./SS12/demofile2.txt", "r")
# print(f.read())


##### tạo một file nếu nó không tồn tại.
# f = open("./SS12/demofile3.txt", "w")


##### Delete a file
# import os
# os.remove("./SS12/demofile.txt")


#### Ví dụ minh họa: kiểm tra file tồn tại, sau đó xóa nó.
# import os
# if os.path.exists("./SS12/demofile2.txt"):
#     os.remove("./SS12/demofile2.txt")
# else:
#     print("The file does not exist")

#### Xóa folder: os.rmdir()
import os

#### Tạo foder
# os.mkdir("./SS13") ### make directories

#### Xóa foler
# os.rmdir("./SS13") ### remove directories


#### Chữa bài 3a
f = open("./SS12/numbers.txt", "w")
f.write("10\n20\n30\n40\n50")
f.close()

f = open("./SS12/numbers.txt", "r")
total = 0
for i in f:
    # print(i)
    i  = int(i)
    total = total + i
print(total)