﻿
image bg intro = "the casino background.jpg"

image player_picked_card = "[player_card]_idle.png"
image opponent_picked_card = "[opponent_card]_idle.png"

# For main character

image cassandra:
    "images/cassandra/cassandra_1.png"
    pause 0.5
    "images/cassandra/cassandra_2.png"
    pause 0.1
    "images/cassandra/cassandra_1.png"

image opponent:
    "images/[opponent_name]/[opponent_name]_1.png"
    pause 0.1
    "images/[opponent_name]/[opponent_name]_2.png"

# The game starts here.

label start:

    scene bg intro

    # For initialization

    call variables from _call_variables

    # To display current money of the player

    show screen show_money

    menu start_menu:
        "Start":
            jump gameplay
        "Reset Level":
            $ level = 1
            call show_text("Level Reseted") from _call_show_text
            jump start_menu
        "Reset Game":
            $ level = 1
            $ money = 2000
            call show_text("Game Reseted") from _call_show_text_1
            jump start_menu

    return

# Initialize variables

label variables:
    $ player_cards_drawn = ["cards1", "cards2", "cards3"]
    $ player_card = " "
    $ opponent_card = " "
    $ level = 1
    $ winner = " "
    $ money = 2000
    $ beat = 0
    $ opponent_name = " "
    return

# Manage game and level

label gameplay:

    hide player_picked_card
    hide opponent_picked_card 
    
    $ text = level
    $ player_card = " "
    $ opponent_card = " " 

    if level == 1:
        jump level_1
    elif level == 2:
        jump level_2
    elif level == 3:
        jump level_3
    elif level == 4:
        jump level_4
    elif level == 5:
        jump level_5
    elif level == 6:
        jump level_6
    elif level == 7:
        jump level_7

# To display the beat in each game and subtruct the beat to the current money of player

label beat_menu:
    menu:
        "Beat [beat]":
            if money-beat >= 0:
                $ money -= beat
                return
            else:
                call show_text("You don't have enough balance") from _call_show_text_2
                jump gameplay
        "Main menu":
            jump start_menu

# Handle levels

label level_1:

    call show_text("Level 1") from _call_show_text_3

    $ beat = 100
    
    call beat_menu from _call_beat_menu
    
    # For displaying opponent images

    $ opponent_name = "pride"

    # To start the round

    jump play_round
    
label level_2:

    call show_text("Level 2") from _call_show_text_4

    $ beat = 200 
    
    call beat_menu from _call_beat_menu_1

    $ opponent_name = "envy"

    jump play_round

label level_3:
    call show_text("Level 3") from _call_show_text_5

    $ beat = 300 
    call beat_menu from _call_beat_menu_2

    $ opponent_name = "gluttony"
    jump play_round

label level_4:
    call show_text("Level 4") from _call_show_text_6

    $ beat = 400 
    call beat_menu from _call_beat_menu_3

    $ opponent_name = "lust"
    jump play_round

label level_5:
    call show_text("Level 5") from _call_show_text_7

    $ beat = 500 
    call beat_menu from _call_beat_menu_4

    $ opponent_name = "anger"
    jump play_round

label level_6:
    call show_text("Level 6") from _call_show_text_8

    $ beat = 600
    call beat_menu from _call_beat_menu_5

    $ opponent_name = "greed"
    jump play_round

label level_7:
    call show_text("Level 7") from _call_show_text_9

    $ beat = 700
    call beat_menu from _call_beat_menu_6

    $ opponent_name = "sloth"
    jump play_round

# To play each round
    
label play_round:

    call player_card_randomizer from _call_player_card_randomizer

    # players turn

    show cassandra
    call show_text("Your turn") from _call_show_text_10
    $ player_card = renpy.call_screen("choose_cards")

    # Opponent turn

    hide cassandra
    show opponent
    call show_text("Opponents turn") from _call_show_text_11

    # To generate random number

    call card_picker from _call_card_picker

    # To transform each number into a card
    
    if card_picked == 1:
        $ opponent_card = "rock"
    elif card_picked == 2:
        $ opponent_card = "paper"
    else:
        $ opponent_card = "scissors"

    hide opponent

    while True:
        
        # For deciding winner

        if player_card == opponent_card:
            $ winner = "tie"
        elif player_card == "rock":
            if opponent_card == "scissors":
                $ winner = "player"
            else:
                $ winner = "opponent"
        elif player_card == "paper":
            if opponent_card == "rock":
                $ winner = "player"
            else:
                $ winner = "opponent"
        elif player_card == "scissors":
            if opponent_card == "paper":
                $ winner = "player"
            else:
                $ winner = "opponent"

        # For displaying players card
        
        call show_choosen_card from _call_show_choosen_card
        
        # To handle winner        

        if winner == "player":
            call show_text("You win") from _call_show_text_12
            $ level += 1
            $ money += beat

            # To handle end level winner
            # Reset game and money to start at the beggining

            if level > 7:
                call show_text("Congratiolations! You beat the game") from _call_show_text_13
                $ level = 1
                $ money = 2000
                jump start_menu

            menu:
                "Continue to level [level]":
                    jump gameplay
                "Main Menu":
                    jump start_menu
        else:
            if winner == "opponent":
                call show_text("You lose") from _call_show_text_14
            else:
                $ money += beat
                call show_text("Tie") from _call_show_text_15

            menu:
                "Play Again":
                    jump gameplay
                "Main menu":
                    $ level = 1
                    jump start_menu

# To show choosen card of the player and the opponent

label show_choosen_card:

    # Shows picked card of the player

    show player_picked_card with dissolve:
        xalign 0.3
        yalign 0.5

    # Shows picked card of the player

    show opponent_picked_card with dissolve:
        xalign 0.7
        yalign 0.5

    # To puase the game for 1 sec. while shoowing off the card

    pause 1

    # To hide cards

    hide player_picked_card
    hide opponent_picked_card 

    return
    
# To display text

label show_text(text):
    show text "[text]" at truecenter with dissolve
    pause 1
    hide text with dissolve
    return

# To generate random number for random card selection

label card_picker:
    $ card_picked = renpy.random.randint(1, 4)
    return

# Picked 3 random cards for the player option attack

label player_card_randomizer:
    $ card_amount = 3
    $ counter = 0

    # To loop 3 times and convert each random number to valid card
    # Each coverted valid card is stored in the player cards

    while counter < card_amount:
        call card_picker from _call_card_picker_1
        if card_picked == 1:
            $ player_cards_drawn[counter] = "rock"
        elif card_picked == 2:
            $ player_cards_drawn[counter] = "paper"
        else:
            $ player_cards_drawn[counter] = "scissors"
        $ counter += 1

    return

# To display the cards for player option

screen choose_cards:
    
    vbox:
        xalign 0.5
        yalign 0.9
        text "Choose card" at center
        hbox: 
            imagebutton:
                idle "[player_cards_drawn[0]]_idle.png"
                action Return(player_cards_drawn[0])
            imagebutton:
                idle "[player_cards_drawn[1]]_idle.png"
                action Return(player_cards_drawn[1])
            imagebutton:
                idle "[player_cards_drawn[2]]_idle.png"
                action Return(player_cards_drawn[2])

# To display the current money of the player

screen show_money:
    text "Current money: [money]":
        xalign 0.5
        yalign 0.1