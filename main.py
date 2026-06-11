rings = [] 
for i in range(100) : 
    box(pos=vec(90,i,180),size=vec(80,80,70), color=vec(0/255,0/255,i/255))
    box(pos=vec(-90,i,180),size=vec(80,80,70), color=vec(0/255,0/255,i/255))
body = box(pos=vec(0, 0, 0),size=vec(400,400,400), color=vec(247/255,218/255,234/255))
right = box(pos=vec(90, 100, 20),size=vec(63,63,400), color=vec(1,1,1))
left = box(pos=vec(-90, 100, 20),size=vec(63,63,400), color=vec(1,1,1))


for i in range(220) :
    rings.append(ring(axis = vec(0,0.2,1), pos=vec(0, -110, i), radius = 50, color=vec(247/255,218/255,234/255)))
    

gu = ellipsoid(pos=vec(0, -130, 200), length=80, height=70, width=70,color=vec(227/255,53/255,96/255)) 

iban = cylinder(pos=vec(0, -110, 130), axis=vec(0, 0, 1), color=vec(128/255,31/255,14/255),size=vec(80,100,100))
arm1 = box(pos=vec(160, -50, 0),size=vec(200,200,250), color=vec(247/255,218/255,234/255),  axis=vec(0.5,0.2,0))
arm2 = box(pos=vec(-160, -50, 0),size=vec(200,200,250), color=vec(247/255,218/255,234/255),  axis=vec(0.2,0.5,0))

leg1 = ellipsoid(pos=vec(130, -240, 100), length=200, height=140, width=300, color=vec(204/255,70/255,104/255),axis=vec(0.5,-0.1,-0.2))
leg2 = ellipsoid(pos=vec(-130, -240, 100), length=200, height=140, width=300, color=vec(204/255,70/255,104/255),axis=vec(0.5,0.1,0.2))

kirby = compound( [body,arm1, arm2, leg1, leg2]+ rings )
eye = compound( [right, left] )
import random

while True : 

    rate(100)
    k = keysdown()
    if ' 'in k:
        dx = random.uniform(-1, 1)
        dy = random.uniform(-1, 1)
        kirby.pos.x = kirby.pos.x + dx
        kirby.pos.y = kirby.pos.y + dy
        kirby.color = vec(random.random(),random.random(),random.random())
        eye.pos.x = eye.pos.x + dx
        eye.pos.y = eye.pos.y + dy
        
