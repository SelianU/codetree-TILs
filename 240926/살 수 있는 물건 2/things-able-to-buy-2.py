subjects = [{"name": "book", "price": 3000},
           {"name": "mask", "price": 1000},
           {"name": "pen", "price": 500}]

money = int(input())

for subject in subjects:
    if subject["price"] >= money:
        print(subject["name"])
        break