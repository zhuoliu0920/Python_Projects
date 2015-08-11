#!/usr/bin/env python3

import random
import cards
from functools import reduce

# hands = [c1, c2, c3, c4, c5, c6, c7], all the functions defined below are to test if it belongs to any catelog.
# output will be a tuple (test, result), test:Boolen indicates if hands pass the test, result (list) shows the result
# if pass the test, otherwise, empty test.

def straight_flush(hands):
    test = False
    result = []
    if hands == []:
        pass
    else:
        # check flush
        suits = [card.get_suit() for card in hands]
        counts_by_suits = sorted([[suits.count(s),s] for s in set(suits)], reverse=True)
        if counts_by_suits[0][0] > 4:
            max_suit = counts_by_suits[0][1]
            flush_cards = [card for card in hands if card.get_suit()==max_suit]
            # check straight
            ranks = sorted(set([card.get_rank() for card in flush_cards]), reverse=True)
            count = 0 # count for continues ranks (-1 jump)
            for i in range(len(ranks)-1):
                if ranks[i] - ranks[i+1] == 1:
                    count += 1
                else:
                    count = 0
                if count == 4:
                    test = True
                    straight_ranks = ranks[i+1-4:i+2]
                    result = [card for card in flush_cards if card.get_rank() in straight_ranks]
                    break
    return (test, result)
    

def four_of_a_kind(hands):
    test = False
    result = []
    if hands == []:
        pass
    else:
        ranks = [card.get_rank() for card in hands]
        counts_by_ranks = sorted([[ranks.count(r),r] for r in set(ranks)], reverse=True)
        if counts_by_ranks[0][0] == 4:
            test = True
            fourkind_rank = counts_by_ranks[0][1]
            # result = 4 cards of a kind and randomly picked card from other 3 cards
            result.extend([card for card in hands if card.get_rank()==fourkind_rank])
            result.append(random.choice([card for card in hands if card.get_rank()!=fourkind_rank]))
    return (test, result)

def full_house(hands):
    test = False
    result = []
    if hands == []:
        pass
    else:
        ranks = [card.get_rank() for card in hands]
        counts_by_ranks = sorted([[ranks.count(r),r] for r in set(ranks)], reverse=True)
        if (counts_by_ranks[0][0] == 3) & (counts_by_ranks[1][0] > 1):
            test = True
            threekind_rank = counts_by_ranks[0][1]
            twokind_rank = counts_by_ranks[1][1]
            # result = 3 cards of same rank and randomly picked 2 cards from the left 2 or 3 cards with same rank
            result.extend([card for card in hands if card.get_rank()==threekind_rank])
            result.extend(random.sample([card for card in hands if card.get_rank()==twokind_rank], 2))
    return (test, result)

def flush(hands):
    test = False
    result = []
    if hands == []:
        pass
    else:
        suits = [card.get_suit() for card in hands]
        counts_by_suits = sorted([[suits.count(s),s] for s in set(suits)], reverse=True)
        if counts_by_suits[0][0] > 4:
            test = True
            five_suit = counts_by_suits[0][1]
            # result = 5 cards of same suit
            result.extend(random.sample([card for card in hands if card.get_suit()==five_suit], 5))
    return (test, result)

def straight(hands):
    test = False
    result = []
    if hands == []:
        pass
    else:
        ranks = sorted(set([card.get_rank() for card in hands]), reverse=True)
        count = 0 # count for continues ranks (-1 jump)
        for i in range(len(ranks)-1):
            if ranks[i] - ranks[i+1] == 1:
                count += 1
            else:
                count = 0
            if count == 4:
                test = True
                straight_ranks = ranks[i+1-4:i+2]
                result = [random.choice([card for card in hands if card.get_rank()==sr]) for sr in straight_ranks]
                break
    return (test, result)

def three_of_a_kind(hands):
    test = False
    result = []
    if hands == []:
        pass
    else:
        ranks = [card.get_rank() for card in hands]
        counts_by_ranks = sorted([[ranks.count(r),r] for r in set(ranks)], reverse=True)
        if (counts_by_ranks[0][0] == 3) & (counts_by_ranks[0][0] == 1):
            test = True
            threekind_rank = counts_by_ranks[0][1]
            # result = 3 cards of same rank and randomly picked 2 cards from the left 4 cards with different ranks
            result.extend([card for card in hands if card.get_rank()==threekind_rank])
            result.extend(random.sample([card for card in hands if card.get_rank()!=threekind_rank], 2))
    return (test, result)

