import socket 
import threading
import pygame
import pickle
from game import Game

err = 0
def sen():
    mess = pickle.dumps(x.pad2PosY)
    client.send(mess)

def rec():
    while True:
        try:
            data = pickle.loads(client.recv(24))
        except:
            global err
            err += 1
            print(err)
        x.pad1PosY = data[0]
        x.ballPosX = data[1]
        x.ballPosY = data[2]

server = "192.168.0.11"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 3001
client.connect((server, port))
x = Game()
recThread = threading.Thread(target=rec)
recThread.start()
fps = pygame.time.Clock()
while True:    
    x.drawScreen()
    fps.tick(60)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                x.pad2Vel -= 3
            if event.key == pygame.K_DOWN:
                x.pad2Vel += 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                x.pad2Vel = 0
            if event.key == pygame.K_DOWN:
                x.pad2Vel = 0
    x.movePad2()
    sen()
