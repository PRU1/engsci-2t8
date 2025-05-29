def display_current_value():
    global value
    print(value)

def add(to_add):
    global value
    value += to_add

def minus(to_sub):
    global value
    value -= to_sub

def mult(to_mult):
    global value
    value *= to_mult

def div(to_div):
    global value
    value /= to_div

def undo():
    global value
    global values
    print(values)
    if len(values) > 1:
        values.pop() # undoing is non reversable
        value = values[-1]
        # take make it reversible, have a global index variable
    else:
        print("no undo possible")
    print("after pop" , values)

def undo2():
    global value
    global values
    print(values)
    if len(values) > 2:
        values.pop() # undoing is non reversable
        values.pop()
        value = values[-1]
        # take make it reversible, have a global index variable
    else:
        print("undo2 not possible")
    print("after pop" , values)


    
if __name__=="__main__":
    value = float(0)
    values = [0] # memory of calculator.  
    print("Welcome to the calculator program")
    print("Current value: ", value)
    while True:
        sign = str(input()) # not having char data type is wack :(
        match sign[0]:
            case '+':
                temp=sign.replace('+','')
                add(float(temp))
                values.append(value)
            case '-':
                temp=sign.replace('-','')
                minus(float(temp))
                values.append(value)
            case '*':
                temp=sign.replace('*','')
                mult(float(temp))
                values.append(value)
            case '/':
                temp=sign.replace('/','')
                div(float(temp))
                values.append(value)
            case '#':
                undo()
            case'&':
                undo2()
        display_current_value()