class Horse:
    def run(self):
        print ("i'm running")

class Bird:
    def fly(self):
        print("i'm fying")

class Pegasus(Horse,Bird):
    pass



def main():
    pegasus = Pegasus()
    pegasus.run()
    pegasus.fly()

if __name__ == '__main__':
    main()