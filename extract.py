import pandas as pd
import requests

def extract():
    print("-------------------------Extract-------------------------")
    # Make the API request
    response = requests.get('https://api.apify.com/v2/datasets/mGU2eGThTAaOMhuVx/items?token=apify_api_QBc0e219leXKCMqvWtllMeUn5AkuUz10mpOU')  # Replace with the actual API endpoint

    # Check if the request was successful
    if response.status_code == 200:
        # Convert the response JSON into a Python dictionary
        extracted_data = response.json()
        return extracted_data

    else:
        print('Failed to retrieve data from the API.')