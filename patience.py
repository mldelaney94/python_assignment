""" Edited by Matthew Delaney. Simulates a game of 'patience', whereby the
player has 52 facedown cards organised in a circle of stacks of 4, with a stack
of 4 in the centre """

from random import seed, shuffle

CARD_TO_UNICODE = {
        'S1': chr(0x1F0A1), 'S2': chr(0x1F0A2), 'S3': chr(0x1F0A3),
        'S4': chr(0x1F0A4), 'S5': chr(0x1F0A5), 'S6': chr(0x1F0A6),
        'S7': chr(0x1F0A7), 'S8': chr(0x1F0A8), 'S9': chr(0x1F0A9),
        'S10': chr(0x1F0AA), 'Sj': chr(0x1F0AB), 'Sq': chr(0x1F0AD),
        'Sk': chr(0x1F0AE),
        'H1': chr(0x1F0B1), 'H2': chr(0x1F0B2), 'H3': chr(0x1F0B3),
        'H4': chr(0x1F0B4), 'H5': chr(0x1F0B5), 'H6': chr(0x1F0B6),
        'H7': chr(0x1F0B7), 'H8': chr(0x1F0B8), 'H9': chr(0x1F0B9),
        'H10': chr(0x1F0BA), 'Hj': chr(0x1F0BB), 'Hq': chr(0x1F0BD),
        'Hk': chr(0x1F0BE),
        'D1': chr(0x1F0C1), 'D2': chr(0x1F0C2), 'D3': chr(0x1F0C3),
        'D4': chr(0x1F0C4), 'D5': chr(0x1F0C5), 'D6': chr(0x1F0C6),
        'D7': chr(0x1F0C7), 'D8': chr(0x1F0C8), 'D9': chr(0x1F0C9),
        'D10': chr(0x1F0CA), 'Dj': chr(0x1F0CB), 'Dq': chr(0x1F0CD),
        'Dk': chr(0x1F0CE),
        'C1': chr(0x1F0D1), 'C2': chr(0x1F0D2), 'C3': chr(0x1F0D3),
        'C4': chr(0x1F0D4), 'C5': chr(0x1F0D5), 'C6': chr(0x1F0D6),
        'C7': chr(0x1F0D7), 'C8': chr(0x1F0D8), 'C9': chr(0x1F0D9),
        'C10': chr(0x1F0DA), 'Cj': chr(0x1F0DB), 'Cq': chr(0x1F0DD),
        'Ck': chr(0x1F0DE)
        }

def generate_dial_and_centre(for_seed):
    """ Randomly generates a deck of cards and arranges it into 13 bundles """
    colours = 'CDHS' # Clubs, Diamonds, Hearts, Spades
    #                                            jacks, queens, kings
    ranks = list(str(x) for x in range(1, 11)) + list('jqk')
    seed(for_seed)
    cards = [colour + rank for colour in colours for rank in ranks]
    shuffle(cards)
    dial = dict.fromkeys(range(1, 13))
    for i in range(12):
        dial[i + 1] = [cards[i + 13 * j] for j in range(4)]
    return dial, [cards[12 + 13 * j] for j in range(4)]

def initial_hour(hour, dial):
    """ Prints cards from dial using key hour """
    for card in dial[hour]:
        print('hidden'+CARD_TO_UNICODE[card], end=' ')
    # REPLACE PASS ABOVE WITH YOUR CODE

def hour_after_playing_from_beginning_for_at_most(hour, nb_of_steps, dial,
                                                  centre):
    curr_pos = 13
    revealed_cards = set()
    for i in range(nb_of_steps):
        old_pos = curr_pos
        curr_card = get_card(curr_pos, dial, centre)
        old_num_revealed_cards = len(revealed_cards)
        revealed_cards.add(curr_card)
        curr_num_revealed_cards = len(revealed_cards)
        if old_num_revealed_cards == curr_num_revealed_cards:
            return -1
        curr_pos = find_where_to_place_card(curr_card)
        dial, centre = place_card(curr_pos, dial, centre, curr_card)

    dial_to_string(hour, dial, centre, revealed_cards)

def kings_at_end_of_game(dial, centre):
    result = hour_after_playing_from_beginning_for_at_most(13, 52, dial,
                                                               centre)
    if result == -1:
        if ('Hk', 'Dk', 'Ck', 'Sk') in centre:
            print(centre)
        else:
            print('No success')

    # REPLACE PRINT() ABOVE WITH YOUR CODE

# POSSIBLY DEFINE OTHER FUNCTIONS
def get_card(pos, dial, centre):
    if pos == 13:
        return centre.pop(len(centre)-1)
    return dial[pos].pop(len(dial[pos])-1)

def place_card(pos, dial, centre, card):
    if pos == 13:
        centre.insert(0, card)
    else:
        dial[pos].insert(0, card)
    return dial, centre

def find_where_to_place_card(card):
    """ returns a number corresponding to the position the card should be
    placed """
    place = card[1:]
    if place == 'j':
        place = 11
    elif place == 'q':
        place = 12
    elif place == 'k':
        place = 13
    return int(place)

def dial_to_string(hour, dial, centre, revealed_cards):
    to_print = []
    if hour == 13:
        print(centre)
        for card in centre:
            if card in revealed_cards:
                to_print.append(CARD_TO_UNICODE[card])
            else:
                to_print.append('hidden'+CARD_TO_UNICODE[card])
    else:
        print(dial[hour])
        for card in dial[hour]:
            if card in revealed_cards:
                to_print.append(CARD_TO_UNICODE[card])
            else:
                to_print.append('hidden'+CARD_TO_UNICODE[card])
    print(' '.join(to_print))

dial, centre = generate_dial_and_centre(18)
kings_at_end_of_game(dial, centre)
