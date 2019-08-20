def add_link_to(links):

    original_url = input('Enter url: ')

    short_name = None

    while not short_name or short_name in links:
        short_name = input('Enter the shirt name: ')
        if short_name in links:
            print('This name aleady exist'
                  '(url: {}'.format(links[short_name]))

    links[short_name] = original_url


def get_link_from(links):

    name = input('Enter link name:')
    url = links.get(name,None)

    if url:
        print(url)
    else:
        print('Link does not exist')

def main():

    links = {}

    while True:
        print('1.Add link')
        print('2.Get link')
        print('3.Exit')

        choise = input('Choise: ')

        if choise == '1':
            add_link_to(links)
        elif choise == '2':
            get_link_from(links)
        elif choise == '3':
            break
        else:
            print('incorrect input')

if __name__ == '__main__':
    main()