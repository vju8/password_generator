**Name:**\
Password Generator

**Description:**\
This mini-project aims generating a password considering specific conditions.
    
**Conditions:**
- at least one lowercase
- at least one uppercase
- minimum password length 
- maximum password length (default 12)
- at least one number (optional)
- at least one special character (optional)

**The logics behind this pwd creator:**
- each password has minimum and maximum length. The minimum length can at most be equal to the maximum length
- the numbers and special characters conditions are adjustable in the generator   
- all_characters represents a string combining all the accessible characters for the wanted password
- based on the conditions chosen, a condition list of strings is created. Also, in order to make the pwd generation more random, the shuffle of the list is done
- the minimum_cond_idx int list represents the indexes in the passwordwhere the characters to fullfill the conditions will be inserted. The list is then sorted, so that later the for loop can access all of the indexes
- with the conditions_idx int there is a possibility to access strings in the conditions list and pick a random value from the strings, therefore fullfilling the basic conditions of the password generator. The conditions_idx is incremented after each access of the conditions list
- each iteration of the for loop adds a new char to the pwd (either from specific strings in conditions list, or simply randomly from all_characters string (depending on the index)) until password is ready

**Libraries used:**
- random
- string