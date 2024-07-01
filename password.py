'Task 3:Build a tool that assesses the strength of a password based on criteria such as length,'
'presence of uppercase and lowercase letters, numbers, and special characters. Provide feedback to users on the passwords strength.'

import re

def check_password_complexity(password):
    length = len(password) >= 8
    uppercase = bool(re.search(r'[A-Z]', password))
    lowercase = bool(re.search(r'[a-z]', password))
    digit = bool(re.search(r'\d', password))
    specialcharacter = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    if length and uppercase and lowercase and digit and specialcharacter:
        return "Strong password!"
    else:
        feedback = "Weak password!!! \n"
        if not length:
            feedback += "- Ensure the password is at least 8 characters long \n"
        if not uppercase:
            feedback += "- Include at least one uppercase letter \n"
        if not lowercase:
            feedback += "- Include at least one lowercase letter \n"
        if not digit:
            feedback += "- Include at least one digit \n"
        if not specialcharacter:
            feedback += "- Include at least one special character \n"

        return feedback
    
    
password = input("Enter your password: ")
result = check_password_complexity(password)
print(result)


