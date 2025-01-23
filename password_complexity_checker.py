import re

def check_password_strength(password):
    """Check password strength and return criteria status and score."""
    strength_criteria = {
        "Length (at least 8 characters)": len(password) >= 8,
        "Uppercase letter": bool(re.search(r'[A-Z]', password)),
        "Lowercase letter": bool(re.search(r'[a-z]', password)),
        "Number": bool(re.search(r'\d', password)),
        "Special character": bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    }

    strength_score = sum(strength_criteria.values())

    return strength_score, strength_criteria

def display_criteria(criteria):
    """Display criteria status."""
    print("\nCriteria Breakdown:")
    for crit, met in criteria.items():
        print(f"{crit}: {'✔️' if met else '❌'}")

def main():
    print(" Password Complexity Checker ")
    print("Your password must meet at least 3 out of 5 rules.\n")

    while True:
        password = input("\nEnter your password: ")
        score, criteria = check_password_strength(password)
        
        display_criteria(criteria)
        print(f"\nYour password met {score}/5 criteria.")
        
        if score >= 3:
            print("\n✅ Password Accepted! ")
            break
        else:
            print("\n❌ Password is too weak. Please try again and meet at least 3 criteria.")

if _name_ == "_main_":
    main()
