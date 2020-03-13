from random import randint, randrange
from itertools import groupby

ONE_PAIR = 0
TWO_PAIR = 1
THREE_KIND = 2
FULL_HOUSE = 3
STRAIGHT = 4
FOUR_KIND = 5
FIVE_KIND = 6
BUST = 7

NINE = 0
TEN = 1
JACK = 2
QUEEN = 3
KING = 4
ACE = 5

def play():
    pass
    # REPLACE PASS ABOVE WITH YOUR CODE

def simulate(n):
    hand_percentage = {ONE_PAIR: 0, TWO_PAIR: 0, THREE_KIND: 0, FULL_HOUSE: 0,
                       STRAIGHT: 0, FOUR_KIND: 0, FIVE_KIND: 0}
    for i in range(n):
        hand = generate_hand()
        hand_percentage[determine_hand(hand)] += 1

    simulation_to_string(n, hand_percentage)

# DEFINE OTHER FUNCTIONS
def generate_hand():
    hand = []
    hand_dict = {NINE: '9', TEN: '10', JACK: 'Jack', QUEEN: 'Queen',
                 KING: 'King', ACE: 'Ace'}
    'King'
    for i in range(5):
        hand.append(hand_dict[randrange(NINE, ACE)])

    return hand

def determine_hand(dice):
    straight_1 = {'Ace', 'King', 'Queen', 'Jack', '10'}
    straight_2 = {'King', 'Queen', 'Jack', '10', '9'}
    if set(dice) == straight_1 or set(dice) == straight_2:
        return STRAIGHT

    num_unique_results = 0
    possible_three_kind = 0
    for result, num_results in groupby(sorted(dice)):
        s = len(list(num_results))
        if s == 5:
            return FIVE_KIND
        elif s == 4:
            return FOUR_KIND
        elif s == 3:
            possible_three_kind = 1
        num_unique_results += 1
    if num_unique_results == 2:
        return FULL_HOUSE
    elif num_unique_results == 3 and possible_three_kind == 1:
        return THREE_KIND
    elif num_unique_results == 4:
        return ONE_PAIR
    elif num_unique_results == 5:
        return BUST
    else:
        return TWO_PAIR

def simulation_to_string(n, results):
    results_fivekind = 100 * (results[FIVE_KIND] / n)
    results_fourkind = 100 * (results[FOUR_KIND] / n)
    results_threekind = 100 * (results[THREE_KIND] / n)
    results_twopair = 100 * (results[TWO_PAIR] / n)
    results_onepair = 100 * (results[ONE_PAIR] / n)
    results_straight = 100 * (results[STRAIGHT] / n)
    results_fullhouse = 100 * (results[FULL_HOUSE] / n)
    print("Five of a kind : " + '%.2f' % results_fivekind + "%")
    print("Four of a kind: " + '%.2f' % results_fourkind + "%")
    print("Full house: " + '%.2f' % results_fullhouse + "%")
    print("Straight: " + '%.2f' % results_straight + "%")
    print("Three of a kind: " + '%.2f' % results_threekind + "%")
    print("Two pair: " + '%.2f' % results_twopair + "%")
    print("One pair: " + '%.2f' % results_onepair + "%")

simulate(1000000)
