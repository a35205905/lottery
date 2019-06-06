import random

from terminaltables import AsciiTable


def print_table(text, items):
    table = AsciiTable([items])
    print(text)
    print(table.table)


def main():
    print('Game Start!')
    bet_way = input("First, choose betting way('auto' or 'user')：")
    if bet_way != 'auto' and bet_way != 'user':
        print('Wrong format, please restart lottery game!')
        exit()

    bet_numbers_set = []
    if bet_way == 'auto':
        # random by not repeating
        num = input('choose set of auto numbers you want, range by 1~20：')
        if not num.isdigit():
            print('Wrong format, enter not by numbers!')
            exit()
        elif not 1 <= int(num) <= 20:
            print('Wrong format, number range is 1~20!')
            exit()

        for i in range(int(num)):
            bet_numbers_set.append(sorted(random.sample(range(1, 50), 6)))

    elif bet_way == 'user':
        bet_numbers = input('choose six not repeating numbers, range by 1~49 (ex. 1,2,3,4,5,6)：')
        bet_numbers = bet_numbers.split(',')
        if len(bet_numbers) != 6:
            print('Wrong format, there are not six numbers!')
            exit()
        
        for bet_number in bet_numbers:
            if bet_number.isdigit() is False:
                print('Wrong format, enter not by numbers!')
                exit()
            elif not  1 <= int(bet_number) <=49:
                print('Wrong format, number range is 1~49!')
                exit()

        if len(bet_numbers) != len(set(bet_numbers)):
            print('Wrong format, number is repeating!')
            exit()

        bet_numbers = list(map(int, bet_numbers))
        bet_numbers_set.append(sorted(bet_numbers))
    
    n = 0
    for bet_numbers in bet_numbers_set:
        n += 1
        print(n, '.')
        # list int vlaue to string
        bet_numbers = list(map(str, bet_numbers))
        text = 'Your bet numbers is：'
        print_table(text, bet_numbers)

        winning_numbers = sorted(random.sample(range(1, 50), 6))
        winning_numbers = list(map(str, winning_numbers))
        text = 'Winning numbers is：'
        print_table(text, winning_numbers)

        check_numbers = []
        for bet_number in bet_numbers:
            if bet_number in winning_numbers:
                check_numbers.append(bet_number)

        english_numbers = {
            0: 'zero',
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
        }
        text = 'Your lottety is winning {} numbers'.format(english_numbers.get(len(check_numbers)))
        print_table(text, check_numbers)
        print()

    print('Game Over!')
    

if __name__ == '__main__':
    main()
