import random 
import string 


def password_generator(minimum_length, maximum_length = 12, numbers = True, special_chars = True):
    """
    Function responsible for generating a password considering specific 
    conditions.
    
    Conditions:
    - at least one lowercase 
    - at least one uppercase 
    - minimum password length 
    - maximum password length (default 12) [BASE]
    - at least one number (optional)
    - at least one special character (optional)

        Parameters
        ----------------------------------------------------------------------
        minimum_length : int
            Minimum password length.
        maximum_length : int, optional
            DESCRIPTION. The default is 12.
        numbers : boolean, optional
            DESCRIPTION. The default is True.
        special_chars : boolean, optional
            DESCRIPTION. The default is True.
    
        Returns
        ----------------------------------------------------------------------
        password : str
            Generated password based on the wanted conditions returned as 
            a string.
    """
    
    all_lowercase_letters = string.ascii_lowercase
    all_uppercase_letters = string.ascii_uppercase 
    all_digits = string.digits
    all_special_chars = string.punctuation

    all_characters = all_lowercase_letters + all_uppercase_letters
    conditions = [all_lowercase_letters, all_uppercase_letters]
    
    if numbers:
        all_characters += all_digits
        conditions.append(all_digits)
    if special_chars:
        all_characters += all_special_chars
        conditions.append(all_special_chars)

    random.shuffle(conditions)
    
    minimum_cond_idx = random.sample(range(0, random.randint(minimum_length, maximum_length)), len(conditions))
    minimum_cond_idx.sort()
    
    password = ""
    conditions_idx = 0
    for char in range(0, random.randint(minimum_length, maximum_length)):
        if char in minimum_cond_idx:
            password += random.choice(conditions[conditions_idx])
            conditions_idx +=1 
        else:
            password += random.choice(all_characters) 
    return password    


new_password = password_generator(10, 12, False, False)
print(f"The generated password is: {new_password}\nAnd it's legth is {len(new_password)}")