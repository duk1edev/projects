
def generate_simple_numbers():
    """ Создаем список из простых чисел до 1000000
    """
    
    end = 1000000
    
    for i in range(2,end+1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            yield i
    
     


    
   
    



  

   

   
if __name__ == '__main__':
    count = int(input('Enter n first simple numbers: '))
    index_ = 0


    for number in generate_simple_numbers():
        if index_ >= count:
            break
        else:
            print("[{0}] = {1}".format(index_,number))
            index_ += 1

    
      
    


