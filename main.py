import json

def z1():
    with open('F:/10 lab/кофешоколадкичай.json', encoding='UTF-8') as file:
        a = json.load(file)

    for item in a['products']:
        print('Название:', item['name'])
        print('Цена:', item['price'])
        print('Вес:', item['weight'])
        if item['available']:
            print('В наличии')
        else:
            print('Нет в наличии!')
        print()

def z2():
    with open('F:/10 lab/кофешоколадкичай.json', encoding='UTF-8') as file:
        a = json.load(file)


    products = a["products"]


    for item in products:
        print(f"Название: {item['name']}")
        print(f"Цена: {item['price']}")
        print(f"Вес: {item['weight']}")
        if item['available']:
            print("В наличии")
        else:
            print("Нет в наличии!")
        print()


    name = input("Введите название продукта: ")
    price = int(input("Введите цену продукта: "))
    available = input("Продукт есть в наличии?: ")
    if available == "yes":
        available = True
    else:
        available = False
    weight = int(input("Введите вес продукта: "))
    print()


    new_item = {
        "name": name,
        "price": price,
        "available": available,
        "weight": weight
    }


    products.append(new_item)


    with open('F:/10 lab/кофешоколадкичай.json', 'w', encoding='UTF-8') as file:
        json.dump(a, file)

    products = a["products"]

    for item in products:
        print(f"Название: {item['name']}")
        print(f"Цена: {item['price']}")
        print(f"Вес: {item['weight']}")
        if item['available']:
            print("В наличии")
        else:
            print("Нет в наличии!")
        print()

def z3():
    with open ("en-ru slovarik.txt","r") as file:
        l = file.readlines()

    d = {}

    for line in l:
        eng = line.split(" - ")[0].strip()
        ru = line.split(" - ")[1].strip().split(', ')
        for word in ru:
            if word not in d:
                d[word] = [eng]
            else:
                d[word].append(eng)
    with open("ru-en slovarik.txt","w") as file:
        for ru,eng in sorted(d.items()):
            file.write(f"{ru} - {', '.join(eng)}\n")