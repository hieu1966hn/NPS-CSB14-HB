### 1. Tạo list: Tạo một list bằng cách đặt các phần tử bên trong dấu ngoặc vuông [];

# fruits = ['apple', "banana" , "orange"]
#           0          1          2
## 2. Truy cập phần tử: Các phần tử trong list được đánh chỉ số vị trí bắt đầu từ 0.
## In ra giá trị "orange"
# print(fruits[2])

## 3. Thay đổi phần tử trong danh sách: Bằng cách gán giá trị một phần tử bằng giá trị  
## mới với chỉ số vị trí tương ứng

# fruits[1] = "grape"

## 4. in ra cả danh sách.
# print(fruits)

## 5. Thêm phần tử nữa vào danh sách: sử dụng phương thức append() để thêm 1 phần tử vào cuối list
# fruits.append("mangosteen")
# print(fruits)


## 6. Xóa phần tử trong danh sách: Sử dụng remove() để xóa 1 phần tử khỏi list
# fruits.remove("apple")
# print(fruits)


## 7. Sắp xếp list: tăng dần, giảm dần: Sử dụng sort() để sx các phần tử tăng dần trong List
# numbers = [3,1,2,5,10]
# numbers.sort()
# print(numbers) # kết quả: List được sx tăng dần.
# # sx giảm dần
# numbers.sort(reverse=True)
# print(numbers) # kết quả: List được sx .

## 8. Kiểm tra tình trạng List: Kiểm tra được xem List rỗng hay không bằng cách đánh giá nó như một giá trị Boolean
# empty_list = []
# print(bool(empty_list)) # Kết quả ra gì? False - không có phần tử
# non_empty_list = [1,2,3]
# print(bool(non_empty_list)) # Kết quả ra gì? True - có phần tử trong danh sách.


### 9. Duyệt List
## C1: Duyệt với for item in list => item: giá trị từng phần tử sau mỗi lần lặp.
# arr = [1,2,3]
# for i in arr:
#     print(i)

## C2: Duyệt với for i in range(len(list)) => i: vị trí phần tử trong danh sách.
# for index in range(len(arr)):
#     print(index)


### 10. Sao chép mảng: Sử dụng copy() hoặc slice[:]
# arr1 = ["Giường", "Bàn", "Ghế"] # Khang
# # arr2 = arr1 # Thùy Anh. => cú pháp copy này sai
# arr2 = arr1.copy() # tạo ra 1 ô nhớ mới với đầy đủ phần tử từ arr1
# arr1[0] = "Đèn ngủ"
# print(arr2)


##### Tuple
## Tạo Tuple
# fruits = ('apple', 'banana', "orange")
# single_fruit = ('watermelon',) #Cần dấu "," để Python biết đây là tuple.

## truy cập phần tử: giống hệt list
# print(fruits[0])

## sắp xếp tuple: Dù tuple là bất biến nhưng chúng ta vẫn có thể sx phần tử bằng hàm: sorted() 
## hoặc comprehension
# numberTuple = (3,2,4,10)
# sorted_number = sorted(numberTuple)
# print(sorted_number)




##### Giải bài tập thực hành trên lớp
## Bài a;
a = input("Mời người dùng nhập món 1")
b = input("Mời người dùng nhập món 2")
c = input("Mời người dùng nhập món 3")
foods = []
foods.append(a)
foods.append(b)
foods.append(c)

print(foods)

# Duyệt danh sách để in ra từng phần tử
for index in foods:
    print(index)

removeMonAn = input("Mời người dùng nhập vào món ăn muốn bỏ")
print(f"Món ăn người dùng muốn bỏ là {removeMonAn}")
foods.remove(removeMonAn)
print(foods)


