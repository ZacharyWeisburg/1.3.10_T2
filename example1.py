####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Zach^2'
strategy_name = 'RandomBetray'
strategy_description = '2/3 chance to betray, 1/3 chance to collude'

import random
    
def move(my_history, their_history, my_score, their_score):
    x = return random.choice(1, 3)
    if x = 1 or x = 2:
        return "b"
    else:
        return "c"
