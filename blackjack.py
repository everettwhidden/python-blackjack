import random
import math


cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
deck = cards + cards + cards + cards

print("\nHello! Welcome to blackjack. Let's deal!\n")

user_hand = random.sample(deck, 2)
for card in user_hand:
      deck.remove(card)

comp_hand = random.sample(deck, 2)
for card in comp_hand:
      deck.remove(card)

print(f"Your hand: {user_hand}\n")
print(f"My hand: {comp_hand}\n")

if sum(comp_hand) == 21 and sum(user_hand) == 21:
    print("We tied on the deal! Good game!")
elif sum(user_hand) == 21:
    print("Wow, you have a natural 21! You win!")
elif sum(comp_hand) == 21:
    print("I win! I have 21 off the deal! Good game.")
else:
    if sum(user_hand) < 21 and sum(comp_hand) < 21:
        while sum(user_hand) < 21:
            play = input("Do you want to hit, or stand?\n\n")
            if play == "hit":
                newuser_card = random.choice(deck)
                user_hand.append(newuser_card)
                deck.remove(newuser_card)
                while sum(user_hand) > 21 and 11 in user_hand:
                    user_hand[user_hand.index(11)] = 1
                print(f"\nOk! Your new hand: {user_hand}\n")
            elif play == "stand":
                print(f"\nOk, you have {sum(user_hand)} in your hand\n")
                break


                
        
    if sum(user_hand) > 21:
        print("You busted! Good game!")
        

    if sum(user_hand) == 21:
        print("Nice, you have 21. Now it is my turn.")

if sum(user_hand) <= 21 and sum(comp_hand) < 21:
    while sum(comp_hand) < 17:
        print("I am going to hit\n")
        newcomp_card = random.choice(deck)
        comp_hand.append(newcomp_card)
        deck.remove(newcomp_card)
        while sum(comp_hand) > 21 and 11 in comp_hand:
            comp_hand[comp_hand.index(11)] = 1
        print(f"My new hand: {comp_hand}\n")

    if sum(comp_hand) < 21:
        print(f"I am going to stand. I have {sum(comp_hand)} in my hand.")
    


if sum(user_hand) <= 21:
    if sum(user_hand) == 21 and sum(comp_hand) == 21:
        print("We tied! Good game!")
    elif sum(comp_hand) > 21:
        print("Congrats! You win! I busted.")
    elif sum(comp_hand) == 21:
        print("I win with 21! Good game!")
    elif sum(user_hand) < 21 and sum(comp_hand) < 21:
        if sum(user_hand) > sum(comp_hand):
            print("Congrats! You win!")
        elif sum(comp_hand) > sum(user_hand):
            print("Good game, I win!")
        else:
            print("We tied! Good game.")





    

