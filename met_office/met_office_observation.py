import requests
import json
from os import path

MET_OFFICE_API_KEY = "a3e7a65f-5243-4ae3-a759-bf0bc21ff8b1"
MET_OFFICE_BASE_URL = "http://datapoint.metoffice.gov.uk/public/data/"
DATATYPE = "json"


def get_weather():
    """Only needs to be run once per hour.
    Returns hourly met_office observations for the last 24 hours. Updated hourly."""

    # https://register.metoffice.gov.uk/MyAccountClient/account/view

    location_id = "99057"  # Woburn

    resource_location = f"val/wxobs/all/{DATATYPE}/{location_id}"
    resolution = "hourly"
    met_office_url = MET_OFFICE_BASE_URL + resource_location + "?res=" + resolution + "&key=" + MET_OFFICE_API_KEY
    print(met_office_url)
    # http://datapoint.metoffice.gov.uk/public/data/val/wxobs/all/json/99057?res=hourly&key=a3e7a65f-5243-4ae3-a759-bf0bc21ff8b1

    response = requests.get(met_office_url, timeout=1)
    response.raise_for_status()
    data = response.json()
    print(data)
    with open("met_office/data/observation/hourly_location.json", mode="w") as file:
        # fp is a file pointer
        json.dump(data, fp=file, indent=4)


def get_hourly_sites():
    """NOTE: This only needs to be run once to get the met_office station IDs.
    Returns a list of locations (also known as sites) for which results are available
    for the hourly observations data feed. You can use this to find the ID of the site
    that you are interested in."""

    if not path.exists("met_office/data/observation/hourly_sitelist.json"):
        resource_sitelist = f"val/wxobs/all/{DATATYPE}/sitelist"
        met_office_url = MET_OFFICE_BASE_URL + resource_sitelist + "?key=" + MET_OFFICE_API_KEY
        print(met_office_url)
        # http://datapoint.metoffice.gov.uk/public/data/val/wxobs/all/json/sitelist?key=a3e7a65f-5243-4ae3-a759-bf0bc21ff8b1
        response = requests.get(met_office_url, timeout=1)
        response.raise_for_status()
        data = response.json()
        print(data)
        with open("met_office/data/observation/hourly_sitelist.json", mode="w") as file:
            # fp is a file pointer
            json.dump(data, fp=file, indent=4)

        # Closest location to Milton Keynes is:
        my_location = {
            "Locations": {
                "Location": [
                    {
                        "elevation": "89.0",
                        "id": "99057",
                        "latitude": "52.017",
                        "longitude": "-0.6",
                        "name": "Woburn",
                        "region": "ee",
                        "unitaryAuthArea": "Central Bedfordshire"
                    }
                ]
            }
        }


def get_hourly_site_capabilities():
    """Only needs to be run once per hour.
    Returns a summary of available time steps for the UK observations data feed.
    You can use this data feed to check that the time step you are interested in is
    available before querying the relevant web service to get the data. Updated hourly."""

    resource_capabilities = f"val/wxobs/all/{DATATYPE}/capabilities"
    resolution = "hourly"
    met_office_url = MET_OFFICE_BASE_URL + resource_capabilities + "?res=" + resolution + "&key=" + MET_OFFICE_API_KEY
    print(met_office_url)
    # http://datapoint.metoffice.gov.uk/public/data/val/wxobs/all/json/capabilities?res=hourly&key=a3e7a65f-5243-4ae3-a759-bf0bc21ff8b1

    response = requests.get(met_office_url, timeout=1)
    response.raise_for_status()
    data = response.json()
    print(data)
    with open("met_office/data/observation/hourly_capabilities.json", mode="w") as file:
        # fp is a file pointer
        json.dump(data, fp=file, indent=4)



