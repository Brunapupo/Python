import turtle

flor = turtle.Turtle()

r = 100

flor.speed(20) #velocidade para desenhar

#cabo da flor
flor.up()
flor.left(270)
flor.forward(100)
flor.down()
flor.width(15)
flor.color('#006400', '#008000')
flor.begin_fill()
flor.fd(240)
flor.up()
flor.left(170)
flor.forward(90)
flor.seth(-351)
flor.down()
flor.circle(r, 40)
flor.seth(150)
flor.circle(r, 40)
flor.left(260)
flor.up()
flor.forward(152)
flor.end_fill()

#petola 1
flor.width(4)
flor.color('#000000', '#DDA0DD')   #Cor da caneta e preenchimento
flor.begin_fill()
flor.up()    #primeira petála
flor.seth(-60)
flor.down()
flor.circle(r, 70)
flor.seth(120)
flor.circle(r, 70)
flor.end_fill()

#petola 2

flor.width(4)
flor.color('#000000', '#DDA0DD')   #Cor da caneta e preenchimento
flor.begin_fill()
flor.up()
flor.seth(-20)
flor.down()
flor.circle(r, 70)
flor.seth(160)
flor.circle(r, 70)
flor.end_fill()

#petola 3
flor.width(4)
flor.color('#000000', '#DDA0DD')   #Cor da caneta e preenchimento
flor.begin_fill()
flor.up()
flor.seth(8)
flor.down()
flor.circle(r, 70)
flor.seth(187)
flor.circle(r, 70)
flor.end_fill()

#petola 4
flor.width(4)
flor.color('#000000', '#DDA0DD')   #Cor da caneta e preenchimento
flor.begin_fill()
flor.up()
flor.seth(55)
flor.down()
flor.circle(r, 70)
flor.seth(235)
flor.circle(r, 70)
flor.end_fill()

#petola 5
flor.width(4)
flor.color('#000000', '#DDA0DD')   #Cor da caneta e preenchimento
flor.begin_fill()
flor.up()
flor.seth(95)
flor.down()
flor.circle(r, 70)
flor.seth(275)
flor.circle(r, 70)
flor.end_fill()

#petola 6
flor.width(4)
flor.color('#000000', '#DDA0DD')   #Cor da caneta e preenchimento
flor.begin_fill()
flor.up()
flor.seth(130)
flor.down()
flor.circle(r, 70)
flor.seth(310)
flor.circle(r, 70)
flor.end_fill()

#petala 7
flor.width(4)
flor.color('#000000', '#DDA0DD')   #Cor da caneta e preenchimento
flor.begin_fill()
flor.up()
flor.seth(170)
flor.down()
flor.circle(r, 70)
flor.seth(350)
flor.circle(r, 70)
flor.end_fill()

#petola 8
flor.width(4)
flor.color('#000000', '#DDA0DD')   #Cor da caneta e preenchimento
flor.begin_fill()
flor.up()
flor.seth(216)
flor.down()
flor.circle(r, 70)
flor.seth(395)
flor.circle(r, 70)
flor.end_fill()

#petola 9
flor.width(4)
flor.color('#000000', '#DDA0DD')   #Cor da caneta e preenchimento
flor.begin_fill()
flor.up()
flor.seth(260)
flor.down()
flor.circle(r, 70)
flor.seth(440)
flor.circle(r, 70)
flor.end_fill()

#chuva de petolas

flor.up()
flor.forward(800)
flor.width(4)
flor.color('#000000', '#FEE5FF')   #Cor da caneta e preenchimento
flor.begin_fill()
flor.up()
flor.seth(95)
flor.down()
flor.circle(r,60)
flor.seth(275)
flor.circle(r, 60)
flor.end_fill()

flor.up()
flor.forward(300)
flor.down()
flor.width(4)
flor.color('#000000', '#C6D1F7')   #Cor da caneta e preenchimento
flor.begin_fill()
flor.up()
flor.seth(55)
flor.down()
flor.circle(r, 70)
flor.seth(235)
flor.circle(r, 70)
flor.end_fill()


flor.up()
flor.forward(300)
flor.down()
flor.width(4)
flor.color('#000000', '#FFFAC7')   #Cor da caneta e preenchimento
flor.begin_fill()
flor.up()
flor.seth(55)
flor.down()
flor.circle(r, 70)
flor.seth(235)
flor.circle(r, 70)
flor.end_fill()

flor.up()
flor.left(90)
flor.forward(500)
flor.down()
flor.width(4)
flor.color('#000000', '#DFFED5')   #Cor da caneta e preenchimento
flor.begin_fill()
flor.up()
flor.seth(45)
flor.down()
flor.circle(r, 70)
flor.seth(225)
flor.circle(r, 70)
flor.end_fill()

