for i in range(100) : 
    box(pos=vec(90,i,180),size=vec(80,80,70), color=vec(0/255,0/255,i/255))
    box(pos=vec(-90,i,180),size=vec(80,80,70), color=vec(0/255,0/255,i/255))
box(pos=vec(0, 0, 0),size=vec(400,400,400), color=vec(247/255,218/255,234/255))
box(pos=vec(90, 100, 20),size=vec(63,63,400), color=vec(1,1,1))
box(pos=vec(-90, 100, 20),size=vec(63,63,400), color=vec(1,1,1))
text(text='Kirby', align='center', color=vec(1,1,1) , pos=vec(0,400,0),  width=100)

for i in range(250) :
    ring(axis = vec(0,0,1), pos=vec(0, -110, i), radius = 50, color=vec(247/255,218/255,234/255), )
    
ellipsoid(pos=vec(0, -110, 260), length=40, height=10, width=30)
