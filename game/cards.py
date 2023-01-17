import random


def ls_to_str(ls: list):
    return str(ls)[1:-1]


def str_to_ls(string: str):
    return [int(card) for card in string.split(', ')]


def new_deck():
    return ls_to_str(list(range(1, 101)))


def distribute(deck: str, n_players: int, n_cards_per_player: int = 1):
    deck_ls = str_to_ls(deck)
    players = []
    for _ in range(n_players):
        player = random.sample(deck_ls, n_cards_per_player)  # choosing random cards for player
        deck_ls = [card for card in deck_ls if card not in player]  # removing cards from deck
        player.sort()
        players.append(ls_to_str(player))
    return {'deck': ls_to_str(deck_ls), 'players': players}


def put_smallest(cards: str):
    cards_ls = str_to_ls(cards)
    smallest = min(cards_ls)
    cards_ls.remove(smallest)
    return {'card': smallest, 'remaining': ls_to_str(cards_ls)}
