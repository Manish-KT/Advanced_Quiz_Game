import requests

response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
question_data = response.json()["results"]
for i in range(len(question_data)):
    print(question_data[i]["correct_answer"])
