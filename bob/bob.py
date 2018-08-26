def hey(phr):

    if not phr.strip():
        return "Fine. Be that way!"
    elif phr.isupper():
        if phr.endswith('?'):
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"
    elif phr.strip().endswith('?'):
        return "Sure."
    else:
        return "Whatever."
