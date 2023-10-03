def main(s):
    """
    A variable of type str is given. Check that it consists of letters only.
    Args:
        s: str
    Returns:
        bool: answer
    """
    if s.count("1")==0 and s.count("2")==0 and s.count("3")==0 and s.count("4")==0 and s.count("5")== 0 and s.count("6")==0 and s.count("7")==0 and s.count("8")==0 and s.count("9")==0 and s.count("0")==0 :
        return True
    else:
        return False 
print(main("aaaaa"))