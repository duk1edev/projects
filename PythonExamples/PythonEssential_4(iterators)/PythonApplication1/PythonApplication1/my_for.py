def my_for(itarable,callback):
    it = iter(itarable)
    while True:
        try:
            value = next(it)
            callback(value)
        except StopIteration:
            break


def loop_body(value):
    print('Next value received:',value)

my_for(range(10),loop_body)