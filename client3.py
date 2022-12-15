#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
from threading import Thread
import threading
import pickle

SERVER = "127.0.0.1" # IP - адрес
PORT = 1488 # порт

client = socket.socket()
client.connect((SERVER, PORT))
print("Клиент подключен")

def task(): # чтобы "слушать", что отправляет сервер
    while True:
        in_data = client.recv(4096)
        if in_data.decode() == "":
            print("Отключение клиента")
            client.close()
            exit()
        K_B = int(in_data.decode())**1234 % 10 
        print('Вычисленное значение K_B: ', K_B)

def task2(): # чтобы самим вводить данные
    while True:
        out_data = input()
        #print(type(out_data))
        client.sendall(bytes(out_data, "UTF-8"))
        print("Отправлено: " + str(out_data))

t1 = Thread(target=task) # т.к. должны работать одновременно, каждую функцию поместим в отдельный поток
t2 = Thread(target=task2)

t1.start()
t2.start()

