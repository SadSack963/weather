# Met Office Weather DataHub
# https://metoffice.apiconnect.ibmcloud.com/metoffice/production/

import os

IBM_CLIENT_ID = os.environ.get("IBM_CLIENT_ID")
IBM_CLIENT_SECRET = os.environ.get("IBM_CLIENT_SECRET")


def testing():
    # Milton Keynes
    latitude = 52.040623
    longitude = -0.759417

    import http.client

    conn = http.client.HTTPSConnection("api-metoffice.apiconnect.ibmcloud.com")

    headers = {
        'x-ibm-client-id': IBM_CLIENT_ID,
        'x-ibm-client-secret': IBM_CLIENT_SECRET,
        'accept': "application/json"
    }

    conn.request("GET",
                 f"/metoffice/production/v0/forecasts/point/three-hourly?excludeParameterMetadata={True}&includeLocationName={True}&latitude={latitude}&longitude={longitude}",
                 headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))


testing()
