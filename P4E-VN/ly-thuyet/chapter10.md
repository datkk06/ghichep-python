#Tổng hợp lý thuyết chapter 10.

#Tuple.

- Một tuple là một dãy các đối tượng không bị thay đổi trong python , vì thế tuple là không thể bị thay đổi. 
Các tuple cũng là các dãy giống như list.

- Ví dụ về tuple :

```sh
sv = ('Dat',1,2,3,'Thanh')
gv = "Cuong",11.9,2
```

- Một tuple trống không chưa một phần tử nào : tup1 = ()
- Một tuple chỉ có giá trị đơn phải có dấu phảy ở cuối : tup2 = (50,)
- Các tuple có thể được lồng với nhau : 

```sh
sv = ('Dat',1,2,3,'Thanh')
gv = sv, ("Cuong",11.9,2)
```

- Truy cập các giá trị bên trong tuple :

- Ví dụ ta có các tuple như sau :

```sh
sv = ('Dat',1,2,3,'Thanh')
gv = ("Cuong",11.9,2)
```

- Thực hiện lấy ra các giá trị :

```sh
sv[0:2]
gv[0]
```

- Giống như String và List, bạn cũng có thể sử dụng toán tử nối + và toán tử lặp * với tuple. Điểm khác biệt 
là nó tạo ra một tuple mới, không tạo ra một chuỗi hay list.

- Với tuple việc xóa từng phần tử trong nó là không thể chúng ta chỉ có thể xóa toàn bộ tuple với lệnh `del` như sau :

```sh
del tup1
```

- Cập nhật dữ liệu trong tuple :

```sh
tup1 = (1,2,3,4)
tup1[0] = 5
```

- Các hàm được xây dựng sẵn cho tuple trong python :

| Tên hàm | Mô tả |
|---------|-------|
| Hàm cmp(tuple1, tuple2) | So sánh 2 tuple với nhau |
| Hàm len(tuple) | Trả về độ dài của tuple |
| Hàm max(tuple) | Trả về item có giá trị lớn nhất của tuple đã cho |
| Hàm min(tuple) | Trả về item có giá trị nhỏ nhất của tuple đã cho |
| Hàm tuple(seq) | CHuyển một dãy về tuple |

```sh
Lý do vì sao chúng ta nên sử dụng tuple :
```

- Trình xử lý các tuple là nhanh hơn các List.
- Làm cho dữ liệu an toàn hơn bởi vì tuple là không thay đổi (immutable) và vì thế nó không thể bị thay đổi.
- Các tuple được sử dụng để định dạng String.