class GraphicalObject(object):

    def click(self):
        try:
            self.on_click()
        except AttributeError:
            print(self.__class__.__name__,'is not clickable')

class Rectangle(GraphicalObject):
    def __init__(self, width, heigth, text = ''):
        super().__init__()

        self.width  = width
        self.heigth = heigth
        self.text = text
    def draw(self):
        if self.text:
            padded_text = ' ' + self.text + ''
        else:
            padded_text = self.text
        padded_text_len = len(padded_text)
        
        left_padding = round((self.width - padded_text_len)/2)
        left = '*' * left_padding
        rigth = '*' * (self.width - left_padding - padded_text_len)

        for i in range(self.heigth):
            if i == round(self.heigth/2):
                print(left,padded_text,rigth,sep='')
            else:
                print('*'*self.width)

class Clickable(object):
    """Обработчик нажатия мыши
    """
    def on_click(self):
        print(self.__class__.__name__,'clicked')

class Button(Rectangle,Clickable):
    def __init__(self, width = 25, heigth = 5, text = None):
        if text is None:
            text = self.__class__.__name__
        super().__init__(width,heigth,text)


def main():
    rect = Rectangle(20,5)
    rect.draw()
    rect.click()

    print()

    button = Button(text = 'Duk1eDev')
    button.draw()
    button.click()

if __name__ == '__main__':
    main()