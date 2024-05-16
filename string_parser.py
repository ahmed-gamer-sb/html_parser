def parse_string(text: str()):
    """
    check for the validity of the try:
    Meaning that each '(' should have a ')'
    """
    tstack = []
    for ch in text:
        if ch == "(":
            tstack.append(ch)
        elif ch == ")":
            "checking if the tstack is empty and the ch is ')' then this can't be closed"
            if not tstack: return False
            tstack.pop()
    if tstack:
        print("Not valid at all")
        return False
    else:
        pritn("String is valid")
        return True

