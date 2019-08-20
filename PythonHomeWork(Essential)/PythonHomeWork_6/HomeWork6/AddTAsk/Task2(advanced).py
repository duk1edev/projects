from flask import Flask 



@app.route('/',methods=['GET','POST'])
def create_link():
    """Контроллер создания новой ссылки
    """
    error_message = None
    name = ''
    url = 'http://'
    success_message = None

 
if __name__ == '__main__':
    app.run('0.0.0.0',8000)
