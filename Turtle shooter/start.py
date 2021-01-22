import turtle
import os
import math
import random

#setup the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
turtle.register_shape("player.gif")
turtle.register_shape("enemy.gif")

#border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

#Score
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align = "left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#Enemy
#enemy = turtle.Turtle()
#enemy.color("red")
#enemy.shape("circle")
#enemy.penup()
#enemy.speed(0)
#enemy.setposition(-200, 230)



#Select number of enemies
number_of_enemies = 5
#create empty list
enemies = []
#Add enemies
for i in range (number_of_enemies):
    enemies.append(turtle.Turtle())
    
for enemy in enemies:
    enemy.color("red")
    enemy.shape("enemy.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(100,250)
    enemy.setposition(x, y)

enemyspeed = 2    

#Create player bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

bulletstate = "ready"


#Movement  of player
playerspeed = 15

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x<-280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x>280:
        x = 280
    player.setx(x)
 
def fire_bullet():
     global bulletstate
     if bulletstate == "ready":
         bulletstate = "fire"
         x = player.xcor()
         y = player.ycor() + 10
         bullet.setposition(x, y) 
         bullet.showturtle()
       
#Check if the bullet hits the enemy
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(),2) + math.pow(t1.ycor() - t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

#Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right") 
turtle.onkey(fire_bullet,"space")

#Main game loop
while True:
    
    for enemy in enemies:
        
        #enemy motion
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        
        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1
            
            
        if enemy.xcor() < -280:
            
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1
        
        if isCollision(bullet, enemy):
            #hide the bullet and send it down
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0,-400)
            #reset the enemy
            x = random.randint(-200,200)
            y = random.randint(100,250)
            enemy.setposition(x, y)
            #update score
            score+=10
            score_pen.clear()
            scorestring = "Score: %s" %score
            score_pen.write(scorestring, False, align = "left", font=("Arial", 14, "normal"))
            
        if isCollision(enemy, player):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over!!!")
            break
    
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
        
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"
    
    


delay = raw_input("Press enter to begin")