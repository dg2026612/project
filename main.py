for i in range(100) : 
    box(pos=vec(90,i,180),size=vec(80,80,70), color=vec(0/255,0/255,i/255))
    box(pos=vec(-90,i,180),size=vec(80,80,70), color=vec(0/255,0/255,i/255))
box(pos=vec(0, 0, 0),size=vec(400,400,400), color=vec(247/255,218/255,234/255))
box(pos=vec(90, 100, 20),size=vec(63,63,400), color=vec(1,1,1))
box(pos=vec(-90, 100, 20),size=vec(63,63,400), color=vec(1,1,1))

for i in range(220) :
    ring(axis = vec(0,0.2,1), pos=vec(0, -110, i), radius = 50, color=vec(247/255,218/255,234/255))
    
ellipsoid(pos=vec(0, -130, 200), length=80, height=70, width=70,color=vec(227/255,53/255,96/255)) 
cylinder(pos=vec(0, -110, 130), axis=vec(0, 0, 1), color=vec(128/255,31/255,14/255),size=vec(80,100,100))
box(pos=vec(150, 0, 0),size=vec(200,200,200), color=vec(247/255,218/255,234/255),  axis=vec(0,0,0.7))
