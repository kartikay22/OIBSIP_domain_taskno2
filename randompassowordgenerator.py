import random
import string

def Password(lenght, use_text=True, use_number=True, use_special_character=True):
    character = ""
    print("DEBUG: Inside the Password function.")
    print(f"DEBUG: Input length: {lenght}")
    
    if use_text:
        character += string.ascii_letters
        print("DEBUG: Including letters.")
    if use_number:
        character += string.digits
        print("DEBUG: Including numbers.")
    if use_special_character:
        character += string.punctuation
        print("DEBUG: Including special characters.")
    
    if not character:
        print("error: please select at least one character type.")
        return None  # Return None instead of just returning to be explicit
    
    # Generate the password
    pwd = "".join(random.choice(character) for _ in range(lenght))
    print(f"DEBUG: Generated password before returning: {pwd}")
    return pwd

def main():
    print("Starting Swapneel Password Generator")
    
    try:
        lenght = int(input("Enter your password lenght: "))
        use_text = input("Include letter in your password? (Y/N): ").lower() == 'y'
        use_number = input("Include number in your password? (Y/N): ").lower() == 'y'
        use_special_character = input("Include Special character in your password? (Y/N): ").lower() == 'y'
        
        pwd = Password(lenght, use_text, use_number, use_special_character)
        
        if pwd:
            print("Your Generated Password:", pwd)
        else:
            print("Password generation failed.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid number for password length.")

if __name__ == "__main__":
    main()
