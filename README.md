# Weather Average Temperature Calculator

The script [temperature_7d_avg.py](./temperature_7d_avg.py) calculates the average temperature over the past seven days for a specified city.

## Setup

1. Install Python 3.x on your system.
2. Clone this repository and navigate to the project directory.
3. Install required Python libraries:

```
pip install -r requirements.txt
```
## Usage

Run the script from the command line by specifying a city name:
```
python temperature_7d_avg.py "City name"
```
## Notes

The script uses a Free APIs for non-commercial use and the limitations are:
- For Open-Meteo API: Less than 10'000 API calls per day, 5'000 per hour, 600 per minute.
- For Geocode.xyz API: 1 API call per second.

