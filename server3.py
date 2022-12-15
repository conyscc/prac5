#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket, threading

LOCALSHOT = "127.0.0.1" # IP - адрес
PORT = 1488 # порт

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # разворачиваем сервер
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((LOCALSHOT, PORT))
print("Сервер запущен")


class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):  # инициализируем новое подключение
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("Новое подключение:", clientAddress)

    def run(self):  # обработка полученных сообщений
        msg = ''
        while True:
            data = self.csocket.recv(4096)
            msg = data.decode()  # декодируем полученные данные
            print('Получено:', msg)
            B = str((int((msg.split()[0])) ** 5678) % int(msg.split()[1]))
            K_A = (int(msg.split()[2]) ** int(B)) % int(msg.split()[1])
            print('Вычисленное значение K_A: ', K_A)
            clientsock.sendall(bytes(B, "UTF-8"))
            if msg == 'EXIT':
                print("Отключение")
                server.close()
                exit()


while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()  # принимаем подключение клиента
    newthread = ClientThread(clientAddress, clientsock)  # новый поток
    newthread.start()

