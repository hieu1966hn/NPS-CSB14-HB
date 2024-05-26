- Giới thiệu về Hàm và cách viết hàm trong Python
- Phân biệt được hàm print và hàm return
- Cách viết hàm thành module và import module sang file python khác để sử dụng.


Hàm: Là một đoạn code dùng để thực hiện một việc cụ thể nào đó. Có 2 loại hàm
+ Hàm built-in: hàm có sẵn Python: print(), input(), int(), float(),...
+ Hàm do người dùng xây dựng: 


Cú pháp viết hàm: 
def sum(a,b):
    .....


Nhận xét: 
- def: cú pháp khai báo hàm 
- sum: tên hàm
- (a, b): tham số

Hàm có giá trị trả về (***): return
- Trả về một giá trị, nếu không có return thì hàm được gọi luôn trả về giá trị là: null
- Khi từ khóa return được gọi sẽ kết thúc hàm ngay lập tức, phần code sau return sẽ không chạy.


Scope Variable
- Phạm vi của biến:
+ Biến chỉ tồn tại và được sử dụng sau khi khai báo (a = 1, b= "hello")
+ Phạm vi sử dụng biến: Được sử dụng ngay sau dòng khai báo biến đó
+ Nếu biến được khai báo trong hàm
def sum(a,b):
    c = a+b
    print("....")
    
print(c) => Không tồn tại. (Giống CCCD)

Có 2 dạng biến
- Global: Là biến được tạo ngoài hàm, được duy trì trong toàn bộ chương trình code.
- Local: Là biến được tạo ra trong hàm. Có tác dụng trong hàm đó và biến mất khi hàm kết thúc.
** Trong trường hợp biến global & local cùng tên, sẽ ưu tiên biến local trước.


Module
- Tách hàm ra file để có thể sử dụng ở nhiều chương trình khác nhau
- File hàm phải ở cùng folder với chương trình
- Cách import: ...



Bài tập thực hành cơ bản với hàm: 
1. Viết hàm tìm số lớn hơn trong 2 số truyền vào 
2. Viết hàm kiểm tra năm nhập vào là năm nhuận hay không nhuận biết
- Năm nhuận là năm chia hết cho 4
- Năm chia hết cho 100 thì phải chia hết cho 400


3. Định nghĩa hàm có thể chấp nhận input là số nguyên và in ra "Đây là một số chẵn" nếu số đó chẵn. In ra "Đây là một số lẻ" nếu số đó là lẻ.
4. Viết hàm tính tổng một list cho trước. Nếu trong List tồn tại phần tử không phải là số => bỏ qua phần tử đó để tiếp tục thực hiện hàm.
5. Viết chương trình chấp nhận chuỗi do người dùng nhập vào, phân tách nhau bởi dấu "," (string.split(,)) và in những từ đó thành chuỗi theo thứ tự bảng chữ cái, phân tách nhau bằng dấu phẩy.