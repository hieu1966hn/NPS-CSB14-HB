## Cú pháp if else
# a = 500
# b = 300
# if a < b:
#     print("a nhỏ hơn b")
# elif a == b+200:
#     print("b nhỏ hơn a vừa đúng 200 đơn vị")
# #  Điều kiện dưới đồng thời thỏa mãn nhưng sẽ không dạy do điều kiện dòng 6 đã thỏa mãn trước đó.
# elif a+b == 800:
#     print("Tổng 2 số bằng 800 tròn")
# else:
#     print("a không nhỏ hơn b")
### Chú ý: Code chạy từ trên => dưới. nên trong if - elif - else thì đk nào thỏa mãn => chạy và thoát câu điều kiện


### Toán tử logic
# and: tìm kết quả là "false" và trả về giá trị đó. Nếu các điều kiện không có giá trị "false" => trả về "true"
# or: tìm kết quả là "true" và trả về giá trị đó. Nếu các điều kiện không có giá trị "true" => trả về "false"
# not: trả về kết quả ngược lại với điều kiện đó (true/false).
# print(1 < 2 and 2 > 1 and 3 > 9) # => true

a = float(input("Mời người dùng nhập vào kg"))
b = float(input("Mời người dùng nhập vào chiều cao đơn vị mét"))
print(a/(b*b))

