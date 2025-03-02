def calculate(input, rules):
    tape = "L" + input + "R"
    
    rule_dict = {}
    for rule in rules:
        char, state, new_char, new_state, action = rule
        rule_dict[(char, state)] = (new_char, new_state, action)
    
    position = 0  # Sijainti on merkin L kohdalla
    state = 1     # Alkutila on 1
    steps = 0     # Laskuri toiminnoille
    
    while steps < 1000:
        if position < 0 or position >= len(tape):
            return False
        
        current_char = tape[position]
        
        if (current_char, state) not in rule_dict:
            return False
        
        new_char, new_state, action = rule_dict[(current_char, state)]
        
        tape = tape[:position] + new_char + tape[position+1:]
        
        state = new_state
        
        if action == "LEFT":
            position -= 1
        elif action == "RIGHT":
            position += 1
        elif action == "ACCEPT":
            return True
        elif action == "REJECT":
            return False
        
        steps += 1
    
    # Jos tuhat toimintoa suoritettu ilman hyväksyntää tai hylkäystä, hylätään
    return False

def create_rules():
    rules = []
    
    # TILA 1: Aloita
    rules.append(("L", 1, "L", 2, "RIGHT"))
    
    # TILA 2: Heti alussa, lähde liikkumaan oikealle
    rules.append(("0", 2, "0", 3, "RIGHT"))
    rules.append(("1", 2, "1", 3, "RIGHT"))
    
    # TILA 3: Etsi ensimmäisen puoliskon loppua (keskikohtaa)
    rules.append(("0", 3, "0", 3, "RIGHT"))
    rules.append(("1", 3, "1", 3, "RIGHT"))
    
    # Kun olemme puolivälissä (merkki R), palaa takaisin alkuun
    rules.append(("R", 3, "R", 4, "LEFT"))
    
    # TILA 4: Liiku vasemmalle takaisin syötteen alkuun
    rules.append(("0", 4, "0", 4, "LEFT"))
    rules.append(("1", 4, "1", 4, "LEFT"))
    
    # Kun olemme alussa (merkki L), aloita vertailu
    rules.append(("L", 4, "L", 5, "RIGHT"))
    
    # TILA 5: Tallenna ensimmäinen merkki muistiin
    rules.append(("0", 5, "0", 6, "RIGHT"))  # 0 tallennettiin
    rules.append(("1", 5, "1", 7, "RIGHT"))  # 1 tallennettiin
    
    # TILA 6 ja 7: Liiku oikealle syötteen puoliväliin
    # Tila 6: Tallennettiin 0
    rules.append(("0", 6, "0", 6, "RIGHT"))
    rules.append(("1", 6, "1", 6, "RIGHT"))
    
    # Tila 7: Tallennettiin 1
    rules.append(("0", 7, "0", 7, "RIGHT"))
    rules.append(("1", 7, "1", 7, "RIGHT"))
    
    # Kun olemme puolivälissä, vertaa ensimmäistä merkkiä puolivälin jälkeiseen
    rules.append(("R", 6, "R", 8, "LEFT"))  # Odotetaan 0 puolivälin jälkeen
    rules.append(("R", 7, "R", 9, "LEFT"))  # Odotetaan 1 puolivälin jälkeen
    
    # TILA 8: Vertaa puolivälin jälkeistä merkkiä nollaan
    rules.append(("0", 8, "0", 10, "LEFT"))  # Täsmää!
    rules.append(("1", 8, "1", 11, "REJECT"))  # Ei täsmää!
    
    # TILA 9: Vertaa puolivälin jälkeistä merkkiä yhteen
    rules.append(("0", 9, "0", 11, "REJECT"))  # Ei täsmää!
    rules.append(("1", 9, "1", 10, "LEFT"))  # Täsmää!
    
    # TILA 10: Merkki täsmäsi, jatka vertailua
    rules.append(("0", 10, "0", 10, "LEFT"))
    rules.append(("1", 10, "1", 10, "LEFT"))
    rules.append(("L", 10, "L", 12, "RIGHT"))  # Kaikki täsmäsi!
    
    # TILA 11: Merkki ei täsmännyt, hylkää
    rules.append(("0", 11, "0", 11, "REJECT"))
    rules.append(("1", 11, "1", 11, "REJECT"))
    rules.append(("L", 11, "L", 11, "REJECT"))
    
    # TILA 12: Hyväksy
    rules.append(("0", 12, "0", 12, "ACCEPT"))
    rules.append(("1", 12, "1", 12, "ACCEPT"))
    rules.append(("L", 12, "L", 12, "ACCEPT"))
    rules.append(("R", 12, "R", 12, "ACCEPT"))
    
    return rules

if __name__ == "__main__":
    rules = create_rules()

    print(calculate("00", rules)) # True
    print(calculate("001001", rules)) # True
    print(calculate("10111011", rules)) # True
    print(calculate("01", rules)) # False
    print(calculate("00100", rules)) # False
    print(calculate("10111101", rules)) # False
