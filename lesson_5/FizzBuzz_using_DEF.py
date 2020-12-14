def fizzbuzz(limit):
    saving_results = []
    for i in range(1, limit + 1):
        if i % fizz == 0 and i % buzz == 0:
            saving_results.append('FB')
        elif i % fizz == 0:
            saving_results.append('F')
        elif i % buzz == 0:
            saving_results.append('B')
        else:
            saving_results.append(i)
    return saving_results

fizz = int(input('Enter FIZZ = '))
buzz = int(input('Enter BUZZ = '))

def main():
    print(fizzbuzz(int(input('Limit of numbers = '))))
main()