import pygame

class Game:
    def __init__(self):
        self.ballPosX = 400
        self.ballPosY = 300
        self.ballVelX = 0
        self.ballVelY = 0
        self.ballRad = 12
        self.pad1PosX = 6
        self.pad1PosY = 220
        self.pad2PosX = 789
        self.pad2PosY = 220
        self.padWidth = 5
        self.padHeight = 160
        self.pad1Vel = 0
        self.pad2Vel = 0
        self.screenWidth = 800
        self.screenHeight = 600
        self.BLACK = (0, 0, 0)
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        self.winner = '0'
        
    def drawScreen(self):
        self.screen.fill(self.BLACK)
        self.drawBall()
        self.drawPaddles()
        pygame.display.flip()

    def drawBall(self):
        pygame.draw.circle(self.screen, (255, 255, 255), (self.ballPosX, self.ballPosY), self.ballRad, 0)

    def drawPaddles(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (self.pad1PosX, self.pad1PosY, self.padWidth, self.padHeight))
        pygame.draw.rect(self.screen, (255, 255, 255), (self.pad2PosX, self.pad2PosY, self.padWidth, self.padHeight))

    def coll(self):
        if self.ballPosY - self.ballRad <= 0 or self.ballPosY + self.ballRad >= self.screenHeight:               #Checks and handles for top/bottom wall collision
            self.ballVelY = - self.ballVelY

        if self.ballPosX - self.ballRad <= 0:                
            self.ballVelX = 0
            self.ballVelY = 0
            self.winner = 'P2'

        if self.ballPosX + self.ballRad >= self.screenWidth:
            self.ballVelX = 0
            self.ballVelY = 0
            self.winner = 'P1'

        if abs(self.ballPosX - self.pad1PosX - self.padWidth) <= self.ballRad:                              #Checks and handles Paddle 1 collisions
            if self.ballPosY - self.ballRad >= self.pad1PosY and self.ballPosY + self.ballRad <= self.pad1PosY + self.padHeight:
                self.ballVelX = - self.ballVelX

        elif abs(self.pad2PosX - self.ballPosX) <= self.ballRad:
            if self.ballPosY - self.ballRad >= self.pad2PosY and self.ballPosY + self.ballRad <= self.pad2PosY + self.padHeight:
                self.ballVelX = - self.ballVelX

    def moveBall(self):
        self.ballPosY = self.ballPosY + self.ballVelY
        self.ballPosX = self.ballPosX + self.ballVelX

    def movePad1(self):
        if self.pad1PosY <= 0: 
            self.pad1PosY = self.pad1PosY - self.pad1Vel +1
        if self.pad1PosY >= self.screenHeight - self.padHeight:
            self.pad1PosY = self.pad1PosY - self.pad1Vel - 1   
        self.pad1PosY = self.pad1PosY + self.pad1Vel

    def movePad2(self):
        if self.pad2PosY <= 0: 
            self.pad2PosY = self.pad2PosY - self.pad2Vel +1
        if self.pad2PosY >= self.screenHeight - self.padHeight:
            self.pad2PosY = self.pad2PosY - self.pad2Vel - 1  
        self.pad2PosY = self.pad2PosY + self.pad2Vel


