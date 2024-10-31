# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
# Use randint to generate random cards.
from blackjack_helper import *

# Write all of your part 3 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.

# Initialize the game
no_of_players = int(input("Welcome to Blackjack! How many players? "))

if no_of_players > 0:
    player_names = []
    name_count = {}  # Dictionary to track duplicate names
    player_scores = {}  # Dictionary to store player scores (start with 3 points)
    player_trials = {}  # Dictionary to track remaining trials (start with 3)

    # Get player names, account for duplicates, and initialize scores and trials
    for i in range(1, no_of_players + 1):
        player_name = input(f"What is player {str(i)}'s name? ").strip()

        # Check for duplicate names and append a number if necessary
        if player_name in name_count:
            name_count[player_name] += 1
            player_name += f"_{name_count[player_name]}"
        else:
            name_count[player_name] = 1

        player_names.append(player_name)
        player_scores[player_name] = 3  # Start with 3 points
        player_trials[player_name] = 3  # Each player has 3 trials

    # Play rounds until players are eliminated or they want to stop
    keep_playing = 'y'
    while keep_playing == 'y' and player_names:
        # USERS' TURN
        hand_totals = {}
        for player in player_names[:]:  # Use a slice to modify list inside loop
            PLAYER = player.upper() + "'S"
            user_hand = draw_starting_hand(PLAYER)
            should_hit = 'y'

            # Player hits or stands until they reach 21 or choose to stop
            while user_hand < 21:
                should_hit = input(f"You have {user_hand}. Hit (y/n)? ").lower().strip()
                if should_hit == 'n':
                    break
                elif should_hit != 'y':
                    print("Sorry, I didn't get that.")
                else:
                    user_hand += draw_card()

            print_end_turn_status(user_hand)
            hand_totals[player] = user_hand

        # DEALER'S TURN
        dealer_hand = draw_starting_hand("DEALER")
        while dealer_hand < 17:
            print(f"Dealer has {dealer_hand}.")
            dealer_hand += draw_card()
        print_end_turn_status(dealer_hand)

        # GAME RESULT
        print_header("GAME RESULT")
        for player, user_hand in hand_totals.items():
            if user_hand <= 21 and (user_hand > dealer_hand or dealer_hand > 21):
                # Player wins the round
                player_scores[player] += 1
                print(f"{player} wins! Score: {player_scores[player]}")
            elif user_hand > 21 or (dealer_hand <= 21 and dealer_hand > user_hand):
                # Player loses the round, reduce a trial
                player_trials[player] -= 1
                print(f"{player} loses! Score: {player_trials[player]}")
            else:
                # It's a push (no winner)
                print(f"{player} pushes. Score: {player_scores[player]}")

        # Eliminate players with 0 trials
        for player in player_names[:]:
            if player_trials[player] <= 0:
                print(f"{player} eliminated! No trials left.")
                player_names.remove(player)

        if not player_names:
            print("All players eliminated!")
            break

        # Ask if players want to play another hand
        keep_playing = input("Do you want to play another hand (y/n)? ").lower().strip()

print("Game over.")
