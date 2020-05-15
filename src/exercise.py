from random import randint

def main():
    number = randint(1,10)

    while True:

      try: 
        guess = int(input("Guess a number: "))

        if guess == number:
          print("Yes!")
          return
        elif guess > number:
          print("Too high!")
        elif guess < number:
          print("Too low!")
      
      except:
        print("I didn't quite catch that!") 
        
if __name__ == '__main__':
    main()
