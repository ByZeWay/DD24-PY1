import json

def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)

    s = sum([item["score"] * item["weight"] for item in data])

    return round(s, 3)


print(task())
