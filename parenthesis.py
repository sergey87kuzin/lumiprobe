def parenthesis(some_string):
    if not type(some_string) == str:
        return False
    result = 0
    for element in some_string:
        if element == '(':
            result += 1
        elif element == ')':
            result -= 1
        else:
            return False
        if result < 0:
            return False
    if result != 0:
        return False
    return True


if __name__ == '__main__':
    assert(parenthesis('(((())))'))
    assert(not parenthesis('(((()))'))
    assert(parenthesis('((()()))'))
    assert(not parenthesis(')(((())))'))
    assert(parenthesis('(()()())'))
    assert(not parenthesis('(((()))))'))
