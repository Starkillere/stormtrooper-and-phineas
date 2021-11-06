#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Mon dessin, est un dessin de stormtrooper, suivie d'un très beau garçons d'arithmetique modulaire.
   (Un stromtrooper avec un phineas qui a comme particularité d'avoir comme bas la table de 464
   modulo 691 en arithmetique modulaire (la chance qu'il a))
   
   langage:
   --------
   pytohn3
   
   Module utiliser:
   ---------------
   Turtle

   Création:
   ---------
   Fait par: Starkiller (Ayouba Anrezki)
   Initiation: 11/10/2021 à 14h07
   Aide: GéoGebra classique5, documentation officiel du module turtle
   Mise à jour: 11/10/2021 à 18h52
   Disponible sur: mon github(https://github.com/Starkillere)

   Test:
   -----
   >>>arithmetique_modulaire(6)

   >>>stormetrooper()

   >>>boy_modulaire()
   
'''

from turtle import *


#Fonction qui fait de l'arithmetique modulaire (de jolie cercle)
def arithmétique_modulaire(n,r=50,m=100, colore1='#03a309', colore2='#080101'):
    width(1)
    color(colore1, colore2)
    begin_fill()
    rayon=r
    modulo=m
    table=n
    pos = {} 
    penup()
    pendown()
    for i in range(modulo):
    	circle(rayon,360/modulo)
    	pos[i]=position()
    penup()
    for i in range (modulo):
        penup()
        j=i*table
        goto(pos[i])
        pendown()
        goto(pos[j%modulo]) 
    end_fill()
    width(0)
    color('#03f4fc')

#Fonction qui réalise le stormtrooper
def stormetrooper():
    #casque 

    #données
    color('white', '#a8a7a5')
    width(3)

    #dessin
    begin_fill()
    goto(3.37715, 5.99096)
    goto(2.0223, 26.50725)
    goto(-6.68745, 28.6363)
    goto(-8.07462, 50.41456)
    goto(-4.80178, 53.21739)
    goto(-5.06731, 113.35924)
    goto(-3.60327, 120.50145)
    goto(-1.23596, 126.51079)
    goto(0.76715, 131.60962)
    goto(2.95237, 138.71157)
    goto(5.86599, 145.26721)
    goto(10.23641, 152.36916)
    goto(14.60684, 157.65009)
    goto(18.97727, 163.47733)
    goto(22.80139, 167.48355)
    goto(27.17182, 172.21818)
    goto(31.72435, 175.67811)
    goto(35.18427, 179.13803)
    goto(42.3716, 186.00457)
    goto(48.19, 188.91377)
    goto(53.94311, 192.69703)
    goto(59.4501, 196.06241)
    goto(66.18086, 199.12184)
    goto(75.66512, 204.62883)
    goto(116.19977, 219.11675)
    goto(149.07349, 225.20448)
    goto(235.92505, 227.63957)
    goto(300, 200)
    goto(349.85636, -34.47375)
    goto(360.72477, -45.94596)
    goto(346.83736, -74.32458)
    goto(310.29047, -86.96705)
    goto(276.54608, -103.01621)
    goto(235.46726, -130.70004)
    goto(242.68498, -138.51924)
    goto(173.87655, -153.4046)
    goto(104.64759, -203.21947)
    goto(64.5713, -199.88457)
    goto(50, -200)
    goto(-11.81685, -124.16649)
    goto(0.24444, -115.45556)
    goto(-1.09571, -85.97242)
    goto(1.58458, -56.48927)
    goto(0,0)
    end_fill()

    #détaille
    
    #nez

    #données
    color('white', '#424140')
    width(3)

    #dessin
    begin_fill()
    goto(86.01359, -35.71705)
    goto(89.36395, -50.45863)
    goto(79.31288, -95.35342)
    goto(1.58458, -56.48927)
    end_fill()

    #contoure des yeux 

    #données
    color('white', '#a8a7a5')
    width(5)

    #dessin
    begin_fill()
    goto(0,0)
    goto(86.01359, -35.71705)
    goto(79.98295, -10.25434)
    goto(96.06466, -10.92441)
    goto(114.82666, 58.76303)
    goto(2.0223, 26.50725)
    end_fill()

    #yeux

    #données
    color('white', '#000a09')
    width(5)

    #dessin
    begin_fill()
    goto(114.82666, 58.76303)
    goto(96.06466, -10.92441)
    goto(2.0223, 26.50725)
    goto(-6.68745, 28.6363)
    goto(-8.07462, 50.41456)
    goto(-4.80178, 53.21739)
    end_fill()

    #données
    color('white', '#000000')
    width(5)

    #dessin
    begin_fill()
    goto(189.97958, 93.15845)
    goto(200.12603, 79.43091)
    goto(2.0223, 26.50725)
    end_fill()
    
    #Bouche

    #données
    color('white', '#000000')
    width(5)
    
    #dessin
    goto(0.24444, -115.45556)
    begin_fill()
    goto(-11.81685, -124.16649)
    goto(50, -200)
    goto(104.64759, -203.21947)
    goto(0.24444, -115.45556)
    end_fill()

    #BOUCHE

    #données
    color('#424140', 'black')
    width(1)

    #dessin
    begin_fill()
    goto(1.58458, -56.48927)
    goto(79.31288, -95.35342)
    goto(-1.09571, -85.9724)
    goto(1.58458, -56.48927)
    end_fill()
    goto(1.58458, -56.48927)
    goto(12.27398, -85.44304)
    goto(20, -60)
    goto(25.04799, -86.42566)
    goto(34.38285, -66.77333)
    goto(41.26116, -91.33874)
    goto(53.05256, -79.54734)
    goto(56.00041, -96.74313)

    #new data
    color('white')
    width(3)

    #new dessin
    goto(79.31288, -95.35342)
    goto(1.58458, -56.48927)
    goto(-1.09571, -85.97242)
    goto(79.31288, -95.35342)

    #gp21

    #donées
    color('#424140', '#424140')
    width(3)

    #dessin
    begin_fill()
    goto(-1.09571, -85.97242)
    goto(110.65376, -107.16002)
    goto(141.23095, -115.02944)
    goto(173.87655, -153.4046)
    goto(104.64759, -203.21947)
    goto(104.64759, -203.21947)
    goto(0.24444, -115.45556)
    goto(-1.09571, -85.97242)
    end_fill()

    #gp22

    #données
    color('white', '#424140')
    width(3)

    #dessin
    begin_fill()
    goto(110.65376, -107.16002)
    goto(152.22773, -58.40042)
    goto(184.56304, -36.84355)
    goto(217.92487, -24.52533)
    goto(343.35649, 11.22127)
    goto(360.72477, -45.94596)
    goto(346.83736, -74.32458)
    goto(310.29047, -86.96705)
    goto(276.54608, -103.01621)
    goto(235.46726, -130.70004)
    goto(242.68498, -138.51924)
    goto(173.87655, -153.4046)
    goto(141.23095, -115.02944)
    goto(110.65376, -107.16002)
    end_fill()

    #tgpd

    #données:
    color('white', 'black')
    width(3)
    
    #dessin 
    begin_fill()
    goto(131.38581, -85.58912)
    goto(143.32678, -102.1926)
    goto(221.44868, -46.59283)
    goto(208.14042, -28.02317)
    goto(152.22773, -58.40042)
    goto(131.38581, -85.58912)
    end_fill()

    #tgpd1

    #données
    color('#424140')
    width(2)

    #dessin
    goto(143.76559, -81.87519)
    goto(149.33649, -92.70749)
    goto(149.95548, -73.82834)
    goto(156.76435, -85.27963)
    goto(158.31183, -65.78148)
    goto(163.57323, -78.47075)
    goto(166.97767, -58.35362)
    goto(173.16756, -68.87643)
    goto(176.57199, -51.54474)
    goto(182.45239, -63.92452)
    goto(188.33278, -44.73586)
    goto(190.49924, -57.11564)
    goto(200, -40)
    goto(199.78407, -52.16373)
    goto(208.75941, -35.45103)
    goto(201.33155, -30.80862)
    goto(209.68789, -48.75929)

    #RADIOPHANE

    #données
    color('white', 'black')
    width(3)

    #dessin
    penup()
    goto(235.46726, -130.70004)
    pendown()
    begin_fill()
    goto(244.62997, -91.28297)
    goto(240.04832, -47.43002)
    goto(206.66771, -10.7768)
    goto(240, 0)
    goto(281.07998, -50.88103)
    goto(292.93279, -94.48243)
    goto(235.46726, -130.70004)
    end_fill()
    
    penup()
    goto(206.66771, -10.7768)
    pendown()
    arithmétique_modulaire(6,40,100,'#212121','black')
     
    #dpd

    #données
    color('white', '#212121')
    width(3)

    #dessin
    penup()
    goto(131.67688, 21.15806)
    pendown()
    begin_fill()
    goto(160.58841, -14.17825)
    goto(121.50431, -65.04114)
    goto(94.19897, -31.31101)
    goto(131.67688, 21.15806)
    end_fill()
    penup()
    goto(133.28308, 7.23769)
    pendown()

    #new données
    color('#212121', 'black')
    width(2)

    #dessin
    begin_fill()
    goto(133.28308, 7.23769)
    goto(160.58841, -14.17825)
    goto(125.2521, -52.72696)
    goto(105.44234, -29.16942)
    goto(133.28308, 7.23769)
    end_fill()

    #bpd1

    #données
    color('#424140')

    #dessin
    penup()
    goto(128.99989, -1.86408)
    pendown()
    goto(152.02203, -23.28003)
    penup()
    goto(125.32711, -8.03107)
    pendown()
    goto(145.46531, -29.06716)
    penup()
    goto(120.96597, -14.31624)
    pendown()
    goto(140.07802, -35.09579)
    penup()
    goto(116.7331, -20.85795)
    pendown()
    goto(134.819, -38.55905)
    penup()
    goto(111.47407, -25.21909)
    pendown()
    goto(129.81652, -42.15058)

#Fonction qui fais le beau garçons arithmetique modulaire
def boy_modulaire():
    #Forme tête
    
    #données 
    color('#9c3a06', '#f0c4ad')
    width(3)

    #dessin
    begin_fill()
    goto(-248.74009, 161.66906)
    goto(-296.74611, 78.23003)
    goto(-321.89212, 13.07901)
    goto(-332.17912, -41.78501)
    goto(-351.61013, -50.92902)
    goto(-384.75714, -12.067)
    goto(-337.89412, 29.08101)
    goto(-342.46612, 81.65903)
    goto(-413.33215, 27.93801)
    goto(-555.0642, 102.23304)
    end_fill()

    #yeux

    #données
    color('black','white')
    width(3)

    #dessin
    penup()
    goto(-353.89613, 105.66204)
    pendown()
    begin_fill()
    circle(40)
    end_fill()

    #new données
    color('black', 'blue')

    #new dessin
    penup()
    goto(-344.10916, 121.27195)
    pendown()
    begin_fill()
    circle(10)
    end_fill()

    #cheveux

    #données
    color('#b35305', '#b35305')
    width(3)

    #dessin
    penup()
    goto(-260, 160)
    pendown()
    begin_fill()
    goto(-300, 200)
    goto(-253.54607, 185.80067)
    goto(-305.96441, 238.21901)
    goto(-239.75177, 188.55953)
    goto(-238.83215, 226.26395)
    goto(-223.19861, 160.0513)
    goto(-195.61001, 130.62346)
    goto(-219.52013, 138.90004)
    goto(-227.79671, 110.39182)
    goto(-235.15367, 131.54308)
    goto(-242.51063, 107.63296)
    goto(-248.94797, 139.81966)
    goto(-260, 160)
    end_fill()

    #oreille

    #données
    color('#9c3a06', '#f0c4ad')
    width(1)
    penup()
    goto(-303.94821, 76.88771)
    pendown()
    begin_fill()
    goto(-288.62746, 76.24935)
    goto(-281.28626, 63.80123)
    goto(-284.79727, 54.22576)
    goto(-293.73437, 49.43802)
    goto(-303.94821, 49.7572)
    goto(-310.33186, 54.54494)
    end_fill()

    #bouche

    #dents

    #données
    color('#a86932', '#f5f5f5')
    width(1)
    #dessin
    penup()
    goto(-342.46612, 81.65903)
    pendown()
    begin_fill()
    goto(-398.44308, 35.11104)
    goto(-386.38469, 27.75571)
    goto(-337.71453, 67.00585)
    goto(-342.46612, 81.65903)
    end_fill()
    penup()
    goto(-380.628, 3.15896)
    pendown()
    begin_fill()
    goto(-376.44132, -7.30774)
    goto(-352.52449, 9.43467)
    goto(-357.14352, 11.47248)
    goto(-380.628, 3.15896)
    end_fill()

    #LANGUE

    #données
    color('#000000','#f25265')
    width(1)

    #dessin
    penup()
    goto(-337.89412, 29.08101)
    pendown()
    begin_fill()
    goto(-352.38863, 25.87298)
    goto(-357.14352, 11.47248)
    goto(-352.52449, 9.43467)
    goto(-337.89412, 29.08101)
    end_fill()

    #font

    #données
    color('#520000', '#520000')
    width(1)

    #dessin
    penup()
    goto(-376.0272, 35.2469)
    pendown()
    begin_fill()
    goto(-367.06085, 21.93322)
    goto(-363.52865, 10.38565)
    goto(-336.22203, 34.02421)
    goto(-337.71453, 67.00585)
    goto(-376.0272, 35.2469)
    end_fill()

    #bas

    #données
    width(2)

    #dessin
    penup()
    goto(-352.64913, -336.95098)
    pendown()
    arithmétique_modulaire(464,150,691, '#424242','#f78745')

#main
if __name__ == '__main__':
    #Données:
    bgcolor('black')
    speed('fastest')
    title('Troupe le trouper et bébé_phinéas le droide')
    stormetrooper()
    penup()
    goto(-555.0642, 102.23304)
    pendown()
    boy_modulaire()
    #titre
    color('white')
    penup()
    goto(-298.32605, 350.16476)
    pendown()
    write("Troupe la stormtrooper et son ami bébé-phinéas le droïde.", font=("Verdana"))
    ht()
    done()