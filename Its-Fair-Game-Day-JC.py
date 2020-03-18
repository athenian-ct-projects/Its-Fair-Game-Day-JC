import random
import time
print("this game is blackjack. If you are wondering which focus day this is connected to, it isn't connected to any of them. ")
print()
print("I started making it, and I forgot it had to be related to a focus day, but it was too late to switch, so here it is ")
print()
print("how to play: your goal is to get your card total closest to 21, and to beat the dealer. If you get over 21, you lose. stand to give the turn to the dealer, and hit to draw a new card")


#defines lists and values

cardlist=[]
dealerlist=[]
cardlistStr=[]
dealerlistStr=[]
c1=0
c2=0
c3=0
c4=0
a=0
b=0
da=0
db=0
winx=0
losex=0
#defines the list for where I will take card names

carddeck=['A','2','3','4','5','6','7','8','9','10','J','Q','K','A','2','3','4','5','6','7','8','9','10','J','Q','K','A','2','3','4','5','6','7','8','9','10','J','Q','K','A','2','3','4','5','6','7','8','9','10','J','Q','K']

#Assigns values to the card names

cardvalue={
        'A': 11,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10
  }
  

#this function crashes python
def crash():
  try:
   crash()
  except:
   crash()





                                              

#blakcjack funtion

def blackjack():
#define lose, tie, win functions that happen when you lose, win or tie
  def lose():
    global cardlist
    global dealerlist
    global cardlistStr
    global dealerlistStr
    global losex
    losex=losex+1
    print('you have won '+str(winx) + "times and lost "+str(losex)+" times")
    print()
    print('you lost :(')


    print("The dealer's cards are ")
    print(dealerlistStr)
    print()
    
    print("your cards are ")
    print(cardlistStr)
    cardlist=[]
    dealerlist=[]
    cardlistStr=[]
    dealerlistStr=[]
    again=input('try again? ')
    if again==('yes'):
      blackjack()
    if again==('no'):
      crash()

    else:
      again=input('yes or no')
      if again==('yes'):
        blackjack()
      if again==('no'):
        crash()

      
  def win():
    global cardlist
    global dealerlist
    global cardlistStr
    global dealerlistStr
    global winx
    winx=winx+1
    print('you have won '+str(winx) + " times and lost "+str(losex)+" times")
    print()
    print('you won :)')
  
    print("The dealer's cards are ")
    print(dealerlistStr)
    print()
    print("your cards are ")
    print(cardlistStr)
  
    cardlist=[]
    dealerlist=[]
    cardlistStr=[]
    dealerlistStr=[]
    again2=input('play again? ')
    if again2==('yes'):
      blackjack()  
    if again2==('no'):
      crash()
    if again2 != ('yes') or again2 != ('no'):
      again2=input('yes or no')
    if again2==('yes'):
      blackjack()  
    if again2==('no'):
      crash()





  def tie():
    global cardlist
    global dealerlist
    global cardlistStr
    global dealerlistStr

    print("The dealer's cards are ")
    print(dealerlistStr)
    print()
    print("your cards are ")
    print(cardlistStr)
    cardlist=[]
    dealerlist=[]
    cardlistStr=[]
    dealerlistStr=[]

    again2=input('you tied, play again? ')
    if again2==('yes'):
      blackjack()  
    if again2==('no'):
      print('ok')
      crash()
    if again2 != ('yes') or again2 != ('no'):
      again2=input('yes or no')
    if again2==('yes'):
      blackjack()  
    if again2==('no'):
      print('ok')
      crash()







  #globals the lists
  
 
  global cardlist
  global dealerlist
  global cardlistStr
  global dealerlistStr

#defines lists and some random ints
  cardlist=[]
  dealerlist=[]

  cardlistStr=[]
  dealerlistStr=[]

  c1=(random.randint(0,51))
  c2=(random.randint(0,51))
  c3=(random.randint(0,51))
  c4=(random.randint(0,51))

#this prints what your cards are at the start of the game
  print('Your cards are '+str(carddeck[c1])+' and '+str(carddeck[c2]))
  print("The dealer's open card is "+str(carddeck[c3]))
