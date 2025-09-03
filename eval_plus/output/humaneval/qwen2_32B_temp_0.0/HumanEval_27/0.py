

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return string.swapcase()

def test_flip_case():
    assert flip_case('Hello') == 'hELLO'
    assert flip_case('hELLO') == 'Hello'
    assert flip_case('HELLO') == 'hello'
    assert flip_case('hello') == 'HELLO'
    assert flip_case('') == ''
    assert flip_case('123') == '123'
    assert flip_case('!@#') == '!@#'
    assert flip_case('Hello World!') == 'hELLO wORLD!'
    assert flip_case('Hello World!123') == 'hELLO wORLD!123'
    assert flip_case('Hello World!123!@#') == 'hELLO wORLD!123!@#'
    assert flip_case('Hello World!123!@#') == 'hELLO wORLD!123!@#'
    assert flip_case('Hello World!123!@#') == 'hELLO wORLD!123!@#'
    assert flip_case('Hello World!123!@#') == 'hELLO wORLD!123!@#'
    assert flip_case('Hello World!123!@#') == 'hELLO wORLD!123!@#'
    assert flip_case('Hello World!123!@#') == 'hELLO wORLD!123!@#'
    assert flip_case('Hello World!123!@#') == 'hELLO wORLD!123!@#'
    assert flip_case('Hello World!123!@#') == 'hELLO wORLD!123!@#'
    assert flip_case('Hello World!123!@#') == 'hELLO wORLD!123!@#'
    assert flip_case('Hello World!123!@#') == 'hELLO wORLD!123!@#'
    assert flip_case('Hello World!123!@#') == 'hELLO wORLD!123!@#'
    assert flip_case('Hello World!123!@#') == 'hELLO wORLD!123!@#'
    assert flip_case('Hello World!123!@#') == 'hELLO wORLD!123!@#'
    assert flip_case('Hello World!123!@#') == 'hELLO wORLD!123!@#'
    assert flip_case('Hello World!123!@#') == 'hELLO wORLD!123!@#'
    assert flip_case('Hello World!123!@#') == 'hELLO wORLD!123!@#'
    assert flip_case('Hello World!123!@#') == 'hELLO wORLD!123!@#'
    assert flip_case('Hello World!123!@#') == 'hELLO wORLD!123!@#'
    assert flip_case('Hello World!123!@#') == 'hELLO wORLD!123!@#'
    assert flip_case('Hello World!123!@#') == '