#!/usr/bin/python
# -*- coding: utf8 -*-
import socket               # Import socket module

s = socket.socket()         # Tạo đối tượng socket
host = socket.gethostname() # Xác định tên localhost
port = 12345                # Xác định port

s.connect((host, port)) #Kết nối đến Server
print s.recv(1024) #Nhận dữ liệu từ Server với Buffer là 1024 bytes
s.close()                    # Đóng kết nối