def two_pair(hands):
    test = False
    result = []
    if hands == []:
        pass
    else:
        ranks = [card.get_rank() for card in hands]
        counts_by_ranks = sorted([[ranks.count(r),r] for r in set(ranks)], reverse=True)
        if (counts_by_ranks[0][0] == 2) & (counts_by_ranks[1][0] == 2):
            test = True
            twokind_rank1 = counts_by_ranks[0][1]
            twokind_rank2 = counts_by_ranks[1][1]
            # result = 2 cards of same rank and another 2 cards with same rank, and randomly pick one card from 3 cards left
            result.extend([card for card in hands if card.get_rank()==twokind_rank1])
            result.extend([card for card in hands if card.get_rank()==twokind_rank2])
            result.extend(random.sample([card for card in hands if card.get_rank() not in [twokind_rank1,twokind_rank2]], 1))
    return (test, result)

def one_pair(hands):
    test = False
    result = []
    if hands == []:
        pass
    else:
        ranks = [card.get_rank() for card in hands]
        counts_by_ranks = sorted([[ranks.count(r),r] for r in set(ranks)], reverse=True)
        if (counts_by_ranks[0][0] == 2) & (counts_by_ranks[1][0] == 1):
            test = True
            twokind_rank = counts_by_ranks[0][1]
            # result = 2 cards of same rank and randomly picked 3 cards with different ranks
            result.extend([card for card in hands if card.get_rank()==twokind_rank])
            result.extend(random.sample([card for card in hands if card.get_rank()!=twokind_rank] , 3))
    return (test, result)

def test(hands):
    if straight_flush(hands)[0]:
        return (0, straight_flush(hands)[1])
    elif four_of_a_kind(hands)[0]:
        return (1, four_of_a_kind(hands)[1])
    elif full_house(hands)[0]:
        return (2, full_house(hands)[1])
    elif flush(hands)[0]:
        return (3, flush(hands)[1])
    elif straight(hands)[0]:
        return (4, straight(hands)[1])
    elif three_of_a_kind(hands)[0]:
        return (5, three_of_a_kind(hands)[1])
    elif two_pair(hands)[0]:
        return (6, two_pair(hands)[1])
    elif one_pair(hands)[0]:
        return (7, one_pair(hands)[1])
    else:
        return (8, hands[0:5])
    
def main():
    print("Let's play poker!\n")

    my_deck = cards.Deck() # initial the deck
    my_deck.shuffle() # shuffle cards in the deck

    while(my_deck.cards_count() >= 9):
        hand1_list=[]
        hand2_list=[]
        for i in range(2):
            hand1_list.append(my_deck.deal())
            hand2_list.append(my_deck.deal())
        comm_list=[]
        for i in range(5):
            comm_list.append(my_deck.deal())
        print("Community cards: {}".format(comm_list))
        print("Player 1: {}".format(hand1_list))
        print("Player 2: {}\n".format(hand2_list))

        # test player 1 and player 2's hands in which catelog
        hand1_list.extend(comm_list)
        hand2_list.extend(comm_list)
        catelog = ['straigt flush', '4 of a kind', 'full house', 'flush', 'straight', '3 of a kind', '2 pair', '1 pair', 'high card']
        p1 = test(hand1_list)
        p2 = test(hand2_list)
        if p1[0] < p2[0]:
            print("Player 1 wins with a {}: {}\n".format(catelog[p1[0]], p1[1]))
        elif p1[0] > p2[0]:
            print("Player 2 wins with a {}: {}\n".format(catelog[p2[0]], p2[1]))
        else:
            print("TIE with {}: {} vs {}\n".format(catelog[p1[0]], p1[1], p2[1]))

        whether_continue = str(input("Do you wish to play another hand? (Y or N)")).lower()
        print("-------------------------------------------------")
        if whether_continue == 'n':
            break

    if my_deck.cards_count() < 9:
        print("Deck has too few cards so game is done.")
        

if __name__ == "__main__":
    main()
        
