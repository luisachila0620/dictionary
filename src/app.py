import requests, os,json

# print(os.getenv ("API_HOST"))
# Retrieve your API credentials from the .env file
if os.getenv("API_KEY") is None or os.getenv("API_KEY") == "":
    print("ERROR! Make sure you have created your .env file with your API credentials (look for the .evn.example as an example and replace it with your own API credentials that you got from RapidAPI)")
    exit(1)


# Get credentials from the .env file
API_HOST = os.getenv("API_HOST")
API_KEY = os.getenv("API_KEY")
print("hello world")
# open the file
with  open("definition.json") as new_file1:
    content = json.load(new_file1)
    new_file1.close()
print("this was your last seach" + content)
# input ("what term are you looking for?")
term = input("what term are you looking for?")

url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

querystring = {"term":term}

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)
api_response = response.json()
response_list = api_response["list"]
first_item = response_list[0]
definition = first_item["definition"]
print(definition)
# print(response.json()["list"][0]["definition"])

#1. open or create a file
# with open("definition.json", "w") as new_file:

new_file = open("definition.json", "w")
#2. write data on the file
json.dump(definition,new_file)
#3. close the file
new_file.close()






# continue with your application here