#after the dealer finishes their turn, this code checks who wins, loses, or ties
  def standcheck():
    if sum(dealerlist)<=(21):
      if sum(dealerlist)>sum(cardlist):
        lose()
      if sum(cardlist)>sum(dealerlist):
        win()
    if sum(dealerlist)==(21):
      if sum(dealerlist)==sum(cardlist): 
        tie()
      else:
        lose()
    if sum(dealerlist)>(21):
      for x in range(len(dealerlist)):
        if dealerlist[x]==(11):
          dealerlist[x]=(1)
        if sum(dealerlist)>(21):
          win()                  

#This determines what move the dealer does when it is their turn
  def stand():
    if sum(dealerlist)>(17):
      standcheck()
    if sum(dealerlist)==sum(cardlist):
      standcheck()
    if sum(dealerlist)>sum(cardlist):
      lose()
    else:
      dc1=(random.randint(0,51))
      dealerlist.append(cardvalue[carddeck[dc1]])
      dealerlistStr.append(carddeck[dc1])
      while sum(dealerlist)<=(16):
        dc2=(random.randint(0,51))
        dealerlist.append(cardvalue[carddeck[dc2]])
        dealerlistStr.append(carddeck[dc2])

        standcheck()

      if sum(dealerlist)>(17):
        standcheck()

 #Adds all the beginning variables to their resepctive lists
  cardlist.append(cardvalue[carddeck[c1]])
  cardlist.append(cardvalue[carddeck[c2]])
  dealerlist.append(cardvalue[carddeck[c3]])
  dealerlist.append(cardvalue[carddeck[c4]])
  cardlistStr.append(carddeck[c1])
  cardlistStr.append(carddeck[c2])
  dealerlistStr.append(carddeck[c3])
  dealerlistStr.append(carddeck[c4])


