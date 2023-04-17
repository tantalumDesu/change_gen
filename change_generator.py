from random import randint, choices

def convert_gold_to_coins(gold):
    coin_values = {'pp': 1000, 'gp': 100, 'ep': 50, 'sp': 10, 'cp': 1}
    coin_counts = {'pp': 0, 'gp': 0, 'ep': 0, 'sp': 0, 'cp': 0}
    coin_weight = {'pp': .1*(randint(1,120)/100), 'gp': 5*(randint(1,120)/100), 'ep': 1*(randint(1,120)/100), 'sp': 10*(randint(1,120)/100), 'cp': 50*(randint(1,120)/100)}
    total_copper = int(gold * 100)
    while total_copper > 0:
        options = [coin for coin, value in coin_values.items() if value <= total_copper and coin_counts[coin] < (gold * 100) // value]
        if not options:
            break
        weights = [coin_weight[coin] for coin in options]
        chosen = choices(options, weights=weights)[0]
        coin_counts[chosen] += 1
        total_copper -= int(coin_values[chosen])
    output = [f"{count:,}{coin}" for coin, count in coin_counts.items() if count > 0]
    return "\n".join(output)
while True:
    while True:
        try:
            gold=float(input("\nEnter gold amount: "))
            print("")
            break
        except (ValueError, IndexError):
            print("Invalid input. Please choose a valid option.")
            continue
    print(convert_gold_to_coins(gold))