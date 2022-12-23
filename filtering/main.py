from .letters import vowels, consonnants

def is_good_word(word: str) -> bool:
    optional_starting_consonnants_over = False
    main_vowels_over = False

    for letter in word:
        if letter in vowels:
            if not optional_starting_consonnants_over:
                optional_starting_consonnants_over = True
            
            if main_vowels_over and letter != 'e':
                return False

        if letter in consonnants:
            if optional_starting_consonnants_over and not main_vowels_over:
                main_vowels_over = True
    
    return True
