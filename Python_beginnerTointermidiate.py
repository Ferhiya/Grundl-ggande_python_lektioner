#input() for getting value from user
#print() to print to display

#functions and modules
import math
print("test commit message")


"""
#övningar 2

print("2021") #prints string
print(2021) #prints int"
print("2021-12-24") #prints string
print(2021-12-24) #prints sub of int, alltså räknar ut vad subtractionen blir

"""

""" 
#övningar 3
name="tia"
age=25
print("my name is: ", name, "and I'm ",age)
 '
 """
 
"""
#övning 4
name=input("Enter your firstname: ")
lastname=input("Enter lastname: ")
print("Hello your name is:", lastname,name)
"""
 
""" 
 #övning 5
num1=int(input("Enter fisrt number: "))
num2=int(input("Enter second number: "))

result1=num1**num2
print("Tal1 upphöjd med tal2: ",result1)
res2=num1*num2
print("Tal1 gånger tal2: ",res2)
res3=num1/num2
print("tal1 delat med tal2: ",res3)
res4=num1+num2
print("Tal1 plus tal2: ",res4)
res5=num1-num2
print("tal1 minus tal2: ",res5)
res6=num1%num2
print("tal1 heltaldviderat med tal2: ",res6) 
res7=num1//num2
print("räkna ut resten av divisonen mellan tal1 och tal2: ",res7)
"""

"""
#övning 6
num1=float(input("Enter fisrt number: "))
num2=float(input("Enter second number: "))

result1=num1**num2
print("Tal1 upphöjd med tal2: ",result1)
res2=num1*num2
print("Tal1 gånger tal2: ",res2)
res3=num1/num2
print("tal1 delat med tal2: ",res3)
res4=num1+num2
print("Tal1 plus tal2: ",res4)
res5=num1-num2
print("tal1 minus tal2: ",res5)
res6=num1%num2
print("tal1 heltaldviderat med tal2: ",res6) 
res7=num1//num2
print("räkna ut resten av divisonen mellan tal1 och tal2: ",res7)
"""

"""
#övning 7

name=input("Enter your name: ")
nameuprepat=name*5 #string manipulation, name gånger 5
print("",nameuprepat)
"""

"""
#övning 8
 Skriv ett programsomtarettTAL(int)sominput.DetskaskrivautFalseomtaletärmindreän100och
 Trueomdetärstörreellerlikamed100,
 OBS:UtanIf-satser. (skriv direkt ut resultat från jämförelsen)

num=int(input("Enter number: "))

print(num >= 100) #true om num är större eller lika med 100 annars false

"""


#if-satser
"""
#övning 1
num=int(input("enter number: "))

if(num > 10):
    print("Number is bigger than 10")
else:
    print("number is less than 10")    
"""

"""
#övning 2

NumofMilks=int(input("Enter the number of milk pakets that are left: "))

if(NumofMilks < 10):
    print("Order 30 milk pakets")
elif(NumofMilks >= 10 and NumofMilks <= 20):
    print("Order 20 milk pakets")
else: 
    print("You don't need to order more milk.")
"""
"""
#övning 3
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

if num1 > num2:
    largest=num1
else:
    largest=num2
    
print("The bigger number is: ",largest)
"""

"""
#övning 4

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    largest=num1
elif num2 >= num1 and num2 >= num3:
    largest=num2    
else:
    largest=num3
    
print("The bigger number is: ",largest)

"""

"""
#övning 5
print("Enter the category you belong to:")
print("1: Student")
print("2: Senior")
print("3: Regular adult")

adult=int(input(""))

if(adult == 1 or adult == 2):
    print("Ticket cost 20 kr")
elif(adult == 3): 
    print("Ticket cost 30 kr")   
else:
    print("Incorrect choice, try again.")
"""

"""
#övning 6

birthYear=int(input("Enter your birth year: "))

if birthYear >= 1980 and birthYear < 1990:
    print("You were born in the 1980s")
elif birthYear < 2000 and birthYear >= 1990:
    print("You were born in the 1990s")    
else:
    print("You were not born in 1980s or 1990s")
"""

