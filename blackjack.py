import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def blackjack():
    want_to_play=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if want_to_play=='y':
        your_card=random.choices(cards, k=2)
        current_score=sum(your_card)
        print(f"Your cards:{your_card},current score:{current_score}")
        computer_card=random.choices(cards, k=2)
        print(f'Computer\'s first card:{computer_card[0]}')
        if current_score==21:
            if sum(computer_card)==21:
                print("it’s a push")
                return
            else:
                print("it is a Blackjack!you win😊")
                return
        move_ahead=True
        while move_ahead:
            continue_forward = input('Type \'y\' to get another card, type \'n\' to pass:').lower()
            if continue_forward=='y':
                your_card.append(random.choice(cards))
                computer_card.append(random.choice(cards))
                current_score = sum(your_card)
                print(f"Your cards:{your_card},current score:{current_score}")
                print(f'Computer\'s first card:{computer_card[0]}')
                if current_score>21:
                    print("You went over. You lose 😭")
                    return
                if current_score==21:
                    print("it is a Blackjack!you win😊")
                    return
            else:
                print(f'Your final hand: {your_card}, final score: {current_score}')
                print(f"Computer's final hand: {computer_card}, final score: {sum(computer_card)}")
                while sum(computer_card)<17:
                    computer_card.append(random.choice(cards))
                if sum(computer_card)==21:
                    print('Lose, opponent has Blackjack 😱')
                    return
                if sum(computer_card)>21:
                    print("Opponent went over. You win 😁")
                    return
                elif current_score>sum(computer_card):
                    print('You win 😃')
                    return
                elif current_score<sum(computer_card):
                    print( "You lose 😤")
                    return
blackjack()
