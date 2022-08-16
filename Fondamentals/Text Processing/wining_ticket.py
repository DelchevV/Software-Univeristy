ticket = input()
ticket = ticket.replace(" ", "")
tickets = ticket.split(",")


def valid_ticket(lottery_ticket):
    if len(lottery_ticket) == 20:
        return True
    return False


def winning_ticket(lottery_ticket):
    valid_symbol = ["@", "#", "$", "^"]
    left_side=lottery_ticket[:10]
    right_side=lottery_ticket[10:]
    for symbol in valid_symbol:
        for repetition in range(10,5,-1):
            current_repetition=symbol*repetition
            if current_repetition in left_side and current_repetition in right_side:
                if repetition==10:
                    return f'ticket "{lottery_ticket}" - {repetition}{symbol} Jackpot!'
                return f'ticket "{lottery_ticket}" - {repetition}{symbol}'
    return f'ticket "{lottery_ticket}" - no match'


for tick in tickets:
    if valid_ticket(tick):
        print(winning_ticket(tick))
    else:
        print("invalid ticket")


