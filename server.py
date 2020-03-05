import socket
import threading
import pygame
import pickle
from game import Game

def rec():
    while True:
        try:
            data = conn.recv(30)
        except:
            pass
        x.pad2PosY = int(pickle.loads(data))

def sen():
    mess = pickle.dumps([x.pad1PosY, x.ballPosX, x.ballPosY])
    conn.send(mess)

serAdd = ''
port = 3001
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server.bind((serAdd, port))
except socket.error as err:
    str(err)
server.listen(2)
print("Waiting client...")
conn, add = server.accept()
x = Game()
x.ballVelX = 4
x.ballVelY = -4
recThread = threading.Thread(target=rec)
recThread.start()
fps = pygame.time.Clock()
while x.winner == '0':    
    x.drawScreen()
    x.coll()
    x.moveBall()
    fps.tick(60)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                x.pad1Vel -= 3
            if event.key == pygame.K_DOWN:
                x.pad1Vel += 3 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                x.pad1Vel += 3
            if event.key == pygame.K_DOWN:
                x.pad1Vel -= 3
        if event.type == pygame.QUIT:
            pygame.quit()
    x.movePad1()
    sen()
recThread.join()    
print(x.winner, " is the winner!")
pygame.quit()