"""
#övning 7

country=input("Enter your country of residence: ").lower()

if country in ["svergie","danmark","norge"]:
    print("You live in scandinavia")
else:
    print("You don't live in scandinavia")  
"""  
    
    
""" 
#övning 8 

Money=int(input("Enter the amount of money you have: "))
discount=input("Do you have a discount, Yes or No: ").lower()

if (15 <= Money <= 25) and discount == "no":
    print("You can buy a small hamburger")
elif (15 <= Money <= 25) and discount == "yes":
    print("You can buy a small hamburger and fries")
elif (25 < Money <= 50)  and discount == "no":
    print("You can buy a big hamburger")
elif (25 < Money <= 50) and discount == "yes":
    print("You can buy a big hamburger and fries")
elif (50 <= Money <= 60  or Money > 60 ) and discount == "yes":
    print("You can buy a meal with a drink")
else:
    print("You don't have enough money or the amount is too high for the options provided")
""" 

#Loopar

"""
#övning 1
#print for loop of 0-10 number
for x in range (11): 
    print(x)
    
  
 #print 0-10 using a while loop   
y=0
while y <= 10:
    print(y)
    y+=1    
"""

"""
#övning 2
# Användaren matar in två tal
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Kontrollera om num1 är mindre än num2 och skriv ut intervallen
if num1 <= num2:
    # Print numbers between num1 and num2 using a for loop
    for x in range(num1, num2 + 1):
        print(x)

    # Print numbers between num1 and num2 using a while loop
    i = num1
    while i <= num2:
        print(i)
   
        i += 1
       
# Kontrollera om num1 är större än num2 och skriv ut intervallen        
else:
    for x in range(num2, num1 + 1):
        print(x)

    # Print numbers between num1 and num2 using a while loop
    i = num2
    while i <= num1:
        print(i)
        i += 1
"""

"""
#övning 3
while True:
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    
    sum=num1+num2
    print("The sum of the two numbers is: ",sum)
    
    #ask user if they wanna continue program
    continue_prompt=input("Do you want to continue (J/N)? ").upper()
    
    
    #if user answers J, continue loop
    if continue_prompt == "J":
        continue
    
    #if user ansers N, avbrytt loop
    elif continue_prompt == "N":
        break
    
    # Hantera ogiltiga svar
    else:
        print("Invalid input. Please enter 'J' for yes or 'N' for no.")
        
print("Program terminated")
"""

"""
#övning 4

# Initiera en variabel för att hålla summan
total_sum = 0

# Upprepa processen 10 gånger
for _ in range(10):
    # Be användaren att mata in ett tal
    num = int(input("Enter a number: "))
    
    # Lägg till det inmatade talet till total_sum
    total_sum += num

# Skriv ut summan av de inmatade talen
print("Summan av det du matade in är:", total_sum)
"""

"""
#övning 5
num=int(input("enter number: "))

for x in range(1,num):
    print(x)
"""

"""
#övning 6
import random

while True:
    
  print("Roll the dices...")
  print("The values are...")
  
  dice1=random.randint(1,6)
  dice2=random.randint(1,6)
  
  # Skriv ut resultatet av båda tärningarna
  print("Dice 1:", dice1, "\nDice 2:", dice2)
  
  play_again=input("Roll the dices again (Y/N): ").lower()
  
  #roll dices again
  if play_again == "y":
      continue
  elif play_again == "n":
      break
print("Program terminated")
"""

#Listor

"""
#övning 1
numlist= []
# Upprepa processen 10 gånger
for _ in range(4):
    # Be användaren att mata in ett tal
    num = int(input("Enter a number: "))
    numlist.append(num)


largest=numlist[0]

for x in numlist:
    if x > largest:
        largest=x
print("Largest number is:",largest)
"""

"""
#random hänga gubbe
import random

def choose_word():
    words = ['python', 'cog', 'cat', 'pizza', 'cake']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def hangman_game():
    word = choose_word()
    guessed_letters = set()
    attempts = 6  # Number of incorrect guesses allowed
    
    print("Welcome to the hangman game")
    
    while attempts > 0:
        print("\n" + display_word(word, guessed_letters))
        print(f"Attempts remaining: {attempts}")
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Correct guess!")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You've guessed the word: {word}")
                break
        else:
            attempts -= 1
            print("Incorrect guess.")
        
        if attempts == 0:
            print(f"Game over! The word was: {word}")

# Start the game
hangman_game()
"""

"""
#övning 3
print("Hello, Welcome to nomans bank!")
print("1: Create account")
print("2: Delete acounbt")
print("3: List all account numbers")
print("4: List total balance")
print("5: List all acounts and balance")

menu=input("Pick a number on the menu: ")
"""