def main():
    try:
        raise ValueError('value is incorrect')
    except ValueError as error:
        print("Exception: ",error)
        raise


try:
   main()
except ValueError:
    print('Value errror detected')
