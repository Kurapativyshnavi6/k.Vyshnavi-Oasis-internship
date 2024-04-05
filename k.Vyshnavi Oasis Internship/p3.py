import random
import string

def generate_password(length, use_uppercase=True, use_numbers=True, use_symbols=True):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    symbols = string.punctuation if use_symbols else ''

    all_characters = lowercase_letters + uppercase_letters + numbers + symbols

    if not all_characters:
        raise ValueError("At least one character set must be enabled")

    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter the desired password length: "))
    use_uppercase = input("Use uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Use numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Use symbols? (y/n): ").lower() == 'y'

    try:
        generated_password = generate_password(length, use_uppercase, use_numbers, use_symbols)
        print(f"Generated password: {generated_password}")
    except ValueError as e:
        print(e)
