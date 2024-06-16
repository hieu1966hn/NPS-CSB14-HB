#### khai báo một dictionary Nguoi.
# Hieu = {
#     "id": "123456789123",
#     "name": "Nguyễn Trung Hiếu",
#     "age": 26,
#     "height": "179",
#     "weight": 80,
#     "address": "Tây Hồ - Hà Nội",
#     "hobbies": ["Chơi game", "Ngủ", "Dev"],
# }

# print(Hieu) ## Trong từ điển đã được định nghĩa Hiếu là gì rồi!


#### Truy cập vào tên của biến Hieu đã khai báo;
# print(Hieu["name"])

### Thêm khóa - giá trị vào từ điển Hieu.
# Hieu["crush"] = "Nguyễn Văn A"
# print(Hieu["crush"])


### Cập nhật giá trị trong một key
# Hieu["address"] = "Hà Nội"
# print(Hieu["address"])

#### Xóa 1 khóa - giá trị làm như nào?
# del Hieu["weight"]
# print(Hieu["weight"]) ### Do không còn cân nặng nên ko in ra được terminal.


##### Đếm số lượng key - value: len(dict)
# print(len(Hieu))

#### Xóa toàn bộ key - value bên trong dictionary.
# Hieu.clear()
# print(Hieu)


#### Kiểm tra xem bên trong dict có tồn tại key ... hay không?
# print("name" in Hieu) ## True
# print("job" in Hieu) ## False


##### Sao chép từ điển
# A = Hieu ## liệu được không? => được nhưng không nên sử dụng
# ############# A and Hieu đều đang dùng chung ô nhớ.
# print(A) ####

# ## Đổi tên của dict A
# A["name"] = "Nguyễn Văn A"
# print(A["name"]) # A
# print(Hieu["name"]) # A

########## Cú pháp chuẩn sao chép dictinary
# A = {}  # khai báo biến A là một từ điển rỗng
# A = Hieu.copy()
# print(A)


### Duyệt từ điển theo: key
# for key in Hieu:
#     print(key) ##? key đại diện cho: khóa bên trong dict đó.

### Duyệt từ điển theo: value
# for key in Hieu:
#     print(Hieu[key])


### Kiểm tra xem key - value có tồn tại bên trong dict không?////
# for (key, value) in Hieu.items:


##### Chữa bài tập thực hành: 1
# kho_may_tinh = {
#     "HP": 20,
#     "DELL": 50,
#     "MACBOOK": 12,
#     "ASUS": 30,
# }

### Số lượng macbook có trong kho
# print(kho_may_tinh["MACBOOK"])

### Cho phép người dùng nhập tên hãng để in ra số lượng?
# ten_hang = input("Mời người dùng nhập tên hãng: ")
# if(ten_hang in kho_may_tinh):
#     print(f"Số lượng máy tính là {kho_may_tinh[ten_hang]}")
# else:
#     print(f"Không tồn tại hãng {ten_hang} này")


### Chữa bài tập thực hành 2
### Khai báo đây => Không chỉnh sửa khai báo này.
character = {
    "Name": "Light",
    "Age": 17,
    "Strength": 8,
    "Defense": 10,
    "HP": 100,
    "Backpack": ["Shield", "Bread Loaf"],
    "Gold": 100,
    "Level": 2,
}

#### Thêm 50 vàng
character["Gold"] = character["Gold"] + 50
print(character["Gold"])

#### Thêm FlintStone vào trong list "Backpack":
character["Backpack"].append("FlintStone")
print(character["Backpack"])

#### Thêm key - value cho character
character["Pocket"] = ["MonsterDex", "Flashlight"]
print(character["Pocket"])