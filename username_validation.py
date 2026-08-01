"""
Username Validation
Have the function CodelandUsernameValidation(str) take the str parameter being passed and determine if the string is a valid username according to the following rules:

1. The username is between 4 and 25 characters.
2. It must start with a letter.
3. It can only contain letters, numbers, and the underscore character.
4. It cannot end with an underscore character.

If the username is valid then your program should return the string true, otherwise return the string false.
Examples
Input: "aa_"
Output: false
Input: "u__hello_world123"
Output: true

"""

import re

def CodelandUsernameValidation(username: str):
    """
    Validates username
    """
    #  The username is between 4 and 25 characters
    # It must start with a letter
    # It cannot end with an underscore character
    if (not (4 <= len(username) <= 25)) or username[-1:] == "_" or (not username[0].isalpha()):
        return False

    # It can only contain letters, numbers, and the underscore character.
    pattern = re.compile(r"[a-zA-Z0-9_]*")
    matched = pattern.match(username)
    if matched and (matched.span()[1] < len(username)):
        return False

    return True


if __name__ == "__main__":
    print(CodelandUsernameValidation("aa_"))
    print(CodelandUsernameValidation("u__hello_world123"))