flor.up()
flor.left(90)
flor.forward(350)
flor.down()
flor.width(4)
flor.color('#000000', '#FFE2B0')   #Cor da caneta e preenchimento
flor.begin_fill()
flor.up()
flor.seth(25)
flor.down()
flor.circle(r, 70)
flor.seth(205)
flor.circle(r, 70)
flor.end_fill()

flor.up()
flor.forward(300)
flor.width(4)
flor.color('#000000', '#FEE5FF')   #Cor da caneta e preenchimento
flor.begin_fill()
flor.up()
flor.seth(95)
flor.down()
flor.circle(r,60)
flor.seth(275)
flor.circle(r, 60)
flor.end_fill()

flor.up()
flor.forward(300)
flor.down()
flor.width(4)
flor.color('#000000', '#C6D1F7')   #Cor da caneta e preenchimento
flor.begin_fill()
flor.up()
flor.seth(55)
flor.down()
flor.circle(r, 70)
flor.seth(235)
flor.circle(r, 70)
flor.end_fill()


flor.up()
flor.forward(250)
flor.down()
flor.width(4)
flor.color('#000000', '#FFFAC7')   #Cor da caneta e preenchimento
flor.begin_fill()
flor.up()
flor.seth(55)
flor.down()
flor.circle(r, 70)
flor.seth(235)
flor.circle(r, 70)
flor.end_fill()

flor.up()
flor.left(90)
flor.forward(250)
flor.down()
flor.width(4)
flor.color('#000000', '#C6D1F7')   #Cor da caneta e preenchimento
flor.begin_fill()
flor.up()
flor.seth(55)
flor.down()
flor.circle(r, 70)
flor.seth(235)
flor.circle(r, 70)
flor.end_fill()

flor.up()
flor.left(270)
flor.forward(500)
flor.width(4)
flor.color('#000000', '#FEE5FF')   #Cor da caneta e preenchimento
flor.begin_fill()
flor.up()
flor.seth(95)
flor.down()
flor.circle(r,60)
flor.seth(275)
flor.circle(r, 60)
flor.end_fill()

flor.up()
flor.left(180)
flor.forward(350)
flor.down()
flor.width(4)
flor.color('#000000', '#FFE2B0')   #Cor da caneta e preenchimento
flor.begin_fill()
flor.up()
flor.seth(55)
flor.down()
flor.circle(r, 70)
flor.seth(235)
flor.circle(r, 70)
flor.end_fill()

flor.up()
flor.left(90)
flor.forward(200)
flor.down()
flor.up()
flor.left(180)
flor.forward(500)
flor.down()
flor.width(4)
flor.color('#000000', '#DFFED5')   #Cor da caneta e preenchimento
flor.begin_fill()
flor.up()
flor.seth(45)
flor.down()
flor.circle(r, 70)
flor.seth(225)
flor.circle(r, 70)
flor.end_fill()

flor.up()
flor.left(220)
flor.forward(900)
flor.down()
flor.width(4)
flor.color('#000000', '#FFE2B0')   #Cor da caneta e preenchimento
flor.begin_fill()
flor.up()
flor.seth(25)
flor.down()
flor.circle(r, 70)
flor.seth(205)
flor.circle(r, 70)
flor.end_fill()

flor.up()
flor.left(320)
flor.forward(400)
flor.down()
flor.width(4)
flor.color('#000000', '#DFFED5')   #Cor da caneta e preenchimento
flor.begin_fill()
flor.up()
flor.seth(45)
flor.down()
flor.circle(r, 70)
flor.seth(225)
flor.circle(r, 70)
flor.end_fill()

flor.up()
flor.left(90)
flor.forward(550)
flor.down()
flor.width(4)
flor.color('#000000', '#FEE5FF')   #Cor da caneta e preenchimento
flor.begin_fill()
flor.up()
flor.seth(55)
flor.down()
flor.circle(r, 70)
flor.seth(235)
flor.circle(r, 70)
flor.end_fill()

flor.up()
flor.left(320)
flor.forward(200)
flor.down()
flor.width(4)
flor.color('#000000', '#FFE2B0')   #Cor da caneta e preenchimento
flor.begin_fill()
flor.up()
flor.seth(25)
flor.down()
flor.circle(r, 70)
flor.seth(205)
flor.circle(r, 70)
flor.end_fill()

flor.up()
flor.left(155)
flor.forward(700)
flor.down()
flor.width(4)
flor.color('#000000', '#FFE2B0')   #Cor da caneta e preenchimento
flor.begin_fill()
flor.up()
flor.seth(25)
flor.down()
flor.circle(r, 70)
flor.seth(205)
flor.circle(r, 70)
flor.end_fill()

turtle.done()


