
image bg intro = "bg_intro.jpg"
image user_picked_card = "[user_card]_idle.png"
image opponent_picked_card = "[opponent_card]_idle.png"

# The game starts here.

label start:

    scene bg intro

    call variables

    show screen show_money

    menu start_menu:
        "Start":
            jump gameplay
        "Reset Level":
            $ level = 1
            call show_text("Level Reseted")
            jump start_menu
        "Reset Game":
            $ level = 1
            $ money = 2000
            call show_text("Game Reseted")
            jump start_menu

    return

label variables:
    $ user_card = " "
    $ opponent_card = " "
    $ level = 1
    $ winner = " "
    $ money = 2000
    $ beat = 0
    return

label gameplay:

    hide user_picked_card
    hide opponent_picked_card 
    
    $ text = level
    $ user_card = " "
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

label beat_menu:
    menu:
        "Beat [beat]":
            if money-beat >= 0:
                $ money -= beat
                return
            else:
                call show_text("You don't have enough balance")
                jump gameplay
        "Main menu":
            jump start_menu


label level_1:

    call show_text("Level 1")

    $ beat = 100
    call beat_menu
    
    jump play_round
    
label level_2:
    call show_text("Level 2")

    $ beat = 200 
    call beat_menu

    jump play_round

label level_3:
    call show_text("Level 3")

    $ beat = 300 
    call beat_menu

    jump play_round

label level_4:
    call show_text("Level 4")

    $ beat = 400 
    call beat_menu

    jump play_round

label level_5:
    call show_text("Level 5")

    $ beat = 500 
    call beat_menu

    jump play_round

label level_6:
    call show_text("Level 6")

    $ beat = 600
    call beat_menu

    jump play_round

label level_7:
    call show_text("Level 7")

    $ beat = 700
    call beat_menu

    jump play_round
    
label play_round:

    $ user_card = renpy.call_screen("choose_cards")

    call opponent_card_number_picker
    
    if opponent_card_number == 1:
        $ opponent_card = "rock"
    elif opponent_card_number == 2:
        $ opponent_card = "paper"
    else:
        $ opponent_card = "scissors"

    while True:
        
        # For deciding winner

        if user_card == opponent_card:
            $ winner = "tie"
        elif user_card == "rock":
            if opponent_card == "scissors":
                $ winner = "user"
            else:
                $ winner = "opponent"
        elif user_card == "paper":
            if opponent_card == "rock":
                $ winner = "user"
            else:
                $ winner = "opponent"
        elif user_card == "scissors":
            if opponent_card == "paper":
                $ winner = "user"
            else:
                $ winner = "opponent"

        # For displaying players card
        
        call show_choosen_card
        
        # To handle winner        

        if winner == "user":
            call show_text("You win")
            $ level += 1
            $ money += beat

            # To handle end level winner
            # Reset game and money to start at the beggining

            if level > 7:
                call show_text("Congratiolations! You beat the game")
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
                call show_text("You lose")
            else:
                $ money += beat
                call show_text("Tie")

            menu:
                "Play Again":
                    jump gameplay
                "Main menu":
                    $ level = 1
                    jump start_menu

label show_choosen_card:
    show user_picked_card with dissolve:
        xalign 0.3
        yalign 0.5
    show opponent_picked_card with dissolve:
        xalign 0.7
        yalign 0.5
    pause 1
    hide user_picked_card
    hide opponent_picked_card 
    return
    


label show_text(text):
    show text "[text]" at truecenter with dissolve
    pause 1
    hide text with dissolve
    return

label opponent_card_number_picker:
    $ opponent_card_number = renpy.random.randint(1, 4)
    return

screen choose_cards:
    
    vbox:
        xalign 0.5
        yalign 0.9
        spacing 30
        text "Choose card" at center
        hbox: 
            spacing 50
            imagebutton:
                idle "rock_idle.png"
                hover "rock_hover.png"
                action Return("rock")
            imagebutton:
                idle "paper_idle.png"
                hover "paper_hover.png"
                action Return("paper")
            imagebutton:
                idle "scissors_idle.png"
                hover "scissors_hover.png"
                action Return("scissors")

screen show_money:
    text "Current money: [money]":
        xalign 0.5
        yalign 0.1