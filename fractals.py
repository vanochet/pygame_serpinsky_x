from pygame import *
from random import randint as rint,choice,seed


sc = display.set_mode((640, 640))

size = Vector2(sc.get_size())

radius = min((size.x, size.y))/2-10

center = size/2

for i in range(3, 360):
    sc.fill((255,255,255))

    edges = i

    k = (edges-2)/(edges-1)

    angle = 360/edges

    dots = []

    vec = Vector2(0,-1)*radius

    if not edges % 2:
        vec.rotate_ip(angle/2)

    for e in range(edges):
        dots += [center+vec]
        vec.rotate_ip(angle)

    pos = Vector2(dots[0])

    clr = (0,0,0)

    #sf = Surface(size,SRCALPHA)

    for _ in range(2000):
        draw.circle(sc,clr,pos,2)
    
        pos += (choice(dots)-pos)*k
    
        #sc.fill((255,255,255))
        #sc.blit(sf,(0,0))
    
        draw.polygon(sc,clr,dots,3)
        #draw.circle(sc,(255,0,0),target,10)
    
        display.flip()