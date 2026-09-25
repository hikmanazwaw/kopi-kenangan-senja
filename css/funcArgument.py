def create_sorcerer(name, age, race, era):
    return{
        "name": name,
        "age": age,
        "race": race,
        "era": era,
    }

obj1 = create_sorcerer("Sukuna", 1000, "incarnation", "heian")
print(obj1)

obj2 = create_sorcerer("Kenjaku", 1000, "human", "1000+ year ago")
print(obj2)

obj3 = create_sorcerer("Hajime", 400, "human", "400 year ago")
print(obj3)

obj4 = create_sorcerer("400 year ago", 400, "human", "hajime")