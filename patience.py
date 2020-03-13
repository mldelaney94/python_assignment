from random import seed, shuffle


def generate_dial_and_centre(for_seed):
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
    pass
    # REPLACE PASS ABOVE WITH YOUR CODE

def hour_after_playing_from_beginning_for_at_most(hour, nb_of_steps, dial,
                                                  centre
                                                 ):
    print()
    # REPLACE PRINT() ABOVE WITH YOUR CODE

def kings_at_end_of_game(dial, centre):
    print()
    # REPLACE PRINT() ABOVE WITH YOUR CODE

# POSSIBLY DEFINE OTHER FUNCTIONS
