#!/usr/bin/python
# -*- coding: utf8 -*-

import socket               # Import socket module

s = socket.socket()         # Tạo đối tượng socket (mặc định là TCP trên nền IPv4)
host = socket.gethostname() # Xác định tên localhost
port = 12345               # Xác định port muốn dùng
s.bind((host, port))        # Kết nối đến socket

s.listen(5)                 # Server lắng nghe 5 Client cùng 1 lúc
while True:
   c, addr = s.accept()     # Thiết lập kết nối
   print 'Got connection from', addr
   c.send('Thank you for connecting') #Gửi dữ liệu đến Client
   c.close()