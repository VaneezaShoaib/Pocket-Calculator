#Vaneeza Shoaib ZHW9ZC

current = 0
recent_operator = ""
recent_integer = 0
series_of_operations = "0"

def get_value(): # getting current value in calculator
    global current
    return current

def clear(optional=0): #setting current value to 0
    global recent_operator
    global recent_integer
    global current
    global series_of_operations
    recent_operator = ""
    recent_integer = 0
    current = optional
    series_of_operations = str(current)
    return current # return current int value

def step(O,N):
    global current
    global recent_operator
    global series_of_operations
    global recent_integer
    recent_operator = O
    recent_integer = N # assign local paraemter to global variable
    helper()
    if O == "+":
        current = current + N
    elif O == "-":
        current = current - N
    elif O == "*":
        current = current * N
    elif O == "//":
        current = current // N
    return current

def helper():
    global current
    global recent_operator
    global series_of_operations
    series_of_operations = "(" + str(series_of_operations) +")" + str(recent_operator) + str(recent_integer)
    return series_of_operations

def repeat():
    global recent_operator
    global recent_integer
    global current
    if recent_operator == "":
        return current
    else:
        current = step(recent_operator, recent_integer)
        return current

def get_expr():
    global series_of_operations
    return series_of_operations