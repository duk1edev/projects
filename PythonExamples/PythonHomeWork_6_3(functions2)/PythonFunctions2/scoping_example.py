var = "global variable"

def function():
    global var 
    var = "new global variable"
    print(var)

function()
print(var)