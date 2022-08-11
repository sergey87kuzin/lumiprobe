from collections import Counter


def counter(input_string: str):
    if not input_string.isalpha():
        result = ('wrong', 'input')
        return result

    loop_string = input_string.casefold()
    result = Counter(loop_string).most_common(1)[0]
    if result[0] not in input_string:
        result = (result[0].upper(), result[1])
    return result


if __name__ == '__main__':
    string1 = 'aaaAAAbc'
    string2 = 'AAAAAAbc'
    string3 = 'cbAAAaaa'
    string4 = 'c qwerty'
    string5 = 'ababababababa'
    string6 = '6asdfgh'
    assert(counter(string1) == ('a', 6))
    assert(counter(string2) == ('A', 6))
    assert(counter(string3) == ('a', 6))
    assert(counter(string4) == ('wrong', 'input'))
    assert(counter(string5) == ('a', 7))
    assert(counter(string6) == ('wrong', 'input'))
