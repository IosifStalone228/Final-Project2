from conf import MODEL
import random
from faker import Faker
from title import list_1
import json
import re


fake = Faker("ru_RU")

def main(pk1: int = 1) ->list:
    while True:
        list_ = []
        dict_ = {
            "model": MODEL,
            "pk": pk1,
            "fields": {
                "title": random.choice(list_1),
                "year": random.randint(1701, 2022),
                "pages": random.randint(50,1000),
                "isbn13": fake.isbn13(),
                "rating": round(random.uniform(1, 5), 1),
                "price": round(random.uniform(100, 5000), 2),
                "author": [
                    fake.name(),
                    fake.name()
                ]
            }
        }
        yield dict_
        pk1 += 1


if __name__ == "__main__":
    output_file = "output.json"
    pk1 = main()
    list_ = []

for i in range(100):
    list_.append(next(pk1))
    
    
for dict_ in list_:
    for i in dict_:
        with open(output_file, "w") as file:
            file.write(i)

print(list_)
