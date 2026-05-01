import json

def load_data(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data

def display_users(data):
    print(f"User & Their Connection:\n")
    for user in data["users"]:
        print(f"{user['name']} (ID: {user['id']}) - Friends: {user['friends']} - Liked Pages: {user['liked_pages']}")
        #print(f"Id:{user['id']} - {user['name']} is friends with {', '.join(map(str, user['friends']))} and liked page are {', '.join(map(str, user['liked_pages']))}")
    print(f"\nPages Information:")
    for page in data["pages"]:
        print(f"{page['id']} : {page['name']}")
 
