"""
    islower - Function to find lowercase character.
    @c: variable to contain the character value.
    Return: If lowercase True
            Otherwise False
"""
def islower(c):
    if ord(c) in range(97, 123):
        return True
    else:
        return False
