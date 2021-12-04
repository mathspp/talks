def swap_case(string):
    result = ""
    for i in range(len(string)):
        if string[i].upper() == string[i]:
            result += string[i].lower()
        else:
            result += string[i].upper()
    return result

# ↓ refactor the for loop.

def swap_case(string):
    result = ""
    for char in string:
        if char.upper() == char:
            result += char.lower()
        else:
            result += char.upper()
    return result

# ↓ write a conditional expression

def swap_case(string):
    result = ""
    for char in string:
        result += char.lower() if char.upper() == char else char.upper()
    return result

# ↓ use an appropriate string method

def swap_case(string):
    result = ""
    for char in string:
        result += char.lower() if char.isupper() else char.upper()
    return result

# ↓ replace with a list comprehension

def swap_case(string):
    return "".join([
        char.lower() if char.isupper() else char.upper() for char in string
    ])

# ↓ use THE appropriate string method

swap_case = str.swapcase
