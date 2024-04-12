import re

def check_password_complexity(password):
    # Define criteria for a strong password
    min_length = 8
    has_lowercase = bool(re.search(r'[a-z]', password))
    has_uppercase = bool(re.search(r'[A-Z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?\/\\]', password))

    # Evaluate password based on criteria
    complexity_score = 0
    if len(password) >= min_length:
        complexity_score += 1
    if has_lowercase:
        complexity_score += 1
    if has_uppercase:
        complexity_score += 1
    if has_digit:
        complexity_score += 1
    if has_special:
        complexity_score += 1

    return complexity_score

def main():
    while True:
        password = input("Enter your password: ")
        complexity_score = check_password_complexity(password)

        # Provide feedback to the user
        if complexity_score == 5:
            print("Strong password! 👍")
            break
        elif complexity_score >= 3:
            print("Moderate password. Consider adding more complexity. 🔒")
        elif complexity_score >= 1:
            print("Weak password. Please choose a stronger password. ⚠️")
        else:
            print("Password does not meet minimum complexity requirements. Please try again. ❌")

if __name__ == "__main__":
    main()
