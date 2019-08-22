import os.path
try:
    file = open(os.path.join('data', 'somedata.txt'))
    print(file.read())
finally:
    file.close()