spell = input()
bul = False
while True:
    command = input().split(" ")
    spell_command = command[0]
    if spell_command == "Abracadabra":
        break
    if spell_command == "Abjuration":
        spell = spell.upper()
        print(spell)
        bul = True
    if spell_command == "Necromancy":
        spell = spell.lower()
        bul = True
        print(spell)

    if spell_command == "Illusion":
        bul = True
        spell_number = int(command[1])
        spell_letter = command[2]
        x = list(spell)
        if spell_number < len(x):
            x[spell_number] = spell_letter
            spell = "".join(x)
            print("Done!")
        else:
            print("The spell was too weak.")

    if spell_command == "Divination":
        bul = True
        spell_number = command[1]
        spell_letter = command[2]
        spell = spell.replace(spell_number, spell_letter)
        print(spell)

    if spell_command == "Alteration":
        bul = True
        spell_number = command[1]
        removed = spell.replace(spell_number,"")
        print(removed)
    if not bul:
        print("The spell did not work!")
