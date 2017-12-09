import time as t

def find_war_winner(playerA_in, playerB_in):
    if playerA_in == playerB_in:
        #war_count = war_count + 1
        
        print('You hit a war!') 
        playerA_WARdraw = input('Player A, enter a new number: ')
        playerB_WARdraw = input('Player B, enter a new number: ')

        if playerA_WARdraw > playerB_WARdraw:
            print(pA_name + ' wins the WAR! Awesome work!')
        else:
            print(pB_name + ' wins the WAR! Awesome work!')
    else:
        if playerA_in > playerB_in:
            print(pA_name + ' wins! Congratulations!') 
        elif playerA_in < playerB_in:
            print(pB_name + ' wins! Congratulations!') 

sleep_time = 1.0
playingChoice = True;

while playingChoice == True:
    print(str(playingChoice))
    print('--------| WELCOME TO WAR | --------')
    t.sleep(sleep_time)
    print('Viable entries for card numbers: 2 - 11')
    t.sleep(sleep_time)
    print('The winner will be notified!')
    t.sleep(sleep_time)
    print('--------| GOODLUCK | --------')
    print('')

    pA_name = input('Player A, please enter your name: ')
    pB_name = input('Player B, please enter your name: ')

    t.sleep(sleep_time)
    print('')
    t.sleep(sleep_time)
    print('--------| Hello, I wish  you luck! | --------')
    t.sleep(sleep_time)
    print('')
    t.sleep(sleep_time)

    playerA_entry = input(pA_name + ', enter your card number: ')
    if (int(playerA_entry) < 2) | (int(playerA_entry) > 11):
        t.sleep(sleep_time)
        print('Enter a new number, out of bonds!')
        print('')
        t.sleep(sleep_time)
        playerA_entry = input(pA_name + ', enter your card number: ')
    t.sleep(sleep_time)
    print('Entry stored. Thank you, ' + pA_name + '!')
    print('')
    
    playerB_entry = input(pB_name + ', enter your card number: ')
    if (int(playerB_entry) < 2) | (int(playerB_entry) > 11):
        t.sleep(sleep_time)
        print('Enter a new number, out of bonds!')
        print('')
        t.sleep(sleep_time)
        playerA_entry = input(pB_name + ', enter your card number: ')
    t.sleep(sleep_time)
    print('Entry stored. Thank you, ' + pB_name + '!')
    print('')

    t.sleep(sleep_time)
    print('Calculating result...')
    t.sleep(sleep_time)
    print('...please wait...')
    t.sleep(sleep_time)
    print('')

    find_war_winner(playerA_entry, playerB_entry)

    print('')
    t.sleep(sleep_time)
    print('--| Thank you for playing! Would you like to play again? |--')
    t.sleep(sleep_time)
    print('Options: yes or no!')
    print('')

    t.sleep(sleep_time)
    choice = input('Would you like to play again? Enter your choice: ')
    print(str(choice))
    print('')
    if choice == 'no':
        playingChoice = False;
        t.sleep(sleep_time)
        print('Thank you for playing!')
        t.sleep(sleep_time)
        print('--------| GOODBYE | --------')
        exit()
