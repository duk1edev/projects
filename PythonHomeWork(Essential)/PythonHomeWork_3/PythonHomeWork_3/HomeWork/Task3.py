import datetime

MINIMAL_YEAR = 2007


class Employee(object):

    def __init__(self,name,lastname,department,initial_year):
        if not name:
            raise ValueError('first name cannot be empty')
        if not lastname:
            raise ValueError('lastname cannot be empty')
        if not department:
            raise ValueError('part cannot be empty')
        if not is_year_correct(initial_year):
            raise ValueError('incorret year: {}'.format(initial_year))

        self.name = name
        self.lastname = lastname
        self.department = department
        self.initial_year = initial_year
    def __repr__(self):
        return 'Employee ({name!r},{lastname!r},' \
               '{department!r},{initial_year!r})'.format_map(self.__dict__)
    @staticmethod
    def read_employee():
        """Статический метод для чтения нового сотрудника
        """
        name = input('Enter first name: ')
        lastname = input('Enter last name: ')
        department = input('Enter department of work:')
        year = read_year('Enter year when the worker began to work: ')
        return Employee(name,lastname,department,year)

def read_int(message,check_function=None):
    """Функция безопасного чтения числа с клавиатуры
    :param message:         поясняющее сообщение
    :param check_function:  функция предикат проверки кооректности либо None
    :return:                введенное значение
    """
    while True:
        try:
            value = int(input(message))
            if check_function and not check_function(value):
                raise ValueError('incorrect value')
        except ValueError as error:
            print('Error: ',error)
        else:
            return value

def is_year_correct(year):
    """Функция проверки коректности года
    """
    return MINIMAL_YEAR <= year <= datetime.date.today().year

def read_year(message):
    return read_int(message,is_year_correct)

def main():

    employees_count = read_int('Count of workers: ')

    employees = []

    while len(employees) < employees_count:
        try:
           employee = Employee.read_employee()
        except ValueError as error:
            print("Error: ", error)
        else:
            employees.append(employee)
        finally:
            print()

    year = read_year('Enter a year:') 

    for employee in employees:
        if  employee.initial_year >=year:
            print(employee)


if __name__ == '__main__':
    main()
