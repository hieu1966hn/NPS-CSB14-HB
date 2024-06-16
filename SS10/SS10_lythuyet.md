Nội dung buổi học: CẤU TRÚC DỮ LIỆU
- Tìm hiểu về Dictionary
- Các thao tác với Dictionary


*Khái niệm: Dictionary là kiểu dữ liệu được dùng để lưu trữ dữ liệu theo cặp key - value.

*Cách khai báo:
var_name = {
    "key1": value1,
    "key2": value2,
    "key3": value3,
    ....

}

Duyệt từ điển: Cú pháp
for key in dict:
    <statement>



Bài tập thực hành: 
1. Init dictionary - Dưới đây là thông tin về số lượng máy tính theo hãng trong 1 kho của một shop:
 HP: 20
 DELL: 50
 MACBOOK: 12
 ASUS: 30
Yêu cầu
- Khai báo một dict để biểu diễn thông tin trên
a) Read - Hiện ra số lượng MACBOOK có trong kho
b) Read - with key from input - lặp lại câu 2 với hãng máy tính được nhập từ người dùng? (nếu không tồn tại hãng máy tính => hiển thị thông báo "không tồn tại").