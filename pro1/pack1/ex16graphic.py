# turtle 모듈(라이브러리)로 그래픽

from turtle import *  # *은 크게 추천은 안 함


p = Pen()
p.color("red", "yellow")
p.begin_fill()

while True:
    p.forward(200)
    p.left(170)
    if abs(p.pos()) < 1:
        break
p.end_fill()

# https://www.pygame.org/

# 카페 => python => 28번 벽돌깨기



# conda install pygame (아나콘다) 이 안 되면, 

# pip install pygame
