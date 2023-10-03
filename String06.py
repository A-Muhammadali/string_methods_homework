def main(s):
    """
    A variable of type str is given. Check that it consists only of numbers.
    Args:
        s: str
    Returns:
        bool: answer
    """
    if s.title()==s and s.upper()==s:
        return True
    else:
        return False
print(main("55454")) 