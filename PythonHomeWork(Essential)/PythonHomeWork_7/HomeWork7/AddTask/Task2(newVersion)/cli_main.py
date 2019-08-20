"""Модуль консольного интерфейса приложения"""

from links_db import LinksDB


def add_link_to(links):
    """Функция добавления новой ссылки в хранилище links"""

    while True:
        short_name = input('Enter the short name: ')
        original_url = input('Enter url:')

        try:
            links.set_url(short_name, original_url)
        except (KeyError, ValueError)as error:
            print(error.args[0])
        else:
            break


def get_link_from(links):
    """Фугкция получения ссылки из хранилища links_db"""
    name = input('Enter the link name: ')
    try:
        url = links.get_url(name)
    except KeyError:
        print('Key does not exist')
    else:
        print(url)


links = LinksDB()


def main():
    """Главная функция приложения"""

    while True:
        print('1.Add link')
        print('2.Get link')
        print('3.Exit')

        choise = input(">")

        if choise == '1':
            add_link_to(links)
        elif choise == '2':
            get_link_from(links)
        elif choise == '3':
            break
        else:
            print('Incorrect input')

        print()


if __name__ == '__main__':
    main()
