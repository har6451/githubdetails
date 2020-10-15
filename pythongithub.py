import requests
 
# github username
username = input("Enter the github user name :")
# url to request
url = f"https://api.github.com/users/{username}"
# make the request and return the json
user_data = requests.get(url).json()
 
# PRINTING ONLY THE REQUIRED DATA...
print('Name : ',user_data['name'])
print("login id : ",user_data["login"])
print("unique id : ",user_data['id'])
print("Followers : ",user_data['followers'])
print("Following : ",user_data['following'])
print('Public Repos : ',user_data['public_repos'])
print('Location : ',user_data['location'])
print("Github Bio : ",user_data['bio'])