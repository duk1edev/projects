MAX_STARS = 30
WIDTH = 80
def print_result(number):
    if number == 0:
        stars_count = MAX_STARS
    else:
        stars_count = round(MAX_STARS / number)
        if stars_count > MAX_STARS:
            stats_count = MAX_STARS
        
    number_field_width = WIDTH - 2 * stars_count
    stars = "*" * stars_count
    fmt = '{0}{1:^' + str(number_field_width) + '}{0}'

    print(fmt.format(stars,number))


def main():
    while True:
        try:
            first_number = float(input('First number: '))
            second_number = float(input('Second numer: '))
            result = first_number/second_number
            
        except (ValueError,ZeroDivisionError) as error:
            print('Error: ', error)
            print('Please try again')
            print()
        else:
            print_result(result)
            break


if __name__ == '__main__':
    main()
