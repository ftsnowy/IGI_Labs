import constants


def calculate(x, y, op):
    if op == constants.ADD:
        return x + y
    elif op == constants.SUB:
        return x - y
    elif op == constants.MUL:
        return x * y
    elif op == constants.DIV:
        if y == 0:
            return "Can't divide by 0"
        else:
            return x / y
    else:
        return "Invalid operator"
