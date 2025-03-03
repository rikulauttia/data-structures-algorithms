def hash_value(string):
    A = 23
    M = 2**32
    result = 0
    
    for c in string:
        char_value = ord(c) - ord('a')
        
        result = (result * A + char_value) % M
        
    return result

def find_other(string):
    A = 23
    M = 2**32

    if len(string) == 0:
        return "az"
    
    if len(string) == 1:
        char_value = ord(string[0]) - ord('a')
        
        for c1 in range(26):  # 'a' - 'z'
            for c2 in range(26):  # 'a' - 'z'
                if (c1 * A + c2) % M == char_value:
                    new_string = chr(ord('a') + c1) + chr(ord('a') + c2)
                    if new_string != string:
                        return new_string

    
    original_hash = hash_value(string)
    
    if len(string) == 2:
        first_char = ord(string[0]) - ord('a')
        second_char = ord(string[1]) - ord('a')
        
        # Etsitään toinen kahden merkin yhdistelmä, jolla on sama hajautusarvo
        for c1 in range(26):  # 'a' - 'z'
            for c2 in range(26):  # 'a' - 'z'
                # Lasketaan hajautusarvo: (c1*A + c2) % M
                test_hash = (c1 * A + c2) % M
                if test_hash == original_hash:
                    new_string = chr(ord('a') + c1) + chr(ord('a') + c2)
                    if new_string != string:
                        return new_string
        
        # Jos ei löydy kahden merkin yhdistelmää, kokeillaan muita pituuksia
        for c1 in range(26):  # 'a' - 'z'
            for c2 in range(26):  # 'a' - 'z'
                for c3 in range(26):  # 'a' - 'z'
                    # ((c1*A + c2)*A + c3) % M
                    test_hash = ((c1 * A + c2) * A + c3) % M
                    if test_hash == original_hash:
                        return chr(ord('a') + c1) + chr(ord('a') + c2) + chr(ord('a') + c3)
        
        # Viimeisenä vaihtoehtona muutetaan ensimmäistä merkkiä ja lisätään a-kirjain
        for c in range(26):
            if c != first_char:
                new_string = chr(ord('a') + c) + string[1] + "a"
                if hash_value(new_string) == original_hash:
                    return new_string
        
        # Jos mikään ei toimi, palauta vähintään eri merkkijono
        return string + "a"

    prefix = string[:-2]
    last_two = string[-2:]

    prefix_hash = 0
    
    for c in prefix:
        char_value = ord(c) - ord('a')
        prefix_hash = (prefix_hash * A + char_value) % M
    
    required_contribution = (original_hash - (prefix_hash * (A**2)) % M) % M
    
    for c1 in range(26):  # 'a' - 'z'
        for c2 in range(26):  # 'a' - 'z'
            test_contribution = (c1 * A + c2) % M
            if test_contribution == required_contribution:
                new_last_two = chr(ord('a') + c1) + chr(ord('a') + c2)
                if new_last_two != last_two:
                    return prefix + new_last_two

if __name__ == "__main__":
    string1 = "kissa"
    string2 = find_other("kissa")
    print(string1, hash_value(string1)) # kissa 2905682
    print(string2, hash_value(string2)) # zfgjynuk 2905682
    vl1 = "vl"
    vl2 = find_other("vl")
    print(vl1, hash_value(vl1))
    print(vl2, hash_value(vl2))