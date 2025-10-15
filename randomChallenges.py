students = {
    "nathan":{
        "email": "nathan@example.com",
        "total_paid": 1367,
        "total_amount": 4000
    },
    "Alice":{
        "email": "alice@gmail.com",
        "total_paid": 1200,
        "total_amount": 1700
    },
    "Bob":{
        "email": "bob@gmail.com",
        "total_paid": 2000,
        "total_amount": 6000
    },
    "Charlie":{
        "email": "charlie@gmail.com",
        "total_paid": 3000,
        "total_amount": 5000
    }
}

def getOwedMoney():
    for name ,value in students.items():
        owed=value["total_amount"]-value["total_paid"]
        print(f"Hello {name} and email {value["email"]} you owe {owed}")
    return
getOwedMoney()

from collections import defaultdict, Counter
from pprint import pprint

# 1) build nested dict dataset
data = {
    "alice": {
        "joined": "2024-01-15",
        "posts": [
            {"id": 1, "title": "Intro to Python", "likes": 150, "tags": ["python", "beginner"]},
            {"id": 2, "title": "Advanced OOP", "likes": 75, "tags": ["python", "oop"]},
        ],
    },
    "bob": {
        "joined": "2023-11-02",
        "posts": [
            {"id": 3, "title": "Databases 101", "likes": 30, "tags": ["sql", "databases"]},
        ],
    },
    "carol": {
        "joined": "2022-06-20",
        "posts": [],  # inactive user (no posts)
    },
}
# print summary for each user
for user, details in data.items():
    num_posts = len(details["posts"])
    total_likes = sum(post["likes"] for post in details["posts"])
    print(f"User: {user}, Joined: {details['joined']}, Posts: {num_posts}, Total Likes: {total_likes}")


myinfo={
    "school":["Tenwek high school" ,"suswondo pry"],
    "name":"nathan",
    "height": {"feet":5.2 ,"meters":1.6}
}
# for x, y in myinfo.items():
#     # print(f"{x} :{y}")
#     if isinstance(y, dict) and "feet" in y:
#         print(y["feet"])
#     # print(x)
info=myinfo["height"]["feet"]
print(info)