# You can try and play the game alternatively at https://www.247blackjack.com/
# This model uses only one shape of cards

import time
import random


def play(cards):

    dealer_total = 0
    player_total = 0

    for i in range(5):
        ran_dealer_card = random.choice(cards)
        dealer.append(ran_dealer_card)
        index_of_chosen_d = cards.index(ran_dealer_card)
        cards.pop(index_of_chosen_d)
        if ran_dealer_card == "A":
            dealer_total += random.choice(card_values["A"])
        else:
            dealer_total += card_values[dealer[i]]

        if dealer_total >= 17:
            break

    print(f"Dealer : {dealer[0]} | Dealer's total : {dealer_total}")

    for j in range(6):
        ran_player_card = random.choice(cards)
        player.append(ran_player_card)
        index_of_chosen_p = cards.index(ran_player_card)
        cards.pop(index_of_chosen_p)

        if ran_player_card == "A":
            choice_a = input("Do you want 1 or 11 ? ")
            if choice_a == "1":
                player_total += card_values["A"][1]
            elif choice_a == "11":
                player_total += card_values["A"][0]
            else:
                player_total += random.choice(card_values["A"])

        else:
            player_total += card_values[player[j]]

        print(f"Player : {player} | Player total : {player_total}")
        # print(f"Player : {player}")
        hit_or_stand = input("Do you want to 'HIT' or 'STAND'? ")
        if hit_or_stand.lower() == "stand":
            break
        if player_total >= 21:
            break

    if player_total > 21:
        print("\nYou LOSE! Total exceeded 21!")
    elif player_total == 21:
        print("\nBlackjack!!!You WIN!")
    elif player_total > dealer_total:
        print("\nCongratulations!!!You have BEATEN the dealer at his won game!")
    elif player_total < dealer_total:
        print("\nSorry!!!The dealer has BEATEN you!")
    elif player_total == dealer_total:
        print("\nThe Game ends in a DRAW!")
    else:
        print("Condition not grabbed by the dev!")


print("Welcome to Blackjack!")
print("You start with Ksh. 25,000 available to bet.\n")
available = 25000
time.sleep(2)
bet = int(input("Place your bet. Ksh. 10, Ksh. 100, Ksh. 1,000 or Ksh. 5,000 : "))
available -= bet
deal = input("Type 'deal' to go through with the deal, or Ksh. 10, 100, 1,000 or 5,000 to add to bet : ")

all_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "K", "Q", "J", "A"]
# all_cards = ["2", "3", "4", "A"]

card_values = {
    "K": 10,
    "J": 10,
    "Q": 10,
    "A": [11, 1],

    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
}
dealer = []
player = []

while True:
    if deal == "10":
        bet += 10
        available -= 10
        print(f"Available : {available}, Bet : {bet}")
        deal = input("Type 'deal' to go through with the deal, or Ksh. 10, 100, 1,000 or 5,000 to add to bet : ")
    elif deal == "100":
        bet += 100
        available -= 100
        print(f"Available : {available}, Bet : {bet}")
        deal = input("Type 'deal' to go through with the deal, or Ksh. 10, 100, 1,000 or 5,000 to add to bet : ")
    elif deal == "1000":
        bet += 1000
        available -= 1000
        print(f"Available : {available}, Bet : {bet}")
        deal = input("Type 'deal' to go through with the deal, or Ksh. 10, 100, 1,000 or 5,000 to add to bet : ")
    elif deal == "5000":
        bet += 5000
        available -= 5000
        print(f"Available : {available}, Bet : {bet}")
        deal = input("Type 'deal' to go through with the deal, or Ksh. 10, 100, 1,000 or 5,000 to add to bet : ")
    elif deal.lower() == "deal":
        # run the rest of the game here
        play(all_cards)
        break
    else:
        time.sleep(1.5)
        print("Invalid input selected.")