#asks w1=input('Hit or stand? ')
  choice1=input('Hit or stand? ') 
  while choice1!=('hit') and choice1!=('stand'):
      choice1=input('Pick either hit or stand ')
  if (cardlist)==(21):
    win()


  if choice1==('hit'):

      c5=random.randint(0,51)

      cardlist.append(cardvalue[carddeck[c5]])
      cardlistStr.append(carddeck[c5])

      print('Your cards are '+str(carddeck[c1])+', '+str(carddeck[c2])+', and '+ str(carddeck[c5]))
      if sum(cardlist)>(21):
        for x in range(len(cardlist)):
          if cardlist[x]==(11):
            cardlist[x]=(1)
        if sum(cardlist)>(21):
          lose()
      if sum(cardlist)==21:
          print('BLACKJACK')
          win()
      if sum(cardlist)<(21):
        choice1=input('Hit or stand? ')
        while choice1!=('hit') and choice1!=('stand'):
          choice1=input('Pick either hit or stand ')
        if choice1==('stand'):
          stand()
        if choice1==('hit'):

          c6=random.randint(0,51)
          cardlist.append(cardvalue[carddeck[c6]])
          cardlistStr.append(carddeck[c6])

          print('Your cards are '+str(carddeck[c1])+', '+str(carddeck[c2])+', '+ str(carddeck[c5])+', and '+(carddeck[c6]))
          if sum(cardlist)>21:
            for x in range(len(cardlist)):
              if cardlist[x]==(11):
                  cardlist[x]=(1)
            if sum(cardlist)>(21):
                lose()          
          if sum(cardlist)==21:
            print('BLACKJACK')
            win()
          else:
            choice1=input('Hit or stand? ')
            while choice1!=('hit') and choice1!=('stand'):
              choice1=input('Pick either hit or stand ')
            if choice1==('stand'):
              stand()
            if choice1==('hit'):
                c7=(random.randint(0,51))
                cardlist.append(cardvalue[carddeck[c7]])
                cardlistStr.append(carddeck[c7])
                print('Your cards are '+str(carddeck[c1])+', '+str(carddeck[c2])+', '+ str(carddeck[c5])+', '+(carddeck[c6])+', and '+(carddeck[c7]))
                if sum(cardlist)>21:
                  for x in range(len(cardlist)):
                    if cardlist[x]==(11):
                      cardlist[x]=(1)
                  if sum(cardlist)>(21):
                    lose()
                if sum(cardlist)==21:
                      print('BLACKJACK')
                      win()
                else:
                    choice1=input('Hit or stand? ')
                    while choice1!=('hit') and choice1!=('stand'):
                      choice1=input('Pick either hit or stand ')
                      if choice1==('stand'):
                        stand()
                      if choice1==('hit'):
                          c8=(random.randint(0,51))
                          cardlist.append(cardvalue[carddeck[c8]])
                          cardlistStr.append(carddeck[c8])
                          print('Your cards are '+str(carddeck[c1])+', '+str(carddeck[c2])+', '+ str(carddeck[c5])+', '+(carddeck[c6])+', '+(carddeck[c7])+', and '+(carddeck[c8]))
                          if sum(cardlist)>21:
                            for x in range(len(cardlist)):
                              if cardlist[x]==(11):
                                cardlist[x]=(1)
                            if sum(cardlist)>(21):
                                lose()
                          if sum(cardlist)==21:
                              print('BLACKJACK')
                              win()
                          else:
                            choice1=input('Hit or stand? ')
                            while choice1!=('hit') and choice1!=('stand'):
                              choice1=input('Pick either hit or stand ')
                              if choice1==('stand'):
                                stand()
                              if choice1==('hit'):
                                  c9=(random.randint(0,51))
                                  cardlist.append(cardvalue[carddeck[c9]])
                                  cardlistStr.append(carddeck[c9])
                                  print('Your cards are '+str(carddeck[c1])+', '+str(carddeck[c2])+', '+ str(carddeck[c5])+', '+(carddeck[c6])+', '+(carddeck[c7])+', '+(carddeck[c8])+', and '+(carddeck[c9]))
                                  if sum(cardlist)>21:
                                    for x in range(len(cardlist)):
                                      if cardlist[x]==(11):
                                        cardlist[x]=(1)
                                    if sum(cardlist)>(21):
                                        lose()
                                  if sum(cardlist)==21:
                                    print('BLACKJACK')
                                    win()
                                  else:
                                    choice1=input('Hit or stand? ')
                                    while choice1!=('hit') and choice1!=('stand'):
                                      choice1=input('Pick either hit or stand ')
                                      if choice1==('stand'):
                                        stand()
                                      if choice1==('hit'):
                                          c10=(random.randint(0,51))
                                          cardlist.append(cardvalue[carddeck[c10]])
                                          cardlistStr.append(carddeck[c10])
                                          print('Your cards are '+str(carddeck[c1])+', '+str(carddeck[c2])+', '+ str(carddeck[c5])+', '+(carddeck[c6])+', '+(carddeck[c7])+', '+(carddeck[c8])+',  '+(carddeck[c9])+', '+(carddeck(c10)))
                                          if sum(cardlist)>21:
                                            for x in range(len(cardlist)):
                                              if cardlist[x]==(11):
                                                cardlist[x]=(1)
                                            if sum(cardlist)>(21):
                                                lose()
                                          if sum(cardlist)==21:
                                            print('BLACKJACK')
                                            win()
                                          else:
                                            choice1=input('Hit or stand? ')
                                            while choice1!=('hit') and choice1!=('stand'):
                                              choice1=input('Pick either hit or stand ')
                                              if choice1==('stand'):
                                                stand()
                                              if choice1==('hit'):
                                                  c11=(random.randint(0,51))
                                                  cardlist.append(cardvalue[carddeck[c11]])
                                                  cardlistStr.append(carddeck[c11])
                                                  print('Your cards are '+str(carddeck[c1])+', '+str(carddeck[c2])+', '+ str(carddeck[c5])+', '+(carddeck[c6])+', '+(carddeck[c7])+', '+(carddeck[c8])+',  '+(carddeck[c9])+', '+(carddeck[c10])+" and "+(carddeck[c11]))
                                                  if sum(cardlist)>21:
                                                    for x in range(len(cardlist)):
                                                      if cardlist[x]==(11):
                                                        cardlist[x]=(1)
                                                    if sum(cardlist)>(21):
                                                        lose()
                                                  if sum(cardlist)==21:
                                                    print('BLACKJACK')
                                                    win()
  if choice1==('stand'):
    stand()
  



#a

blackjack()


