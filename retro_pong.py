#Lauri Tiismaa Devon Peeterson "Retro Pong"

#ipordib turtle mooduli mida me mängu tegemiseks kasutame
import turtle

#Mängu ekraani sätestamine
#Loob mängu ekraani
screen = turtle.Screen()
#Paneb ekraanile nimeks "Retro Pong"
screen.title("Retro Pong")
#Määrab ekraani piirid
screen.setup(width=1000 , height=600)

#Vasakpoolse pulga loomine
pulk1 = turtle.Turtle()
#Määrab pulga kiiruse
pulk1.speed(0)
#Määrab pulga kuju
pulk1.shape("square")
#Määrab pulga värvi
pulk1.color("black")
#Määrab pulga suuruse
pulk1.shapesize(stretch_wid=6, stretch_len=2)
#Kasutame penup commandi et liikuv pulga objekt ekraanile jälgi ei jätaks
pulk1.penup()
#Määrab pulga asukoha
pulk1.goto(-400, 0)

#Parempoolse pulga loomine

pulk2 = turtle.Turtle()
pulk2.speed(0)
pulk2.shape("square")
pulk2.color("black")
pulk2.shapesize(stretch_wid=6, stretch_len=2)
pulk2.penup()
pulk2.goto(400, 0)

#Palli loomine

pall = turtle.Turtle()
#Määrab palli kiiruse
pall.speed(1)
#Määrab palli kuju
pall.shape("circle")
#Kasutame penup commandi et liikuv pulga objekt ekraanile jälgi ei jätaks
pall.penup()
#Määrab palli asukoha
pall.goto(0, 0)
#Määrame dx ja dy mis hiljem määravad palli kiirust 
pall.dx = 3
pall.dy = -3
pall.setx(0)
pall.sety(0)


#Skoori lisamine

#Määrab mängjate algskoorid
mangja1 = 0
mangja2 = 0
#Skoori kuvamine mängu ajal
skoor = turtle.Turtle()
skoor.speed(0)
skoor.penup()
#Peidame turtle et skoori saaks kuvada
skoor.hideturtle()
#Määrame skoori asukoha
skoor.goto(0, 260)
#Skoori tekst
skoor.write("Mängja1 : 0       Mängja2: 0", align="center", font=("Courier", 20, "bold"))

#Pulkade liigutamine

#defineerib pulk1 liikumise üles
def pulk1up():
    # Võtab pulga 1 hetkese kordinaadi ja lisab sellele 15 kui kindel nupp on alla vajutatud
    y = pulk1.ycor()
    if y < 240:
        y += 15
    pulk1.sety(y)

# Defineerib pulk1 liikumise alla
def pulk1down():
    # Võtab pulga 1 hetkese kordinaadi ja lahutab sellest 15 kui kindel nupp on alla vajutatud
    y = pulk1.ycor()
    if y > -230:
        y -= 15
    pulk1.sety(y)

# Defineerib pulk2 liikumise üles
def pulk2up():
    y = pulk2.ycor()
    if y < 240:
        y += 15
    pulk2.sety(y)

# Defineerib pulk2 liikumise alla
def pulk2down():
    y = pulk2.ycor()
    if y > -230:
        y -= 15
    pulk2.sety(y)


#Määrame nupud millega liigutada pulk1-te ja pulk2-te üles ja alla
screen.listen()
screen.onkeypress(pulk1up, "w")
screen.onkeypress(pulk1down, "s")
screen.onkeypress(pulk2up, "Up")
screen.onkeypress(pulk2down, "Down")

#Loon funktsiooni millega saab panna mängu pausile
def pausi_menu():
    global is_paused
    if is_paused:
        is_paused = False
        skoor.clear()
        skoor.write("Mängja1 : {}    Mängja2: {}".format(mangja1, mangja2), align="center", font=("Courier", 20, "bold"))
    else:
        is_paused = True
        skoor.clear()
        skoor.write("Mäng peatatud", align="center", font=("Courier", 20, "bold"))
        
# Kuulame ESC klahvi vajutust pausi ja jätkamise jaoks
screen.onkeypress(pausi_menu, "Escape")

# Kui mäng algab siis mäng pole pausil
is_paused = False

while True:
    #uuendab ekraanil toimuvat
    screen.update()
    #kui esc klahvi pole vajutatud käivitub mäng
    if not is_paused:
    
        screen.update()
 
        pall.setx(pall.xcor()+pall.dx)
        pall.sety(pall.ycor()+pall.dy)
 
        # mõõdab palli liikumist vastu lage ja põrandat ja põrgatab palli tagasi kui pall jõuab teatud asukohta
        if pall.ycor() > 280:
            pall.sety(280)
            pall.dy *= -1
 
        if pall.ycor() < -280:
            pall.sety(-280)
            pall.dy *= -1
        # Mõõdab kas pall puudutab vasakut või paremat seina, kui see juhtub liigub pall tagasi keskele ja üks mängjatest saab punkti
        if pall.xcor() > 500:
            pall.goto(0, 0)
            pall.dy *= -1
            mangja1 += 1
            skoor.clear()
            skoor.write("mängja1 : {}    mängja2: {}".format(
                          mangja1, mangja2), align="center",
                          font=("Courier", 20, "bold"))
 
        if pall.xcor() < -500:
            pall.goto(0, 0)
            pall.dy *= -1
            mangja2 += 1
            skoor.clear()
            skoor.write("mängja1 : {}    mängja2: {}".format(
                                     mangja1, mangja2), align="center",
                                     font=("Courier", 20, "bold"))
 
        # Palli ja pulga kokkupõrge
        if (pall.xcor() > 360 and pall.xcor() < 370) and (pall.ycor() < pulk2.ycor()+40 and
            pall.ycor() > pulk2.ycor()-40):
            pall.setx(360)
            pall.dx*=-1
        
        if (pall.xcor()<-360 and pall.xcor()>-370) and (pall.ycor()<pulk1.ycor()+40 and
            pall.ycor()>pulk1.ycor()-40):
            pall.setx(-360)
            pall.dx*=-1