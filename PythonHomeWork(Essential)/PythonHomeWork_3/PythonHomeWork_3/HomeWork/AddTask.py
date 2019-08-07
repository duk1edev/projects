class MyUnexpectedError(BaseException):
    print('Unexpected error ...')


try:
    print('block TRY running')
    raise MyUnexpectedError('ERROR ERROR: F_ck all i need is U.')
except MyUnexpectedError as error:
    print('You raised myclass  error: ', error)
else:
    print('block ELSE runing...')
finally:
    print('block FINALLY')
