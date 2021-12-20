def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def continue_calculations():
    while True:
        choice_ = input(msg_5)
        if choice_ == "y":
            return True
        elif not choice_ == "n":
            continue
        return False


def is_one_digit(number):
    if -10 < number < 10 and number % 1 == 0:
        return True
    return False


def check(x, y, oper):
    msg = ""
    if is_one_digit(x) and is_one_digit(y):
        msg += msg_6
    if (x == 1 or y == 1) and oper == "*":
        msg += msg_7
    if (x == 0 or y == 0) and oper in ["*", "+", "-"]:
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


def choice_confirm(res):
    if not is_one_digit(res):
        return True
    while True:
        confirmation = input(msg_10)
        if confirmation == "n":
            return False
        elif confirmation != "y":
            continue
        break
    while True:
        confirmation = input(msg_11)
        if confirmation == "n":
            return False
        elif confirmation != "y":
            continue
        break
    while True:
        confirmation = input(msg_12)
        if confirmation == "n":
            return False
        elif confirmation != "y":
            continue
        break
    return True


msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
operations = ["+", "-", "*", "/"]
memory = 0.0
while True:
    calc = input(msg_0)
    calc = calc.split()
    if calc[0] == "M":
        calc[0] = memory
    if calc[2] == "M":
        calc[2] = memory
    if not is_number(calc[0]):
        print(msg_1)
        continue
    if not is_number(calc[2]):
        print(msg_1)
        continue
    if calc[1] not in operations:
        print(msg_2)
        continue
    check(float(calc[0]), float(calc[2]), calc[1])
    if calc[1] == "+":
        result = float(calc[0]) + float(calc[2])
    elif calc[1] == "-":
        result = float(calc[0]) - float(calc[2])
    elif calc[1] == "*":
        result = float(calc[0]) * float(calc[2])
    elif calc[1] == "/" and float(calc[2]) != 0:
        result = float(calc[0]) / float(calc[2])
    else:
        print(msg_3)
        continue
    print(result)
    while True:
        choice = input(msg_4)
        if choice == "y":
            if choice_confirm(result):
                memory = result
        elif not choice == "n":
            continue
        break
    if continue_calculations():
        continue
    break
