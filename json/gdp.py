import requests
from pygal.maps.world import World,COUNTRIES
import pygal
url = 'https://pkgstore.datahub.io/core/gdp/gdp_json/data/1a2503aa36368933be8f9a96e1dc16de/gdp_json.json'
r=requests.get(url)
def get_country_code(country_name):
	for code, name in COUNTRIES.items():
		
		if name == country_name:
			return code
	return None
gdps = r.json()
gdps_lys = []
for gdp in gdps:
	if len(gdps_lys) == 0:
		gdps_lys.append({'name': gdp['Country Name'], 'year': gdp['Year'],'value': gdp['Value']})
	else:
		if gdps_lys[-1]['name'] == gdp['Country Name']:
			gdps_lys[-1]['year'] = gdp['Year']
			gdps_lys[-1]['value'] = gdp['Value']
		else:
			gdps_lys.append({'name': gdp['Country Name'], 'year': gdp['Year'],'value': gdp['Value']})
countries = {}
ans = 0
for gdp in gdps_lys:
	code = get_country_code(gdp['name'])
	if code:
		countries[code] = gdp['value']*1000000000
	else:
		print(gdp['name'])
print (ans)
wm = World()
wm.title = 'Gpd of counries'
wm.add('',countries)
wm.render_to_file('Gdps.svg')
