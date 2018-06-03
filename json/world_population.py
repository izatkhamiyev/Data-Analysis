import json
from pygal.maps.world import World
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle
from country_codes import get_country_code

filename = 'population_data.json'
with open(filename) as f:
	pop_data = json.load(f)
	cc_population={}
	for pop_dict in pop_data:
		if pop_dict['Year'] == '2010':
			country_name = pop_dict['Country Name']
			population = int(float(pop_dict['Value']))
			code = get_country_code(country_name)
			if code:
				cc_population[code] = population
			
	cc_pop1, cc_pop2, cc_pop3 = {},{},{}
	for code, pop in cc_population.items():
		if pop < 10000000:
			cc_pop1[code] = pop
		else: 
			if pop < 1000000000:
				cc_pop2[code] = pop
			else:
				cc_pop3[code] = pop
	print(len(cc_pop1),len(cc_pop2),len(cc_pop3))
	wm_style = RotateStyle('#336699',base_style = LightColorizedStyle)
	wm = World(style = wm_style)
	wm.title = 'World Population in 2010, by Country'
	wm.add('0-10m',cc_pop1)
	wm.add('10-1bn',cc_pop2)
	wm.add('>1bn',cc_pop3)
	wm.render_to_file('world.svg')
	
