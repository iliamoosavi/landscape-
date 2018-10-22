x = 0

def setup():
    size(640, 480)

def draw():
    global x
    
    if x >= 640:
        x = 0
    x += 3

    background(135, 206, 250) 

    noStroke()
    fill(250, 250 ,250)
    ellipse(x, height/7, 50, 50)
    ellipse(x+30, height/7, 50, 50)
    ellipse(x+10, height/7-20, 50, 50)
    

    fill(0, 255, 0)
    rect(width-640, height-0, 640, -40)
   
    fill( 0, 0, 0 )
    rect(width/2, height/2, 100, 100)
      
    fill(54,  30,  22)
    rect(width/2, height/2, 200, 200)
    
    fill(160,   0,   0)
    triangle(width/2,height/2,width/2+200,height/2,width/2+100,height/2-100)
    
    fill(135, 206, 250)
    rect(width/2 +20, height/2 +20, 50, 50)
    
    fill(128,  96,  64)
    rect(width/2 + 90, height/2+80, 70, 120)
    
    fill(255,255,0)
    ellipse(width/2 + 110,height/ 2+ 150,10,10)
    

    
    
    
    
    
