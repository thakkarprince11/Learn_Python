import requests


# Function fetch_random_user_freeapi
def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

    response = requests.get(url=url)
    #print(response)

    data = response.json()

    if data["success"] and "data" in  data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]

        return username, country
    else:
        raise Exception("Failed to fetch userdata")
    

# Function main
def main():
    try:
        username, country = fetch_random_user_freeapi()             # Calling Function

        print(f"Username : {username},\nCountry : {country}")
    except Exception as e:
        print(str(e))


# Entry point main
if __name__ == "__main__":
    main()