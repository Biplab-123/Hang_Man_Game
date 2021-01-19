#required libaries
import pygame
import math
import random

pygame.init()



##All Constants and variable
WIDTH=800
HEIGHT=500
global FPS
FPS=60
WHITE=(255,255,255)
BLACK=(0,0,0)

##word font
WORD_FONT=pygame.font.SysFont('comicsans',60) 

#font of the letters
LETTER_FONT=pygame.font.SysFont('comicsans',40)

#title font
TITLE_FONT=pygame.font.SysFont('comicsans',70)


#size of the Circle that have all 26 characters init
RADIUS=20


#gap between two circle
GAP=15
   
#image variable

hangman_status=0


#list of letters
letters=[]







#Main Screen Display

win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hang_Man")







#starting positions of letters

startx=round((WIDTH-(RADIUS*2+GAP)*13) /2)  ##X position of the letter of circle
starty=400                                  ##Y position of the letter of circle
A=65 #ASCII value of chracter A





#loop of 26 characters 
for i in range(26):
    x=startx + GAP*2 +((RADIUS*2 + GAP)*(i%13)) 
    y=starty + ((i//13) * (GAP + RADIUS *2))
    letters.append([x,y,chr(A+i),True])






#load images of the Hangman
images=[]
for i in range(7): #total 6 imgae
    image=pygame.image.load("hangman" +str(i)+ ".png")
    images.append(image)






#word need to be guessed
words=["DEVELOPER","IDE","PYTHON","CRICKET","FOOTBALL","MESSI","RONALDO","BIPLAB","RITUPARNO","MAA","OPTIMISTIC"]
word=random.choice(words)
guessed=[]





clock=pygame.time.Clock()






##draw eerything in the pogram
def draw():
    win.fill(WHITE) #background of the pogram
    text=TITLE_FONT.render("DEVELOPER HANGMAN",1,BLACK) ##game name at the top of the screen
    win.blit(text,(WIDTH/2 - text.get_width()/2 ,20))

    #draw word
    display_word=" "  #display the word
    for letter in word:
        if letter in guessed:
            display_word+=letter + " "
        else:
            display_word+="_ "
    text=WORD_FONT.render(display_word,1,BLACK) ##guessed letter font
    win.blit(text,(400,200))                    ##position of the letter for displayig




#draw Button(small Circle) and place all the Character from A - Z in the circle
    for letter in letters:
        x,y,ltr,visible = letter
        if(visible):
            pygame.draw.circle(win,BLACK,(x,y),RADIUS,3) #draw the circle
            text=LETTER_FONT.render(ltr,1,BLACK)  ##1 stand for antialias
            win.blit(text,(x-text.get_width()/2 , y-text.get_height()/2)) #position the letters in proper position inside the circle
        
    win.blit(images[hangman_status],(150,100)) ##(150,100)is the position of image
    pygame.display.update() #update the screen each time





#to display win or loss
def display_message(message):
    win.fill(WHITE)
    text=WORD_FONT.render(message,1,BLACK)
    win.blit(text,(WIDTH/2 - text.get_width()/2 ,HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)




    
##if you lost it display what letter it actually was
def actual_word(correct_word):
    win.fill(WHITE)
    text=WORD_FONT.render(correct_word,1,BLACK)
    win.blit(text,(WIDTH/2 - text.get_width()/2 ,HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2000)
    


#restart game ##not implemented yet
def restart_game():
    win.fill(WHITE)
    hangman_status=0
    won=True
    






run=True
while run:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            run=False

        if(event.type == pygame.MOUSEBUTTONDOWN):

            #pos is position of the mouse
            m_x,m_y = pygame.mouse.get_pos() #get the mouse position in each click
            for letter in letters:
                x,y,ltr,visible=letter
                if(visible): ##we do it because we dont want to press a button more than once ,if we press a button single time it will Disappear
                    dis=math.sqrt((x - m_x)**2 +(y - m_y)**2) ##apply formula to get the each circle position 
                    if(dis<RADIUS):  ##check the position is less than the radius of the cricle 
                        letter[3]=False ##3 indictae the true and false
                        guessed.append(ltr) #append the letters each time in the list

                        #if we guessed a worng word than add hangman image each time 
                        if ltr not in word:
                            hangman_status+=1

    #call the Draw Function
    draw() 


                          
#check we win or loss
    won=True
    for letter in word:
        if letter not in guessed:
            won=False
            break

    if(won):
        display_message("YOU WON!!")
        break

    if(hangman_status == 6):
        display_message("YOU LOST!!")
        actual_word("Correct word is!!"+ word)
        break

    
                
   
pygame.quit()                













            




