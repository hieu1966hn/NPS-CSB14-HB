Buổi 12: Đọc ghi File.
- File: là đơn vị lưu trữ thông tin trong hệ thống máy tính. File có thể chứa nhiều loại dữ liệu khác nhau gồm: video, hình ảnh, văn bản, âm thanh, ... Các file được tổ chức và lưu trữ trong các thư mục (folder).
- Liệt kê các đuôi file cơ bản: 
+ .mp3: file âm thanh
+ .mp4: file video
+ .doc/.pdf/.pptx/: tài liệu
+ .xlxs: file bảng tính.
+ .psd: .....
+ .exe: file thực thi 


Khái niệm: File path

r: read only, Báo lỗi nếu không có file
a: Thêm nội dung vào cuối file, Tạo file nếu chưa có file đó
w: Ghi đè file, tạo file nếu chưa có file đó
x: Tạo file

Xóa file: 
- import module os
- hàm remove
- hàm rmdir()

Đề bài:
Bài 1a: Ghi dữ liệu vào file
- Tạo  1 file văn bản có tên là example.txt.
- Ghi dòng chữ "Hello World!" vào file này.

Bài 1b: Đọc dữ liệu từ file
- Mở file example.txt đã tạo ở bài tập 1a.
- Đọc và in ra nội dung của file này.

Bài 2: Đếm số dòng trong file
- Viết một chương trình để đếm số dòng trong file example.txt

Bài 3a: Đọc số nguyên từ file
- Tạo một file có tên là numbers.txt và ghi vào file này các số nguyên, mỗi số nằm trên một dòng.
- Viết một chương trình để đọc các số từ file và tính tổng của chúng.
Bài 3b: Tính giá trị trung bình
- Sử dụng file numbers.txt từ bài tập 3a.
- Viết chương trình để tính và in ra giá trị trung bình của các số.
