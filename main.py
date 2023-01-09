import dotenv
import os
import sys
import requests

def main():
    dotenv.load_dotenv("config.env")
    apikey = os.getenv('apikey')
    location = os.getenv('location')
    print("\nWelcome to AGWA, made with <3 by 404Mate!")
    if apikey == None or "":
        print("\nWARNING! No API key detected.")
        sys.exit

    try:
    # check internet
        request = requests.get("https://1.1.1.1",
            timeout=10)
    #catch no internet
    except:
        print("\n No Internet Detected")
        sys.exit()
    
    if location == "" or None:
        location = input("\nWhat is your city name or zipcode?\n")

    root_url = "http://api.openweathermap.org/data/2.5/weather?"
    url = f"{root_url}appid={apikey}&q={location}"
    r = requests.get(url)
    data = r.json()
    descr = None
    if data['cod'] == 200:
        descr = data['weather'][0]['description']
        weatherid = data['weather'][0]['id']
    if descr == None:
        print('\nCity name nor recognized')
        sys.exit()
    print(descr)
    print(weatherid)

if __name__ == "__main__":
    main()

