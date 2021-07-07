import random
 computerguess = random.randint(1,9)
 userguess = input("enter the no. between 1 and 9")

  if computerguess == userguess:
      print("You are correct! Congratulations")


  if computerguess > userguess:
      print("Wrong, try again")

   
  if computerguess < userguess: 
      print("Wrong, try again")


    


