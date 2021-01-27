#Python operators
a=10
b=20
print(a+b)
a="python"
b="is a high level programmng language"
print(a+b)

    #Global and  local variables
def f():
    global s
    print(s)
    s="This is a local variable"
    print(s)
    
#Global scope    
    
s="This is a global variable"
f()
print(s)

    
    