""" Simulates games of poker dice, where the dice have no suits, and only
NINE through ACE is possible. Written Matthew Delaney March 2020 """

from random import randrange
from itertools import groupby

ONE_PAIR = 0
TWO_PAIR = 1
THREE_KIND = 2
FULL_HOUSE = 3
STRAIGHT = 4
FOUR_KIND = 5
FIVE_KIND = 6
BUST = 7

ACE = 0
KING = 1
QUEEN = 2
JACK = 3
TEN = 4
NINE = 5

def play():
    """ Simulates single-player dice rolling """
    result_dict = {ONE_PAIR: 'One pair', TWO_PAIR: 'Two pair',
                   THREE_KIND: 'Three of a kind', FULL_HOUSE: 'Full house',
                   STRAIGHT: 'Straight', FOUR_KIND: 'Four of a kind',
                   FIVE_KIND: 'Five of a kind'}
    turn_dict = {2: 'second', 3: 'third'}

    hand = generate_hand(5)
    for i in range(2, 4):
        print("The roll is: " + ' '.join(hand))
        print("It is a " + result_dict[determine_hand(hand)])
        keep_list = input('Which dice do you want to keep for the ' +
                          turn_dict[i] + ' roll? ').split()

        while not legal_keep_list(keep_list, hand):
            print('That is not possible, try again!')
            keep_list = input('Which dice do you want to keep for the ' +
                              turn_dict[i] + ' roll? ').split()

        if len(keep_list) == 0:
            hand = generate_hand(5)
        elif 'all' in keep_list or 'All' in keep_list:
            print("Ok, done.")
            return
        else:
            keep_list.extend(generate_hand(5-len(keep_list)))
            hand = keep_list

    print("The roll is: " + ' '.join(hand))
    print("It is a " + result_dict[determine_hand(hand)])
    return

def simulate(n):
    """ Over n simulations, counts number of hands of each rank, and prints
    statistical information about their occurrences"""
    hand_percentage = {ONE_PAIR: 0, TWO_PAIR: 0, THREE_KIND: 0, FULL_HOUSE: 0,
                       STRAIGHT: 0, FOUR_KIND: 0, FIVE_KIND: 0}
    for i in range(n):
        hand = generate_hand(5)
        hand_percentage[determine_hand(hand)] += 1

    simulation_to_string(n, hand_percentage)

# DEFINE OTHER FUNCTIONS
def generate_hand(num_cards):
    """ generates a list num_cards long of random cards """
    hand = []
    hand_dict = {NINE: '9', TEN: '10', JACK: 'Jack', QUEEN: 'Queen',
                 KING: 'King', ACE: 'Ace'}

    for i in range(num_cards):
        hand.append(hand_dict[randrange(ACE, NINE)])

    return hand

def determine_hand(dice):
    """ Determines the rank of a legal hand """
    straight_1 = {'Ace', 'King', 'Queen', 'Jack', '10'}
    straight_2 = {'King', 'Queen', 'Jack', '10', '9'}
    if set(dice) == straight_1 or set(dice) == straight_2:
        return STRAIGHT

    num_unique_results = 0
    possible_three_kind = 0
    for result, groupby_obj in groupby(sorted(dice)):
        s = len(list(groupby_obj))
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
    """ Prints the results of the simulation """
    results_fivekind = 100 * (results[FIVE_KIND] / n)
    results_fourkind = 100 * (results[FOUR_KIND] / n)
    results_threekind = 100 * (results[THREE_KIND] / n)
    results_twopair = 100 * (results[TWO_PAIR] / n)
    results_onepair = 100 * (results[ONE_PAIR] / n)
    results_straight = 100 * (results[STRAIGHT] / n)
    results_fullhouse = 100 * (results[FULL_HOUSE] / n)
    print("Five of a kind: " + '%.2f' % results_fivekind + "%")
    print("Four of a kind: " + '%.2f' % results_fourkind + "%")
    print("Full house: " + '%.2f' % results_fullhouse + "%")
    print("Straight: " + '%.2f' % results_straight + "%")
    print("Three of a kind: " + '%.2f' % results_threekind + "%")
    print("Two pair: " + '%.2f' % results_twopair + "%")
    print("One pair: " + '%.2f' % results_onepair + "%")

def legal_keep_list(keep_list, orig_hand):
    """ Determines if keep_list is a legal input """
    if len(keep_list) == 0:
        return 1
    if len(keep_list) > 5:
        return 0
    legal_alls = ['all', 'All']
    if len(keep_list) == 1 and keep_list[0] in legal_alls:
        return 1

    can_contain = ['Ace', 'King', 'Queen', 'Jack', '10', '9']
    for item in keep_list:
        if item not in can_contain or item not in orig_hand:
            return 0
    return 1

simulate(100000)
