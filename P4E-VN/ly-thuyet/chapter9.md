#Tổng hợp lý thuyết từ chapter9.

#Dictionanries.

- Là tập hợp các cặp key và value không có thứ tự , nó là một container mà chứa các dữ liệu được bao trong dấu 
{} . Mỗi cặp key - value được coi như là một item, key mà đã truyền cho item đó thì phải là duy nhất , trong khi 
đó value có thể là bất kỳ giá trị nào , key phải là một kiểu dữ liệu không thay đổi như là chuỗi hoặc tuple.

- Ví dụ :

```sh
a = {'Ten': 'Dat', 'SN': 1996, 'Que Quan': 'Ninh Binh'}
print a
```

- Chỉ được sử dụng chuỗi với tuple để làm key cho dictionary.

- Truy cập các giá trị trong Dictionary : 

```sh
sv1 = {'sbd': 1,'Ten': 'Dat', 'Lop': 'AT11C'}
sv2 = {'sbd': 2, 'Ten': 'Thanh', 'Lop': 'AT11A'}

print 'Sinh viên 1 có tên là', sv1['Lop']
print "Sinh vien 1 học lớp", sv1['Lop']
```

- Cập nhật Dict :

- Ví dụ chúng ta có một Dict như sau :

```sh
sv1 = {'sbd': 1,'Ten': 'Dat', 'Lop': 'AT11C'}
sv2 = {'sbd': 2, 'Ten': 'Thanh', 'Lop': 'AT11A'}
```

- Ta có thể thêm cũng như cập nhật lại các value tương ứng với các key trong Dict :

```sh
sv1['sbd': 5]
sv1['Que Quan': 'Ninh Binh']
```

- Xóa phần tử trong Dict:

- Ví dụ ta có dict như sau :

```sh
sv1 = {'sbd': 1,'Ten': 'Dat', 'Lop': 'AT11C'}
sv2 = {'sbd': 2, 'Ten': 'Thanh', 'Lop': 'AT11A'}
```

- Bây giờ ta muốn xóa key 'sbd' trong dict sv1 ta làm như sau :

```sh
del sv1['sbd']
```

- ta muốn xóa cả dict sv2 ta làm như sau :

```sh
del sv2
```

- Một số hàm được xây dựng sẵn dùng cho dict trong python :

| Tên Hàm | Miêu tả |
|---------|---------|
| cmp(dict1,dict2) | So sánh các phần tử của cả 2 dict |
| len(dict) | Độ dài cuar dict , nó sẽ là số item trong dict này |
| str(dict) | Tạo ra một biểu diễn chuỗi có thể in được của dict |
| type(variable) | Trả về kiểu biến đã truyền . Nếu biến đã truyền là kiểu Dictionary thì nó sẽ trả về kiểu Dictionary |

- Một số phương thức xây dựng sẵn cho Dict có thể xem thêm tại [đây](http://vietjack.com/python/dictionary_trong_python.jsp)



