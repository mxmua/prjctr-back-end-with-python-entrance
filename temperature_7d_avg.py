import requests
import argparse

def get_coordinates(city_name):
    """ Returns:
        tuple: A tuple containing the latitude and longitude of the city, or (None, None) if not found.
    """
    url = f"https://geocode.xyz/{city_name}?json=1"
    try:
        response = requests.get(url)
        data = response.json()

        if 'error' in data:
            print(f"Error: {data['error']['description']}")
            return None, None

        latitude = data.get('latt')
        longitude = data.get('longt')

        if latitude and longitude:
            return latitude, longitude
        else:
            print("No coordinates found for the given city.")
            return None, None
    except requests.RequestException as e:
        print(f"An error occurred while fetching data: {e}")
        return None, None

def get_weather_data(latitude, longitude):
    """ Fetch weather data for the past seven days for a given Latitude and Longitude.
        Returns:
        list: a list with hourly temperature for the past 7 days
    """

    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&past_days=7&hourly=temperature_2m&timezone=auto"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    temperatures = data['hourly']['temperature_2m']
    return temperatures

def calculate_average_temperature(temperatures):
    """ Calculate the average temperature from a list of temperatures. """
    return sum(temperatures) / len(temperatures)

def main():
    parser = argparse.ArgumentParser(description="Fetch and calculate the average temperature over the past 7 days for a specified city.")
    parser.add_argument('city', type=str, help='City name to fetch the weather data for')
    args = parser.parse_args()

    try:
        lat, lon = get_coordinates(args.city)

        if not lat or not lon:
            raise ValueError(f"City {args.city} not found")

        temperatures = get_weather_data(lat, lon)
        average_temp = calculate_average_temperature(temperatures)
        print(f"The average temperature in {args.city} over the past 7 days was {average_temp:.2f} degrees Celsius.")
    except requests.RequestException as e:
        print(f"Failed to retrieve data: {e}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
