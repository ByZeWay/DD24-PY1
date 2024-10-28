import json

def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)

    s = 0.0

    for i in data:
        score = i.get("score", 0)
        weight = i.get("weight", 0)
        s += score * weight

    return round(s, 3)


print(task())
