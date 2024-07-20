print("Let's play a game that is EPIC BATTLE🥳")
print("Select your move (R,P,S")
player1_score=0
player2_score=0
while True:
  player1=input("take move for player1 ")
  player2=input("take move for player2 ")
  if player1=="R":
    if player2=="R":
      print("You both picked Rock, draw!🥳")
    elif player2=="P":
       print("Player1's Rock is smothered by Player2's Paper!🤣")
       player2_score+=1
    elif player2=="S":
      print("Player1 smashed Player2's Scissors into dust with their Rock!🤣")
      player1_score+=1
    else:
      print("Invalid move player2!🥺")
  elif player1=="P":
    if player2=="R":
      print("Player2's Rock is smothered by Player1's Paper!😂")
      player1_score+=1
    elif player2=="P":
      print("You both picked Paper!🥳")
    elif player2=="S":
      print("Player1's Paper is cut into tiny pieces by Player2's Scissors!😂")
      player2_score+=1
    else:
      print("Invalid move player2!🥺")
  elif player1=="S":
    if player2=="R":
      print("Player 2's Rock makes metal-dust out of Player1's Scissors!😅")
      player2_score+=1
    elif player2=="P":
      print("Player1's Scissors make confetti out of Player2's paper!😅")
      player1_score+=1
    elif player2=="S":
      print("You both picked Scissors!🥳")
  print("Player1's score=",player1_score)
  print("player2's score=",player2_score)
  if player1_score==3 or player2_score==3:
    print("Yah! Player1 is winner🥳.")
    break
  elif player2_score==3:
    print("Yah! Player2 is winner🥳.")
    break
  else:
    continue