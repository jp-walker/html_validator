#!/bin/python3


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant
    to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the input
    string, stripping out all text not contained within angle brackets.


    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''

    result = []
    start = "<"
    end = ">"

    for i in range(len(html)):
        if html[i] == start:
            for e in range(1, len(html) - i):
                if html[i + e] == end:
                    result.append(html[i:i + e + 1])
                elif html[i + e] == start:
                    break

    return result

print("extract tags", _extract_tags('this is a <strong< test'))

def validate_html(html):
    '''
    This function performs a limited version of html validation by checking
    whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

    stack = []
    just_tags = _extract_tags(html)
    for e in just_tags:
        if stack != [] and stack[-1] == (e[0:1] + e[2:]):
            stack.pop()
        else:
            stack.append(e)

    if stack == [] and len(just_tags) > 0:
        return True
    else:
        return False

print("validate html", validate_html('this is a <strong< test'))
    # HINT:
    # use the _extract_tags function below to generate a list of html tags
    # without any extra text;then process these html tags using the balanced
    # parentheses algorithm from the class/book
    # the main difference between your code and the code from class will be
    # that you will have to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags
