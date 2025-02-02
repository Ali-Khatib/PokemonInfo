import requests

link="https://pokeapi.co/api/v2/"
question_list=[]

def getinfo(name):
    url=f"{link}/pokemon/{name}"
    response=requests.get(url)

    if response.status_code==200:
        answer=response.json()
        return answer

    else:
        print("Please enter a valid name")


name=input("Please enter the Pokemon's name: ")

while True:
    question=input("Enter the info you would like to learn about (type 'done' when finished): ").lower()

    if question=='done':
        break

    question_list.append(question)

info=getinfo(name)

if info:
    for q in question_list:
        try:
            print(f"{name.capitalize()}'s {q} is {info[q]}")
        except Exception:
            print(f"I am unable to find {name.capitalize()}'s '{q}' ")




