import datetime as dt
from time import sleep
import met_office.met_office_observation as moo
import met_office.met_office_forecast as mof

# NOTE: This site will eventually be replaced by DataHub

# Get MetOffice Observation Hourly Data
# moo.get_hourly_sites()
# moo.get_hourly_site_capabilities()
# moo.get_weather()

# Get MetOffice Forecast Hourly Data
mof.get_3hourly_sites()
mof.get_3hourly_site_capabilities()
mof.get_weather()
