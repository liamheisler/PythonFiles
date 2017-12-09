import random as r

cardMin = 1
cardMax = 11 #ACE, HIGHEST

playerA_score = 0
playerB_score = 0

rangeMin = 1
rangeMax = 52

war_count = 0

#while True:
for i in range(rangeMin, (int(rangeMax + 1))):
    playerA_draw = r.randint(cardMin, cardMax)
    playerB_draw = r.randint(cardMin, cardMax)
    
    if playerA_draw == playerB_draw:
        war_count = war_count + 1
        playerA_WARdraw = r.randint(cardMin, cardMax)
        playerB_WARdraw = r.randint(cardMin, cardMax)

        if playerA_WARdraw > playerB_WARdraw:
            playerA_score = playerA_score + 3
            strA = str(playerA_score)
            print('Player A wins the WAR! Player A current score: ' + strA)
        else:
            playerB_score = playerB_score + 3
            strB = str(playerB_score)
            print('Player B wins the WAR! Player B current score: ' + strB)
    else:
        if playerA_draw > playerB_draw:
            playerA_score = playerA_score + 1
            stringedA_score = str(playerA_score)
            print('Player A wins! Player A current score: ' + stringedA_score) 
        elif playerA_draw < playerB_draw:
            playerB_score = playerB_score + 1
            stringedB_score = str(playerB_score)
            print('Player B wins! Player B current score: ' + stringedB_score) 

print('')
print('---------| WIN TOTALS |---------')
print('Player A: ' + str(playerA_score))
print('Player B: ' + str(playerB_score))
print('WAR count: ' + str(war_count))

if (playerA_score > playerB_score):
    playerA_percent = (playerA_score / rangeMax) * 100
    playerA_rnd = round(playerA_percent, 1)
    stringedA_perc = str(playerA_rnd)
    print('Player A wins with a win percentage of ' + stringedA_perc + '%!')
elif (playerB_score > playerA_score):
    playerB_percent = (playerB_score / rangeMax) * 100
    playerB_rnd = round(playerB_percent, 1)
    stringedB_perc = str(playerB_rnd)
    print('Player B wins with a win percentage of ' + stringedB_perc + '%!')
else:
    print('It is a tie! Try again!')
