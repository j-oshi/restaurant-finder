import urllib.request
import ssl
import pandas as pd
import json


def fetch_restaurants_data(user_input, use_ssl_verification=True):
    """
    Make an HTTP request to a URL with an option to disable SSL verification.

    :param url: The target URL to make the request.
    :param use_ssl_verification: Whether to perform SSL certificate verification (default is True).
    :return: The response data as a string or an error message.
    """
    try:
        if not use_ssl_verification:
            # Create an SSL context that does not verify the certificate
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE
        else:
            ssl_context = None

        url = f"https://uk.api.just-eat.io/restaurants/bypostcode/{user_input}"

        request = urllib.request.Request(url)

        with urllib.request.urlopen(request, context=ssl_context) as response:
            if response.code == 200:
                data = response.read()
                return data.decode("utf-8")
            else:
                return None

    except urllib.error.URLError as e:
        print(f"Error opening URL '{url}': {e}")
        print("Please try again later.")
        return None


def load_and_filter_restaurants(data):
    try:
        convert_pyton_dictonary = json.loads(data)
        restaurant_data = pd.DataFrame(convert_pyton_dictonary["Restaurants"])

        filtered_conditions = (
            lambda row: row["RatingStars"] > 4.5
            and row["NumberOfRatings"] >= 100
            and row["DeliveryEtaMinutes"]["RangeUpper"] <= 45
            and any(item["Name"] == "Pizza" for item in row["Cuisines"])
        )
        filtered_restaurants = restaurant_data[
            restaurant_data.apply(filtered_conditions, axis=1)
        ]
        filtered_array = filtered_restaurants.to_dict(orient="records")
        return filtered_array

    except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
        print(e)


def filter_restaurant(user_input):
    response = fetch_restaurants_data(user_input)
    if response is not None:
        results = load_and_filter_restaurants(response)
        return results
    else:
        return {"message": "no restaurant found"}


# filter_restaurant("tw12")
