import requests

#correct api endpoint
url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"

#function to fetch and display a random thing
def get_random_tecnology_fact():
    try:
        response=requests.get(url,timeout=5)
        if response.status_code==200:
            fact_data=response.json()
            print(f"\nDid you know? {fact_data['text']}\n")
        else:
            print(f"Failed to fetch fact.Status code:{response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error:{e}")

#main loop
while True:
    user_input=input("Press Enter to get a random technology fact or type 'q' to quit")
    if user_input.lower()=='q':
        break
    get_random_tecnology_fact()
