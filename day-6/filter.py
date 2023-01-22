friends = [
    ('Rachel', 15),
    ('Gregory', 25),
    ('Phoebe', 40)
]

age = lambda data:data[1] >= 18

adults = list(filter(age, friends))

print(adults)