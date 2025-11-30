def print_best_weapon(weapon_list):
    max_damage = -1
    best_weapon_name = ""
    
    for weapon in weapon_list:
        weapon_name = weapon[0]
        weapon_damage = weapon[1]
        
        if weapon_damage > max_damage:
            max_damage = weapon_damage
            best_weapon_name = weapon_name
            
    print(best_weapon_name)
    
weapon1 = ("blade", 10)
weapon2 = ("sabre", 35)
weapon3 = ("sword", 50)
meele_weapon = [weapon1, weapon2, weapon3]

print_best_weapon(meele_weapon)
