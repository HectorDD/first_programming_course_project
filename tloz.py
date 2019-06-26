# -*- coding: cp1252 -*-
import pygame
import sys, pygame
def main():
    pygame.init()
    screen = pygame.display.set_mode((980, 700),pygame.FULLSCREEN)
    pygame.display.set_caption("TLOZ - CUSTOM ")
    nivel=1
    background_image = pygame.image.load('bg.png')
    arbolcut = pygame.image.load('arbol70.png')
    arbolfijo = pygame.image.load('arbol3.png')
    a14 = pygame.image.load("14a.png")
    h5 = pygame.image.load("5h.png")
    h4 = pygame.image.load("4h.png")
    a3 = pygame.image.load("3a.png")
    a13=pygame.image.load("13a.png")
    a2  = pygame.image.load("2a.png")
    a4= pygame.image.load("4a.png")
    a9=pygame.image.load("9a.png")
    h2 = pygame.image.load("2h.png")
    n1=pygame.image.load("N1.png")
    n2=pygame.image.load("N2.png")
    n3=pygame.image.load("N3.png")
    vida1 = pygame.image.load("vida1.png")
    vida2 = pygame.image.load("vida2.png")
    vida3 = pygame.image.load("vida3.png")
    vida4 = pygame.image.load("vida4.png")
    vida5 = pygame.image.load("vida5.png")
    malo = pygame.image.load("malo.png")
    reloj=pygame.image.load("clock.png")
    indicador=pygame.image.load("indicador.png")
    transpa=pygame.image.load("transpa.png")
    restati=0
    contesp=0
    go=pygame.image.load("go.png")
    win=pygame.image.load("win.png")


    linkd = pygame.image.load('linkabajo.png')
    linkda=pygame.image.load('linkabajoa.png')
    linku = pygame.image.load('linkarriba.png')
    linkua = pygame.image.load('linkarribaa.png')
    linkr = pygame.image.load('linkder.png')
    linkra = pygame.image.load('linkdera.png')
    linkl = pygame.image.load('linkiz.png')
    linkla = pygame.image.load('linkiza.png')

    corazon = pygame.image.load('energia.png')
    corac=pygame.image.load('corac.png')

    bomba = pygame.image.load('bomba.png')
    exp=pygame.image.load("exp.png")
    salida = pygame.image.load('salida.png')
    zelda = pygame.image.load('zelda70.png')
    barra = pygame.image.load('barra.png')
    actlink = linkr
    lucha=False
    rescate=False
    ##posiciones en el nivel 1
    linkx=10
    linky=550
    linkix=10
    linkiy=550

    link2x,link2y=10,550
    linki2x,linki2y=10,550

    link3x,link3y=10,550

    # coordenadas de los corazones para las colisiones nivel 1
    c1x,c1y=280,210
    c2x,c2y=490,560
    b1x,b1y=770,210
    c1=True
    c2=True
    b1=True
    cpx=1000
    cpy=1000
    m1x,m1y=910,350
    m2x,m2y=70,420
    m3x,m3y=210,210
    mab3=True
    miz1=True
    mar2=True

    c3x,c3y=0,210
    c3=True


    cm1x,cm1y=910,420
    z1x,z1y=910,210
    z3x,z3y=0,210


    #####-------------coordenadas y booleanos nivel 3
    c01x,c01y=280,210
    
    
    
    b01x,b01y=490,350
    b02x,b02y=140,350
    c01=True
    c02=True
    
    b01=True
    b02=True
    cpx=1000
    cpy=1000
    
    m01x,m01y=280,350
    m02x,m02y=560,420
    m03x,m03y=770,560
    m04x,m04y=910,560
    
    miz01=True
    miz02=True
    miz03=True
    miz04=True

    cm01x,cm01y=280,420
    cm02x,cm02y=560,490
    cm03x,cm03y=770,630
    cm04x,cm04y=910,630
    
    z01x,z01y=0,210

    #coordenadas de los arboles que se pueden cortar nivel 1
    ac1x,ac1y=70,210
    ac1=True
    ac2x,ac2y=210,560
    ac2=True
    ac3x,ac3y=420,560
    ac3=True
    ac4x,ac4y=490,350
    ac4=True
    ac5x,ac5y=840,560
    ac5=True
    ac6x,ac6y=840,210
    ac6=True
    ac7x,ac7y=910,280
    ac7=True
    #lvl2
    ac8x,ac8y=70,560
    ac9x,ac9y=0,280
    ac100x,ac100y=630,490

    ac01x,ac01y=70,210
    ac01=True
    ac02x,ac02y=210,210
    ac2=True
    ac03x,ac03y=420,210
    ac03=True
    ac04x,ac04y=560,210
    ac04=True
    ac05x,ac05y=910,210
    ac05=True
    ac06x,ac06y=910,280
    ac06=True
    ac07x,ac07y=840,350
    ac07=True
    
    ac09x,ac09y=70,350
    ac09=True
    ac010x,ac010y=0,420
    ac010=True
    ac011x,ac011y=70,420
    ac011=True
    ac012x,ac012y=70,560
    ac012=True

     # coordenadas de los arboles para las colisiones nivel 3

    a01x,a01y=0,630#abajo
    a02x,a02y=0,140#arriba
    
    a03x,a03y=0,280#3
    
    
    a010x,a010y=840,420#4h
    
    a011x,a011y=0,490#2
    a012x,a012y=140,490#2

    a013x,a013y=490,420#2h

    a014x,a014y=630,490#3
    
    a015x,a015y=350,560#2h




    # coordenadas de los arboles para las colisiones nivel 1
    a1x,a1y=0,630
    a2x,a2y=0,140
    a3x,a3y=70,280
    a4x,a4y=210,210
    a5x,a5y=280,350
    a6x,a6y=560,350
    a7x,a7y=420,490
    a8x,a8y=700,490
    a9x,a9y=840,210
    a10x,a10y=-70,490
    a11x,a11y=140,490
    a12x,a12y=140,280

    a100x,a100y=0,490
    a101x,a101y=700,490
    a102x,a102y=0,420
    a103x,a103y=700,420

    nvx,nvy=350,40
    pn1x,pn1y=910,560
    pn3x,pn3y=910,560

    pn2x,pn2y=0,350


    
    #se define cantidad de vidas y energía 
    vidas=3
    energia=5
    

    

    reloj1 = pygame.time.Clock() #tiempo(no estoy segura de que hace, pero si se lo quito falla)
    
    #musica 
    musica = pygame.mixer.music.load('Spectrum.mp3')
    fuente = pygame.font.SysFont("Arial", 28, True, False)
    info = fuente.render("Tiempo ", 0 ,(255,255,255))
    empezar = True


    limi_ancho_derecha=930
    limi_ancho_izquierda=10
    limi_altura_abajo=700
    limi_altura_arriba=40
    vx = 0
    vy = 0
    angulo = 0
    upapretada,downapretada,leftapretada,rightapretada = False,False,False,False
    while empezar:
        salir=False
        while salir != True:
            for event in pygame.event.get():
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        
                        pygame.exit()

                    if event.key == pygame.K_q:
                        lucha=True

                    if event.key==pygame.K_RIGHT and not event.key == pygame.K_UP and not event.key==pygame.K_DOWN and not event.key==pygame.K_LEFT:
                        vx=15
                        vy=0 
                        if lucha: 
                            actlink= linkra   
                        else:        
                            actlink=linkr
                    elif event.key==pygame.K_LEFT  and not event.key==pygame.K_UP and not event.key==pygame.K_DOWN and not event.key==pygame.K_RIGHT:
                        vx=-15
                        vy=0 
                        if lucha: 
                            actlink= linkla   
                        else:        
                            actlink=linkl                
                        
                    elif event.key==pygame.K_UP   and not event.key==pygame.K_RIGHT and not event.key==pygame.K_DOWN and not event.key==pygame.K_LEFT:
                        vx=0
                        vy=-15               
                        if lucha: 
                            actlink= linkua  
                        else:        
                            actlink=linku
                    elif event.key==pygame.K_DOWN   and not event.key==pygame.K_UP and not event.key==pygame.K_RIGHT and not event.key==pygame.K_LEFT:
                        vx=0
                        vy=15    
                        if lucha: 
                            actlink= linkda   
                        else:        
                            actlink=linkd                
                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        
                        pygame.exit()
                    if event.key==pygame.K_RIGHT and not event.key == pygame.K_UP and not event.key==pygame.K_DOWN and not event.key==pygame.K_LEFT:
                        vx=0
                        vy=0             
                    elif event.key==pygame.K_LEFT  and not event.key==pygame.K_UP and not event.key==pygame.K_DOWN and not event.key==pygame.K_RIGHT:
                        vx=0
                        vy=0                  
                    elif event.key==pygame.K_UP   and not event.key==pygame.K_RIGHT and not event.key==pygame.K_DOWN and not event.key==pygame.K_LEFT:
                        vx=0
                        vy=0                
                    elif event.key==pygame.K_DOWN   and not event.key==pygame.K_UP and not event.key==pygame.K_RIGHT and not event.key==pygame.K_LEFT:
                        vx=0
                        vy=0
                    if event.key == pygame.K_q:
                        lucha=False

            ##aqu� comienza el nivel 2--------------------------------------------------------------------
            if nivel==2:            
                Slink=pygame.sprite.Sprite()
                Slink.image=actlink
                Slink.rect=actlink.get_rect()
                Slink.rect.top,Slink.rect.left=linky,linkx #posicion en y,x



                #definir los corazones, bombas y la princesa como sprites
                if c1:
                    cora1 = pygame.sprite.Sprite()
                    cora1.image = corazon
                    cora1.rect=corazon.get_rect()
                    cora1.rect.top,cora1.rect.left=c1y,c1x
                    screen.blit(cora1.image,cora1.rect)
                if c2:
                    cora2 = pygame.sprite.Sprite()
                    cora2.image = corazon
                    cora2.rect=corazon.get_rect()
                    cora2.rect.top,cora2.rect.left=c2y,c2x
                    screen.blit(cora2.image,cora2.rect)
                if b1:
                    bomba1 = pygame.sprite.Sprite()
                    bomba1.image = bomba
                    bomba1.rect=bomba.get_rect()
                    bomba1.rect.top,bomba1.rect.left=b1y,b1x
                    screen.blit(bomba1.image,bomba1.rect)
                if m1x <= 630:
                    miz1=False
                elif m1x >= 910:
                    miz1=True
                if miz1:
                    m1x=m1x-6             
                elif miz1==False:
                    m1x=m1x+6  

                pn1 = pygame.sprite.Sprite()
                pn1.image = salida
                pn1.rect=salida.get_rect()
                pn1.rect.top,pn1.rect.left=pn1y,pn1x
                screen.blit(pn1.image,pn1.rect)        


                m1 = pygame.sprite.Sprite()
                m1.image = malo
                m1.rect=malo.get_rect()
                m1.rect.top,m1.rect.left=m1y,m1x
                screen.blit(m1.image,m1.rect)

                zelda1 = pygame.sprite.Sprite()
                zelda1.image = zeld
                zelda1.rect=zelda.get_rect()
                zelda1.rect.top,zelda1.rect.left=z1y,z1x
                screen.blit(zelda1.image,zelda1.rect)

                #arboles para cortar
                ac1 = pygame.sprite.Sprite()
                ac1.image = arbolcut
                ac1.rect=arbolcut.get_rect()
                ac1.rect.top,ac1.rect.left=ac1y,ac1x
                screen.blit(ac1.image,ac1.rect)

                ac2 = pygame.sprite.Sprite()
                ac2.image = arbolcut
                ac2.rect=arbolcut.get_rect()
                ac2.rect.top,ac2.rect.left=ac2y,ac2x
                screen.blit(ac2.image,ac2.rect)

                ac3 = pygame.sprite.Sprite()
                ac3.image = arbolcut
                ac3.rect=arbolcut.get_rect()
                ac3.rect.top,ac3.rect.left=ac3y,ac3x
                screen.blit(ac3.image,ac3.rect)

                ac4 = pygame.sprite.Sprite()
                ac4.image = arbolcut
                ac4.rect=arbolcut.get_rect()
                ac4.rect.top,ac4.rect.left=ac4y,ac4x
                screen.blit(ac4.image,ac4.rect)

                ac5 = pygame.sprite.Sprite()
                ac5.image = arbolcut
                ac5.rect=arbolcut.get_rect()
                ac5.rect.top,ac5.rect.left=ac5y,ac5x
                screen.blit(ac5.image,ac5.rect)

                ac7 = pygame.sprite.Sprite()
                ac7.image = arbolcut
                ac7.rect=arbolcut.get_rect()
                ac7.rect.top,ac7.rect.left=ac7y,ac7x
                screen.blit(ac7.image,ac7.rect)


                ## definir arboles como sprites
                arbol1 = pygame.sprite.Sprite()
                arbol1.image = a14
                arbol1.rect=a14.get_rect()
                arbol1.rect.top,arbol1.rect.left=a1y,a1x
                #screen.blit(arbol1.image,arbol1.rect)

                arbol2 = pygame.sprite.Sprite()
                arbol2.image = a14
                arbol2.rect=a14.get_rect()
                arbol2.rect.top,arbol2.rect.left=a2y,a2x
                screen.blit(arbol2.image,arbol2.rect)

                arbol3 = pygame.sprite.Sprite()
                arbol3.image = h5
                arbol3.rect=h5.get_rect()
                arbol3.rect.top,arbol3.rect.left=a3y,a3x
                screen.blit(arbol3.image,arbol3.rect)

                arbol4 = pygame.sprite.Sprite()
                arbol4.image = h5
                arbol4.rect=h5.get_rect()
                arbol4.rect.top,arbol4.rect.left=a4y,a4x
                screen.blit(arbol4.image,arbol4.rect)

                arbol5 = pygame.sprite.Sprite()
                arbol5.image = a3
                arbol5.rect=a3.get_rect()
                arbol5.rect.top,arbol5.rect.left=a5y,a5x
                screen.blit(arbol5.image,arbol5.rect)

                arbol6 = pygame.sprite.Sprite()
                arbol6.image = h4
                arbol6.rect=h4.get_rect()
                arbol6.rect.top,arbol6.rect.left=a6y,a6x
                screen.blit(arbol6.image,arbol6.rect)

                arbol7 = pygame.sprite.Sprite()
                arbol7.image = a2
                arbol7.rect=a2.get_rect()
                arbol7.rect.top,arbol7.rect.left=a7y,a7x
                screen.blit(arbol7.image,arbol7.rect)

                arbol8 = pygame.sprite.Sprite()
                arbol8.image = a4
                arbol8.rect=a4.get_rect()
                arbol8.rect.top,arbol8.rect.left=a8y,a8x
                screen.blit(arbol8.image,arbol8.rect)

                arbol9 = pygame.sprite.Sprite()
                arbol9.image = h2
                arbol9.rect=h2.get_rect()
                arbol9.rect.top,arbol9.rect.left=a9y,a9x
                screen.blit(arbol9.image,arbol9.rect)


                
                xant = linkx
                yant = linky        
                linkx +=vx
                linky +=vy



                if linkx<=limi_ancho_izquierda:#if se llega a ir mas del limite
                    linkx=limi_ancho_izquierda
                
                elif linkx>=limi_ancho_derecha:#if se llega a ir mas del limite
                    linkx=limi_ancho_derecha
                
                elif linky<=limi_altura_arriba:#if se llega a ir mas del limite
                    linky=limi_altura_arriba
                
                elif linky>=limi_altura_abajo:
                    linky=limi_altura_abajo

                #colisiones con corazones,princesa y da�os

                if Slink.rect.colliderect(zelda1.rect):
                    zelda1.rect.top,zelda1.rect.left=cpy,cpx                
                    rescate=True

                if Slink.rect.colliderect(cora1.rect):
                    cora1.rect.top,cora1.rect.left=cpy,cpx
                    if energia < 5:
                        energia = energia + 1
                    elif energia == 5 and vidas < 5:
                        vidas=vidas+1
                    c1=False
                if Slink.rect.colliderect(cora2.rect):
                    cora2.rect.top,cora2.rect.left=cpy,cpx
                    if energia < 5 :
                        energia = energia + 1
                    elif energia == 5 and vidas < 5:
                        vidas=vidas+1
                    c2=False
                if Slink.rect.colliderect(bomba1.rect):
                    bomba1.rect.top,bomba1.rect.left=cpy,cpx
                    if energia > 2 :
                        energia = energia - 3  
                    elif energia <= 2:
                        energia=energia-energia
                    b1=False
                if Slink.rect.colliderect(m1.rect):
                    if linky < 380:
                        linkx=770
                        linky=280
                    elif linky > 379:
                        linky = cm1y                    
                    if energia > 0 :
                        energia = energia - 1 
                ### Arboles para cortar!!!------------------------------

                if Slink.rect.colliderect(ac1.rect):
                    if lucha:
                        ac1x,ac1y= 1000,1000
                    else:
                        (linkx,linky) = (xant-5,yant)
                if Slink.rect.colliderect(ac2.rect):
                    if lucha:
                        ac2x,ac2y= 1000,1000
                    else:
                        (linkx,linky) = (xant-5,yant)
                if Slink.rect.colliderect(ac3.rect):
                    if lucha:
                        ac3x,ac3y= 1000,1000
                    else:
                        (linkx,linky) = (xant-5,yant)
                if Slink.rect.colliderect(ac4.rect):
                    if lucha:
                        ac4x,ac4y= 1000,1000
                    else:
                        (linkx,linky) = (xant,yant+5)
                if Slink.rect.colliderect(ac5.rect):
                    if lucha:
                        ac5x,ac5y= 1000,1000
                    else:
                        (linkx,linky) = (xant-5,yant)
                
                if Slink.rect.colliderect(ac7.rect):
                    if lucha:
                        ac7x,ac7y= 1000,1000
                    else:
                        (linkx,linky) = (xant,yant+5)

                if Slink.rect.colliderect(pn1.rect):
                    if rescate:
                        nivel=3
                        restati = restati+((pygame.time.get_ticks()/1000)-restati)
                        rescate=False

                
                
                if Slink.rect.colliderect(arbol1.rect):
                    (linkx,linky) = (xant,yant-5)
                if Slink.rect.colliderect(arbol2.rect):
                    (linkx,linky) = (xant,yant+5)

                if Slink.rect.colliderect(arbol3.rect) and linkx<87 and linky>280:
                    (linkx,linky) = (xant-5,yant)
                elif Slink.rect.colliderect(arbol3.rect) and linkx>100 and linky>280:
                    (linkx,linky) = (xant+5,yant)
                elif Slink.rect.colliderect(arbol3.rect) and linky<280 :
                    (linkx,linky) = (xant,yant-5)

                if Slink.rect.colliderect(arbol4.rect) and linkx<227 and linky<490:
                    (linkx,linky) = (xant-5,yant)
                elif Slink.rect.colliderect(arbol4.rect) and linkx>240 and linky<490:
                    (linkx,linky) = (xant+5,yant)
                elif Slink.rect.colliderect(arbol4.rect) and linky>490 :
                    (linkx,linky) = (xant,yant+5)

                if Slink.rect.colliderect(arbol5.rect) and linkx<480 and linky<367:
                    (linkx,linky) = (xant,yant-5)
                elif Slink.rect.colliderect(arbol5.rect) and linkx<480 and linky>380:
                    (linkx,linky) = (xant,yant+5)
                elif Slink.rect.colliderect(arbol5.rect) and linkx>480 :
                    (linkx,linky) = (xant+5,yant)

                if Slink.rect.colliderect(arbol6.rect) and linkx<577 and linky>367:
                    (linkx,linky) = (xant-5,yant)
                elif Slink.rect.colliderect(arbol6.rect) and linkx>590 and linky>367:
                    (linkx,linky) = (xant+5,yant)
                elif Slink.rect.colliderect(arbol6.rect) and linky<366 :
                    (linkx,linky) = (xant,yant-5)

                if Slink.rect.colliderect(arbol7.rect) and linkx>400 and linky<490:
                    (linkx,linky) = (xant,yant-5)
                elif Slink.rect.colliderect(arbol7.rect) and linkx>400 and linky>510:
                    (linkx,linky) = (xant,yant+5)
                elif Slink.rect.colliderect(arbol7.rect) and linkx<420 :
                    (linkx,linky) = (xant-5,yant)

                if Slink.rect.colliderect(arbol8.rect) and linkx>680 and linky<490:
                    (linkx,linky) = (xant,yant-5)
                elif Slink.rect.colliderect(arbol8.rect) and linkx>680 and linky>510:
                    (linkx,linky) = (xant,yant+5)
                elif Slink.rect.colliderect(arbol8.rect) and linkx<700 :
                    (linkx,linky) = (xant-5,yant)

                if Slink.rect.colliderect(arbol9.rect) and linkx<866 and linky<325:
                    (linkx,linky) = (xant-5,yant)
                elif Slink.rect.colliderect(arbol9.rect) and linkx>865 and linky<325:
                    (linkx,linky) = (xant+5,yant)
                elif Slink.rect.colliderect(arbol9.rect) and linky>324 :
                    (linkx,linky) = (xant,yant+5)

                



                screen.blit(background_image,(0,0))
                if c1:
                    screen.blit(corazon,(c1x,c1y))
                else:
                    screen.blit(corac,(c1x,c1y))
                if c2:
                    screen.blit(corazon,(c2x,c2y))
                else:
                    screen.blit(corac,(c2x,c2y))   
                            
                screen.blit(salida,(pn1x,pn1y))

                if rescate:
                    screen.blit(transpa,(910,210))
                else:
                    screen.blit(zelda,(910,210))


                
                if b1:
                    screen.blit(bomba,(b1x,b1y))
                else:
                    screen.blit(exp,(b1x,b1y))


                
                screen.blit(barra,(-10,-5))

                #pintar la cantidad de vidas---
                if vidas==5:
                    screen.blit(vida5,(840,0))
                elif vidas==4:
                    screen.blit(vida4,(840,0))
                elif vidas==3:
                    screen.blit(vida3,(840,0))
                elif vidas==2:
                    screen.blit(vida2,(840,0))
                elif vidas==1:
                    screen.blit(vida1,(840,0))
                
                #se pinta la cantidad de energía y se verifica para disminuir la vida
                if energia==5:
                    screen.blit(corazon,(910,60))
                    screen.blit(corazon,(840,60))
                    screen.blit(corazon,(770,60))
                    screen.blit(corazon,(700,60))
                    screen.blit(corazon,(630,60))
                elif energia==4:
                    screen.blit(corazon,(910,60))
                    screen.blit(corazon,(840,60))
                    screen.blit(corazon,(770,60))
                    screen.blit(corazon,(700,60))
                elif energia==3:
                    screen.blit(corazon,(910,60))
                    screen.blit(corazon,(840,60))
                    screen.blit(corazon,(770,60))
                elif energia==2:
                    screen.blit(corazon,(910,60))
                    screen.blit(corazon,(840,60))
                elif energia==1:
                    screen.blit(corazon,(910,60))
                elif energia==0 and vidas>0:
                    vidas=vidas-1
                    energia=5
                    linkx,linky = linkix,linkiy
                    actlink = linkr
                

                if rescate:
                    screen.blit(zelda,(140,24))
                else:
                    screen.blit(indicador,(140,24))
                    
                
                reloj1.tick(29)
                
                screen.blit(arbolcut,(ac1x,ac1y))
                screen.blit(arbolcut,(ac2x,ac2y))                                
                screen.blit(arbolcut,(ac3x,ac3y))              
                
                screen.blit(arbolcut,(ac4x,ac4y))               
                
                screen.blit(arbolcut,(ac5x,ac5y))
                
                screen.blit(arbolcut,(ac7x,ac7y))
                

                screen.blit(a14,(a1x,a1y))
                screen.blit(a14,(a2x,a2y))
                screen.blit(h5,(a3x,a3y))
                screen.blit(h5,(a4x,a4y))
                screen.blit(a3,(a5x,a5y))
                screen.blit(h4,(a6x,a6y))
                screen.blit(a2,(a7x,a7y))
                screen.blit(a4,(a8x,a8y))
                screen.blit(h2,(a9x,a9y))


                screen.blit(n2,(nvx,nvy))


                screen.blit(malo,(m1x,m1y))
                
                screen.blit(Slink.image,Slink.rect)  
                if vidas==0:
                    screen.blit(go,(315, 315))
                    nivel=4      
                

                screen.blit(reloj, (0,0)) #Pone la palabra tiempo en la pantalla
                tiempo = (pygame.time.get_ticks()/1000)-restati  #Pasa el tiempo a segundos 
                tiempo = str(tiempo ) #No tengo la menor idea de que hace, pero si lo quito falla
                contador = fuente.render(tiempo ,0,(0,0,230))#Es el tiempo que se pone en la pantalla, pero con un formato y todo eso
                screen.blit(contador,(80, 23))#Pone el contador en la pantalla
                if float((pygame.time.get_ticks()/1000))%181==0:
                    contesp=0


                if float((pygame.time.get_ticks()/1000))%180==0 and contesp==0:

                    if vidas > 0:
                        contesp=1
                        vidas = vidas-1
                        energia=5
                        restati=restati+5

                        linkx,linky=linkix,linkiy
                    if vidas == 0:
                        screen.blit(go,(315, 315))

                        nivel=4

                pygame.display.update()
 ##########################################-------------------------------NIVEL3----------------------------#######################################
            elif nivel==3:
                Slink=pygame.sprite.Sprite()
                Slink.image=actlink
                Slink.rect=actlink.get_rect()
                Slink.rect.top,Slink.rect.left=link2y,link2x

                #####----Arboles normales---.
                if c01:
                    cora01 = pygame.sprite.Sprite()
                    cora01.image = corazon
                    cora01.rect=corazon.get_rect()
                    cora01.rect.top,cora01.rect.left=c01y,c01x
                    screen.blit(cora01.image,cora01.rect)
               

                
                    
                if b01:
                    bomba01 = pygame.sprite.Sprite()
                    bomba01.image = bomba
                    bomba01.rect=bomba.get_rect()
                    bomba01.rect.top,bomba01.rect.left=b01y,b01x
                    screen.blit(bomba01.image,bomba01.rect)

                if b02:
                    bomba02 = pygame.sprite.Sprite()
                    bomba02.image = bomba
                    bomba02.rect=bomba.get_rect()
                    bomba02.rect.top,bomba02.rect.left=b02y,b02x
                    screen.blit(bomba02.image,bomba02.rect)


                    
                


                m01 = pygame.sprite.Sprite()
                m01.image = malo
                m01.rect=malo.get_rect()
                m01.rect.top,m01.rect.left=m01y,m01x
                screen.blit(m01.image,m01.rect)

                m02 = pygame.sprite.Sprite()
                m02.image = malo
                m02.rect=malo.get_rect()
                m02.rect.top,m02.rect.left=m02y,m02x
                screen.blit(m02.image,m02.rect)

                

                zelda01 = pygame.sprite.Sprite()
                zelda01.image = zelda
                zelda01.rect=zelda.get_rect()
                zelda01.rect.top,zelda01.rect.left=z01y,z01x
                screen.blit(zelda01.image,zelda01.rect)

                if m01y >= 560:
                    miz01=False
                elif m01y <= 350:
                    miz01=True
                if miz01:
                    m01y=m01y+6             
                elif miz01==False:
                    m01y=m01y-6

                if m02x >= 770:
                    miz02=False
                elif m02x <= 560:
                    miz02=True
                if miz02:
                    m02x=m02x+6             
                elif miz02==False:
                    m02x=m02x-6

               

                
                #arboles para cortar
                    
                ac01 = pygame.sprite.Sprite()
                ac01.image = arbolcut
                ac01.rect=arbolcut.get_rect()
                ac01.rect.top,ac01.rect.left=ac01y,ac01x
                screen.blit(ac01.image,ac01.rect)

                ac02 = pygame.sprite.Sprite()
                ac02.image = arbolcut
                ac02.rect=arbolcut.get_rect()
                ac02.rect.top,ac02.rect.left=ac02y,ac02x
                screen.blit(ac02.image,ac02.rect)

                ac03 = pygame.sprite.Sprite()
                ac03.image = arbolcut
                ac03.rect=arbolcut.get_rect()
                ac03.rect.top,ac03.rect.left=ac03y,ac03x
                screen.blit(ac03.image,ac03.rect)

                ac04 = pygame.sprite.Sprite()
                ac04.image = arbolcut
                ac04.rect=arbolcut.get_rect()
                ac04.rect.top,ac04.rect.left=ac04y,ac04x
                screen.blit(ac04.image,ac04.rect)

                ac05 = pygame.sprite.Sprite()
                ac05.image = arbolcut
                ac05.rect=arbolcut.get_rect()
                ac05.rect.top,ac05.rect.left=ac05y,ac05x
                screen.blit(ac05.image,ac05.rect)

                ac06 = pygame.sprite.Sprite()
                ac06.image = arbolcut
                ac06.rect=arbolcut.get_rect()
                ac06.rect.top,ac06.rect.left=ac06y,ac06x
                screen.blit(ac06.image,ac06.rect)

                ac07 = pygame.sprite.Sprite()
                ac07.image = arbolcut
                ac07.rect=arbolcut.get_rect()
                ac07.rect.top,ac07.rect.left=ac07y,ac07x
                screen.blit(ac07.image,ac07.rect)

                ac09 = pygame.sprite.Sprite()
                ac09.image = arbolcut
                ac09.rect=arbolcut.get_rect()
                ac09.rect.top,ac09.rect.left=ac09y,ac09x
                screen.blit(ac09.image,ac09.rect)

                ac010 = pygame.sprite.Sprite()
                ac010.image = arbolcut
                ac010.rect=arbolcut.get_rect()
                ac010.rect.top,ac010.rect.left=ac010y,ac010x
                screen.blit(ac010.image,ac010.rect)

                ac011 = pygame.sprite.Sprite()
                ac011.image = arbolcut
                ac011.rect=arbolcut.get_rect()
                ac011.rect.top,ac011.rect.left=ac011y,ac011x
                screen.blit(ac011.image,ac011.rect)

                ac012 = pygame.sprite.Sprite()
                ac012.image = arbolcut
                ac012.rect=arbolcut.get_rect()
                ac012.rect.top,ac012.rect.left=ac012y,ac012x
                screen.blit(ac012.image,ac012.rect)



                ## definir arboles como sprites
                
                arbol01 = pygame.sprite.Sprite()
                arbol01.image = a14
                arbol01.rect=a14.get_rect()
                arbol01.rect.top,arbol01.rect.left=a01y,a01x
                screen.blit(arbol01.image,arbol01.rect)

                arbol02 = pygame.sprite.Sprite()
                arbol02.image = a14
                arbol02.rect=a14.get_rect()
                arbol02.rect.top,arbol02.rect.left=a02y,a02x
                screen.blit(arbol02.image,arbol02.rect)

                arbol03 = pygame.sprite.Sprite()
                arbol03.image = a13
                arbol03.rect=a13.get_rect()
                arbol03.rect.top,arbol03.rect.left=a03y,a03x
                screen.blit(arbol03.image,arbol03.rect)

                arbol010 = pygame.sprite.Sprite()
                arbol010.image = h4
                arbol010.rect=h4.get_rect()
                arbol010.rect.top,arbol010.rect.left=a010y,a010x
                screen.blit(arbol010.image,arbol010.rect)

                arbol011 = pygame.sprite.Sprite()
                arbol011.image = a2
                arbol011.rect=a2.get_rect()
                arbol011.rect.top,arbol011.rect.left=a011y,a011x
                screen.blit(arbol011.image,arbol011.rect)

                arbol012 = pygame.sprite.Sprite()
                arbol012.image = a2
                arbol012.rect=a2.get_rect()
                arbol012.rect.top,arbol012.rect.left=a012y,a012x
                screen.blit(arbol012.image,arbol012.rect)

                arbol013 = pygame.sprite.Sprite()
                arbol013.image = h2
                arbol013.rect=h2.get_rect()
                arbol013.rect.top,arbol013.rect.left=a013y,a013x
                screen.blit(arbol013.image,arbol013.rect)

                arbol014 = pygame.sprite.Sprite()
                arbol014.image = a3
                arbol014.rect=a3.get_rect()
                arbol014.rect.top,arbol014.rect.left=a014y,a014x
                screen.blit(arbol014.image,arbol014.rect)

                arbol015 = pygame.sprite.Sprite()
                arbol015.image = h2
                arbol015.rect=h2.get_rect()
                arbol015.rect.top,arbol015.rect.left=a015y,a015x
                screen.blit(arbol015.image,arbol015.rect)

                pn2 = pygame.sprite.Sprite()
                pn2.image = salida
                pn2.rect=salida.get_rect()
                pn2.rect.top,pn2.rect.left=pn2y,pn2x
                screen.blit(pn2.image,pn2.rect)


                ###-----------Corazones---------###

                

                xant = link2x
                yant = link2y        
                link2x +=vx
                link2y +=vy

                if link2x<=limi_ancho_izquierda:#if se llega a ir mas del limite
                    link2x=limi_ancho_izquierda
                
                elif link2x>=limi_ancho_derecha:#if se llega a ir mas del limite
                    link2x=limi_ancho_derecha
                
                elif link2y<=limi_altura_arriba:#if se llega a ir mas del limite
                    link2y=limi_altura_arriba
                
                elif link2y>=limi_altura_abajo:
                    link2y=limi_altura_abajo

                if Slink.rect.colliderect(m01.rect) :
                    if energia > 0:
                        energia = energia -1
                    
                if Slink.rect.colliderect(m02.rect) :
                    if energia > 0:
                        energia = energia -1

                if Slink.rect.colliderect(cora01.rect) :
                    cora01.rect.top,cora01.rect.left=cpy,cpx
                    c01=False
                    if energia < 5:
                        energia = energia +1
                    elif energia == 5 and vidas < 5:
                        vidas=vidas+1
                    
                    


                if Slink.rect.colliderect(bomba01.rect) and b01 :
                    b01=False
                    if energia > 2:
                        energia = energia -3
                    elif energia < 3 :
                        energia=energia-energia

                if Slink.rect.colliderect(bomba02.rect) and b02 :
                    b02=False
                    if energia > 2:
                        energia = energia -3
                    elif energia < 3:
                        energia=energia-energia

                #------------------------------------------------------------------------
                
                if Slink.rect.colliderect(arbol01.rect) :
                    link2x,link2y=xant,yant-5
                if Slink.rect.colliderect(arbol02.rect) :
                    link2x,link2y=xant,yant+5

                if Slink.rect.colliderect(arbol03.rect) and link2y > (a03y+20):
                    link2x,link2y=xant,yant+5
                elif Slink.rect.colliderect(arbol03.rect) and link2y < (a03y-20):
                    link2x,link2y=xant,yant-5

                """if Slink.rect.colliderect(arbol010.rect) and link2y > 460:
                    link2x,link2y=xant,yant-5"""
                if Slink.rect.colliderect(arbol010.rect) and link2x > (a010x+20):
                    link2x,link2y=xant+5,yant
                elif Slink.rect.colliderect(arbol010.rect) and link2y < (910-20):
                    link2x,link2y=xant-5,yant

                if Slink.rect.colliderect(arbol011.rect) and link2y > 520:
                    link2x,link2y=xant,yant+5
                elif Slink.rect.colliderect(arbol011.rect) and link2y < (a011y+20):
                    link2x,link2y=xant,yant-5

                if Slink.rect.colliderect(arbol012.rect) and link2y > 520:
                    link2x,link2y=xant,yant+5
                elif Slink.rect.colliderect(arbol012.rect) and link2y < (a012y+20):
                    link2x,link2y=xant,yant-5

                if Slink.rect.colliderect(arbol013.rect) and link2y > 520:
                    link2x,link2y=xant,yant+5
                elif Slink.rect.colliderect(arbol013.rect) and link2y < (a013y+20):
                    link2x,link2y=xant,yant-5
                elif Slink.rect.colliderect(arbol013.rect) and link2x > 520:
                    link2x,link2y=xant+5,yant
                elif Slink.rect.colliderect(arbol013.rect) and link2x < (a013x+20):
                    link2x,link2y=xant-5,yant
                    
                if Slink.rect.colliderect(arbol014.rect) and link2y > 520:
                    link2x,link2y=xant,yant+5
                elif Slink.rect.colliderect(arbol014.rect) and link2y < (a014y+20):
                    link2x,link2y=xant,yant-5
                elif Slink.rect.colliderect(arbol014.rect) and link2x > (a014x+20):
                    link2x,link2y=xant-5,yant                    

                if Slink.rect.colliderect(arbol015.rect) and link2y > 580:
                    link2x,link2y=xant,yant-5
                elif Slink.rect.colliderect(arbol015.rect) and link2x < (a015x+20):
                    link2x,link2y=xant-5,yant
                elif Slink.rect.colliderect(arbol015.rect) and link2x > (a015x+20):
                    link2x,link2y=xant+5,yant

                if Slink.rect.colliderect(zelda01.rect):
                    zelda01.rect.top,zelda01.rect.left=cpy,cpx                
                    rescate=True

                #----------------------------------------------------------------------

                if Slink.rect.colliderect(ac01.rect):
                    if lucha:
                        ac01x,ac01y= 1000,1000
                    else:
                        (link2x,link2y) = (xant+5,yant)

                if Slink.rect.colliderect(ac02.rect):
                    if lucha:
                        ac02x,ac02y= 1000,1000
                    else:
                        (link2x,link2y) = (xant+5,yant)

                if Slink.rect.colliderect(ac03.rect):
                    if lucha:
                        ac03x,ac03y= 1000,1000
                    else:
                        (link2x,link2y) = (xant+5,yant)

                if Slink.rect.colliderect(ac04.rect):
                    if lucha:
                        ac04x,ac04y= 1000,1000
                    else:
                        (link2x,link2y) = (xant+5,yant)

                if Slink.rect.colliderect(ac05.rect):
                    if lucha:
                        ac05x,ac05y= 1000,1000
                    else:
                        (link2x,link2y) = (xant,yant+5)

                if Slink.rect.colliderect(ac06.rect):
                    if lucha:
                        ac06x,ac06y= 1000,1000
                    else:
                        (link06x,link06y) = (xant-5,yant)

                if Slink.rect.colliderect(ac07.rect):
                    if lucha:
                        ac07x,ac07y= 1000,1000
                    else:
                        (link07x,link07y) = (xant-5,yant)

                if Slink.rect.colliderect(ac09.rect):
                    if lucha:
                        ac09x,ac09y= 1000,1000
                    else:
                        (link09x,link09y) = (xant-5,yant)

                if Slink.rect.colliderect(ac010.rect):
                    if lucha:
                        ac010x,ac010y= 1000,1000
                    else:
                        (link010x,link010y) = (xant,yant+5)

                if Slink.rect.colliderect(ac011.rect):
                    if lucha:
                        ac011x,ac011y= 1000,1000
                    else:
                        (link2x,link2y) = (xant+5,yant)

                if Slink.rect.colliderect(ac012.rect):
                    if lucha:
                        ac012x,ac012y= 1000,1000
                    else:
                        (link2x,link2y) = (xant-5,yant)

                
                    

                #------------------------------------------------------------------------
                
                screen.blit(background_image,(0,0))
                screen.blit(barra,(-10,-5))
                


                if vidas==5:
                    screen.blit(vida5,(840,0))
                elif vidas==4:
                    screen.blit(vida4,(840,0))
                elif vidas==3:
                    screen.blit(vida3,(840,0))
                elif vidas==2:
                    screen.blit(vida2,(840,0))
                elif vidas==1:
                    screen.blit(vida1,(840,0))
                
                #se pinta la cantidad de energía y se verifica para disminuir la vida
                if energia==5:
                    screen.blit(corazon,(910,60))
                    screen.blit(corazon,(840,60))
                    screen.blit(corazon,(770,60))
                    screen.blit(corazon,(700,60))
                    screen.blit(corazon,(630,60))
                elif energia==4:
                    screen.blit(corazon,(910,60))
                    screen.blit(corazon,(840,60))
                    screen.blit(corazon,(770,60))
                    screen.blit(corazon,(700,60))
                elif energia==3:
                    screen.blit(corazon,(910,60))
                    screen.blit(corazon,(840,60))
                    screen.blit(corazon,(770,60))
                elif energia==2:
                    screen.blit(corazon,(910,60))
                    screen.blit(corazon,(840,60))
                elif energia==1:
                    screen.blit(corazon,(910,60))
                elif energia==0 and vidas>0:
                    vidas=vidas-1
                    energia=5
                    link2x,link2y = linki2x,linki2y
                    actlink = linkr

                if m2y <= 210:
                    mar2=False
                elif m2y >= 420:
                    mar2=True
                if mar2:
                    m2y=m2y-6             
                elif mar2==False:
                    m2y=m2y+6  
                




                
                #------------------------------------------------------------------------------            

                screen.blit(background_image,(0,0))
                if c01:
                    screen.blit(corazon,(c01x,c01y))
                else:
                    screen.blit(corac,(c01x,c01y))
                

                            
                screen.blit(salida,(0,350))


                
                if rescate:
                    screen.blit(transpa,(0,210))
                else:
                    screen.blit(zelda,(0,210))

                if b01:
                    screen.blit(bomba,(b01x,b01y))
                else:
                    screen.blit(exp,(b01x,b01y))

                if b02:
                    screen.blit(bomba,(b02x,b02y))
                else:
                    screen.blit(exp,(b02x,b02y))

                
                screen.blit(barra,(-10,-5))

                #pintar la cantidad de vidas---
                if vidas==5:
                    screen.blit(vida5,(840,0))
                elif vidas==4:
                    screen.blit(vida4,(840,0))
                elif vidas==3:
                    screen.blit(vida3,(840,0))
                elif vidas==2:
                    screen.blit(vida2,(840,0))
                elif vidas==1:
                    screen.blit(vida1,(840,0))
                #se pinta la cantidad de energía y se verifica para disminuir la vida
                if energia==5:
                    screen.blit(corazon,(910,60))
                    screen.blit(corazon,(840,60))
                    screen.blit(corazon,(770,60))
                    screen.blit(corazon,(700,60))
                    screen.blit(corazon,(630,60))
                elif energia==4:
                    screen.blit(corazon,(910,60))
                    screen.blit(corazon,(840,60))
                    screen.blit(corazon,(770,60))
                    screen.blit(corazon,(700,60))
                elif energia==3:
                    screen.blit(corazon,(910,60))
                    screen.blit(corazon,(840,60))
                    screen.blit(corazon,(770,60))
                elif energia==2:
                    screen.blit(corazon,(910,60))
                    screen.blit(corazon,(840,60))
                elif energia==1:
                    screen.blit(corazon,(910,60))
                elif energia==0 and vidas>0:
                    vidas=vidas-1
                    energia=5
                    linkx,linky = linkix,linkiy
                    actlink = linkr
                elif energia==0 and vidas==0:
                    empezar=False

                if rescate:
                    screen.blit(zelda,(140,24))
                else:
                    screen.blit(indicador,(140,24))
                    
                
                reloj1.tick(29)
                
                screen.blit(arbolcut,(ac01x,ac01y))
                screen.blit(arbolcut,(ac02x,ac02y))                                
                screen.blit(arbolcut,(ac03x,ac03y))              
                screen.blit(arbolcut,(ac04x,ac04y))               
                screen.blit(arbolcut,(ac05x,ac05y))
                screen.blit(arbolcut,(ac06x,ac06y))
                screen.blit(arbolcut,(ac07x,ac07y))
              
                screen.blit(arbolcut,(ac09x,ac09y))
                screen.blit(arbolcut,(ac010x,ac010y))
                screen.blit(arbolcut,(ac011x,ac011y))
                screen.blit(arbolcut,(ac012x,ac012y))
                

                screen.blit(a14,(a01x,a01y))
                screen.blit(a14,(a02x,a02y))
                screen.blit(a13,(a03x,a03y))
                
                screen.blit(h4,(a010x,a010y))
                screen.blit(a2,(a011x,a011y))
                screen.blit(a2,(a012x,a012y))
                screen.blit(h2,(a013x,a013y))
                screen.blit(a3,(a014x,a014y))
                screen.blit(h2,(a015x,a015y))
                
                
                if nivel==3:
                    screen.blit(n3,(nvx,nvy))
                    
                screen.blit(malo,(m01x,m01y))
                screen.blit(malo,(m02x,m02y))
                
                
                screen.blit(Slink.image,Slink.rect)     
                if vidas==0:
                    screen.blit(go,(315, 315))
                    nivel=4
                if Slink.rect.colliderect(pn2.rect) and rescate:
                    screen.blit(win,(140,190))
                    nivel=4


                screen.blit(reloj, (0,0)) #Pone la palabra tiempo en la pantalla
                tiempo = (pygame.time.get_ticks()/1000)-restati  #Pasa el tiempo a segundos 
                tiempo = str(tiempo ) #No tengo la menor idea de que hace, pero si lo quito falla
                contador = fuente.render(tiempo ,0,(0,0,230))#Es el tiempo que se pone en la pantalla, pero con un formato y todo eso
                screen.blit(contador,(80, 23))#Pone el contador en la pantalla
                if float((pygame.time.get_ticks()/1000))%181==0:
                    contesp=0


                if float((pygame.time.get_ticks()/1000))%180==0 and contesp==0:

                    if vidas > 0:
                        contesp=1
                        vidas = vidas-1
                        energia=5
                        restati=restati+5

                        linkx,linky=linkix,linkiy
                    if vidas == 0:
                        screen.blit(go,(315, 315))

                        nivel=4

                pygame.display.update() 

        ##########################################-------------------------------NIVEL1----------------------------#######################################3

            elif nivel==1:
                Slink=pygame.sprite.Sprite()
                Slink.image=actlink
                Slink.rect=actlink.get_rect()
                Slink.rect.top,Slink.rect.left=link3y,link3x #posicion en y,x

                zelda1 = pygame.sprite.Sprite()
                zelda1.image = zelda
                zelda1.rect=zelda.get_rect()
                zelda1.rect.top,zelda1.rect.left=z3y,z3x
                screen.blit(zelda1.image,zelda1.rect)

                pn3 = pygame.sprite.Sprite()
                pn3.image = salida
                pn3.rect=salida.get_rect()
                pn3.rect.top,pn3.rect.left=pn3y,pn3x
                screen.blit(pn3.image,pn3.rect)

                #######---------Arboles normales-------######

                arbol1 = pygame.sprite.Sprite()
                arbol1.image = a14
                arbol1.rect=a14.get_rect()
                arbol1.rect.top,arbol1.rect.left=a1y,a1x
                #screen.blit(arbol1.image,arbol1.rect)

                arbol2 = pygame.sprite.Sprite()
                arbol2.image = a14
                arbol2.rect=a14.get_rect()
                arbol2.rect.top,arbol2.rect.left=a2y,a2x
                screen.blit(arbol2.image,arbol2.rect)

                arbol100 = pygame.sprite.Sprite()
                arbol100.image = a9
                arbol100.rect=a9.get_rect()
                arbol100.rect.top,arbol100.rect.left=a100y,a100x
                screen.blit(arbol100.image,arbol100.rect)

                arbol101 = pygame.sprite.Sprite()
                arbol101.image = a4
                arbol101.rect=a4.get_rect()
                arbol101.rect.top,arbol101.rect.left=a101y,a101x
                screen.blit(arbol101.image,arbol101.rect)

                arbol102 = pygame.sprite.Sprite()
                arbol102.image = a9
                arbol102.rect=a9.get_rect()
                arbol102.rect.top,arbol102.rect.left=a102y,a102x
                screen.blit(arbol102.image,arbol102.rect)

                arbol103 = pygame.sprite.Sprite()
                arbol103.image = a4
                arbol103.rect=a4.get_rect()
                arbol103.rect.top,arbol103.rect.left=a103y,a103x
                screen.blit(arbol103.image,arbol103.rect)




                #######----------Arbolescut---------#######

                ac100 = pygame.sprite.Sprite()
                ac100.image = arbolcut
                ac100.rect=arbolcut.get_rect()
                ac100.rect.top,ac100.rect.left=ac100y,ac100x
                screen.blit(ac100.image,ac100.rect)

                malo3 = pygame.sprite.Sprite()
                malo3.image = malo
                malo3.rect=malo.get_rect()
                malo3.rect.top,malo3.rect.left=m3y,m3x
                screen.blit(malo3.image,malo3.rect)


                xant = link3x
                yant = link3y        
                link3x +=vx
                link3y +=vy

                if m3y >= 350:
                    mab3=False
                elif m3y <= 210:
                    mab3=True
                if mab3:
                    m3y=m3y+6             
                elif mab3==False:
                    m3y=m3y-6 



                ####--------Arbolesnormales----### COLISION
                if Slink.rect.colliderect(arbol1.rect):
                    (link3x,link3y) = (xant,yant-5)
                if Slink.rect.colliderect(arbol2.rect):
                    (link3x,link3y) = (xant,yant+5)

                if Slink.rect.colliderect(arbol100.rect) :
                    (link3x,link3y) = (xant,yant+5)
                if Slink.rect.colliderect(arbol102.rect) :
                    (link3x,link3y) = (xant,yant-5)
                if Slink.rect.colliderect(arbol101.rect) :
                    (link3x,link3y) = (xant,yant+5)
                if Slink.rect.colliderect(arbol103.rect) :
                    (link3x,link3y) = (xant,yant-5)

                

                ###--------COLISION Arboles cut----###
                if Slink.rect.colliderect(ac100.rect):
                    if lucha:

                        ac100x,ac100y=cpx,cpy
                    else:
                        (link3x,link3y) = (xant,yant+5)

                if Slink.rect.colliderect(zelda1.rect) :
                    rescate=True
                if Slink.rect.colliderect(pn3.rect):
                    if rescate:
                        nivel=2
                        restati = restati+((pygame.time.get_ticks()/1000)-restati)
                        rescate=False

                if Slink.rect.colliderect(malo3.rect) :
                    if energia > 0 :
                        energia = energia - 1
                    if energia == 0:
                        if vidas>0:
                            vidas=vidas-1
                            energia=5
                            link3x,link3y=linkix,linkiy
                        else: 
                            screen.blit(go,(315,315))
                            nivel=4





                screen.blit(background_image,(0,0))
                screen.blit(barra,(-10,-5))

                if vidas==5:
                    screen.blit(vida5,(840,0))
                elif vidas==4:
                    screen.blit(vida4,(840,0))
                elif vidas==3:
                    screen.blit(vida3,(840,0))
                elif vidas==2:
                    screen.blit(vida2,(840,0))
                elif vidas==1:
                    screen.blit(vida1,(840,0))
                
                #se pinta la cantidad de energía y se verifica para disminuir la vida
                if energia==5:
                    screen.blit(corazon,(910,60))
                    screen.blit(corazon,(840,60))
                    screen.blit(corazon,(770,60))
                    screen.blit(corazon,(700,60))
                    screen.blit(corazon,(630,60))
                elif energia==4:
                    screen.blit(corazon,(910,60))
                    screen.blit(corazon,(840,60))
                    screen.blit(corazon,(770,60))
                    screen.blit(corazon,(700,60))
                elif energia==3:
                    screen.blit(corazon,(910,60))
                    screen.blit(corazon,(840,60))
                    screen.blit(corazon,(770,60))
                elif energia==2:
                    screen.blit(corazon,(910,60))
                    screen.blit(corazon,(840,60))
                elif energia==1:
                    screen.blit(corazon,(910,60))
                elif energia==0 and vidas>0:
                    vidas=vidas-1
                    energia=5
                    link3x,link3y = linki3x,linki3y
                    actlink = linkr
                if rescate:
                    screen.blit(zelda,(140,24))
                else:
                    screen.blit(indicador,(140,24))
                if rescate:
                    screen.blit(transpa,(z3x,z3y))
                else:
                    screen.blit(zelda,(z3x,z3y))

                

                if link3x<=limi_ancho_izquierda:#if se llega a ir mas del limite
                    link3x=limi_ancho_izquierda
                
                elif link3x>=limi_ancho_derecha:#if se llega a ir mas del limite
                    link3x=limi_ancho_derecha
                
                elif link3y<=limi_altura_arriba:#if se llega a ir mas del limite
                    link3y=limi_altura_arriba
                
                elif link3y>=limi_altura_abajo:
                    link3y=limi_altura_abajo



                screen.blit(a14,(a1x,a1y))
                screen.blit(a14,(a2x,a2y))
                screen.blit(a9,(a100x,a100y))
                screen.blit(a9,(a102x,a102y))
                screen.blit(a4,(a101x,a101y))
                screen.blit(a4,(a103x,a103y))

                screen.blit(salida,(pn3x,pn3y))

                screen.blit(malo,(m3x,m3y))

                screen.blit(arbolcut,(ac100x,ac100y))

                screen.blit(n1,(nvx,nvy))

                screen.blit(Slink.image,Slink.rect)
                if vidas==0:
                    screen.blit(go,(315, 315))
                    nivel=4

                screen.blit(reloj, (0,0)) #Pone la palabra tiempo en la pantalla
                tiempo = (pygame.time.get_ticks()/1000)-restati  #Pasa el tiempo a segundos 
                tiempo = str(tiempo ) #No tengo la menor idea de que hace, pero si lo quito falla
                contador = fuente.render(tiempo ,0,(0,0,230))#Es el tiempo que se pone en la pantalla, pero con un formato y todo eso
                screen.blit(contador,(80, 23))#Pone el contador en la pantalla
                if float((pygame.time.get_ticks()/1000))%181==0:
                    contesp=0



                if float((pygame.time.get_ticks()/1000))%180==0 and contesp==0:

                    if vidas > 0:
                        contesp=1
                        vidas = vidas-1
                        energia=5
                        restati=restati+5

                        linkx,linky=linkix,linkiy
                    if vidas == 0:
                        screen.blit(go,(315, 315))

                        nivel=4

                pygame.display.update() 
            










main()
