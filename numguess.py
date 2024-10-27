import random


def ng():
 print('''
-----------------------------
|          WELCOME          |
|            TO             |
|     GUESS THE NUMBER      |
|           GAME            |
-----------------------------''')
 print('''
Stages:
1. Easy (1 to 5)
2. Medium (1 to 50)

3. Medium-difficult (1 to 250)
4. Difficult (1 to 500)
5. Impossible (1 to 100000)''')
 n_stage=input('''Enter which stage you want to play: ''')
 guesses=0

 def gue():
        if guesses==1:
            print("You're pro, man!")
            con()
        elif guesses<=10:
            print("You're good.")
            con()
        if guesses<=20:
            print("You're ok.")
            con()
        else:
            print("You stuck at this try another game :{")
            exit()
 def con(): #  loop untill you say no
    n=input("Do you want to play again(yes/no): ")
    if n in ('n','no','N','NO','No'):
        exit()
    else:
      ng()
 if n_stage=='1' or n_stage.lower()=='easy':
    random_num=random.randint(1,5)
    n_user=int(input("\nGuess the number: "))
    while True:
        if n_user==random_num:
            guesses+=1
            print("You hit the right number.")
            print("\nYou got it in",guesses,"guesses.")
            gue()
        elif n_user>random_num:
            guesses+=1
            print("You're below the number.")
            n_user=int(input("\nGuess the next number: "))
        elif n_user<random_num:
            guesses+=1
            print("You're above the number.")
            n_user=int(input("\nGuess the next number: "))
        else:
            guesses+=1
            print("You hit the wrong number!")
            n_user=int(input("\nGuess the next number: "))

 elif n_stage=='2' or n_stage.lower()=='medium':
    random_num=random.randint(1,50)
    n_user=int(input("\nGuess the number: "))
    while True:
        if n_user==random_num:
            guesses+=1
            print("You hit the right number.")
            print("\nYou got it in",guesses,"guesses.")
            gue()
        elif n_user>random_num:
            guesses+=1
            print("You're below the number.")
            n_user=int(input("\nGuess the next number: "))
        elif n_user<random_num:
            guesses+=1
            print("You're above the number.")
            n_user=int(input("\nGuess the next number: "))
        else:
            guesses+=1
            print("You hit the wrong number!")
            n_user=int(input("\nGuess the next number: "))
            
 elif n_stage=='3' or n_stage.lower()=='medium-difficult':
    random_num=random.randint(1,250)
    n_user=int(input("\nGuess the number: "))
    while True:
        if n_user==random_num:
            guesses+=1
            print("You hit the right number.")
            print("\nYou got it in",guesses,"guesses.")
            gue()
        elif n_user>random_num:
            guesses+=1
            print("You're below the number.")
            n_user=int(input("\nGuess the next number: "))
        elif n_user<random_num:
            guesses+=1
            print("You're above the number.")
            n_user=int(input("\nGuess the next number: "))
        else:
            guesses+=1
            print("You hit the wrong number!")
            n_user=int(input("\nGuess the next number: "))

 if n_stage=='4' or n_stage.lower()=='difficult':
    random_num=random.randint(1,500)
    n_user=int(input("\nGuess the number: "))
    while True:
        if n_user==random_num:
            guesses+=1
            print("You hit the right number.")
            print("\nYou got it in",guesses,"guesses.")
            gue()
        elif n_user>random_num:
            guesses+=1
            print("You're below the number.")
            n_user=int(input("\nGuess the next number: "))
        elif n_user<random_num:
            guesses+=1
            print("You're above the number.")
            n_user=int(input("\nGuess the next number: "))
        else:
            guesses+=1
            print("You hit the wrong number!")
            n_user=int(input("\nGuess the next number: "))

 elif n_stage=='5' or n_stage.lower()=='impossible':
    random_num=random.randint(1,100000)
    n_user=int(input("\nGuess the number: "))
    while True:
     if n_user==random_num:
            guesses+=1
            print("You hit the right number.")
            print("\nYou got it in",guesses,"guesses.")
            gue()
     elif n_user>random_num:
            guesses+=1
            print("You're below the number.")
            n_user=int(input("\nGuess the next number: "))
     elif n_user<random_num:
            guesses+=1
            print("You're above the number.")
            n_user=int(input("\nGuess the next number: "))
     else:
            guesses+=1
            print("You hit the wrong number!")
            n_user=int(input("\nGuess the next number: "))
     
 if n_stage.isdigit:
  n_stage=int(n_stage)
  if n_stage not in (1,2,3,4,5):
      print("Type the right input!!!")
      ng()
 #elif n_stage.isalpha:
    #if n_stage not in ('easy','medium','medium-difficult','difficult','impossible'):
        #print("Type the right input!!!")

if __name__=='__main__':
 ng()
