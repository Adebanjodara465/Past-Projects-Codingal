# a number is chosen
my_numbers = [1,3,5,67,5]
Num = my_numbers[2]
num2 = my_numbers[3]

#A boy is given a list of numbers to guess the  chosen one
print("Hello! \n Can you guess the lucky number?")

guess = int(input("Guess the number: "))

max_attempts = 5
attempts = 0

#if he guessed higher or lower, tell him through a message

if guess == Num:
    print("Wow you got it! \n Get ready for the next round!")

    while attempts < max_attempts:
        guess_2 = int(input("Can you guess this?"))
        attempts += 1
       
        if guess_2 == num2:
            print("Wow, how could you tell? You win!!")
          
            break #to exit the loop while the second guess is correct
        
        elif guess_2 >= num2:
            print(f"You have used {attempts} attempt out of 5.\n Here's a riddle to help:\n Three times two and a prime number that goes with S!")# try to give hints
        else:
            print(f"You have used {attempts} attempt out of 5.\n Not even close!.\n Try again")
        
        
        if attempts == max_attempts:
            print("Sorry all attempts for this quiz have been used")
            break

elif guess >= Num:
    print("How about a little lower?")
else:
    print("That's too low, think a little higher next time.")        



