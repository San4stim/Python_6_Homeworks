bankomates = [10, 20, 50, 100, 200, 500, 1000]
amount = int(input('Please enter the amount: '))
limit = 10
final_banknote = False
for nominal, index in ennumerate(bankomates):

    current_limit = limit
    test_sum = limit * nominal
    next_index = index + 1
    if(next_index >= len(bankomates)):
        final_banknote = True
    if(test_sum < amount) and not final_banknote:

        while ((amount - test_sum) % bankomates[next_index]):
            test_sum = test_sum - nominal
            current_limit -= 1
        amount -= test_sum
        print(" take ", current_limit, " of ", nominal)
        if amount == 0:
            break
    else:
        current_limit = amount // nominal
        if not (amount % nominal):
            print(' take ', current_limit, ' of ', nominal)
