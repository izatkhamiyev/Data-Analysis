import csv
import pygal
filename = 'com.csv' 
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	for index, c in enumerate(header_row):
		print(index,c)
	companies,cm=[],[]
	for row in reader:
		try:
			company = row[1]
			c = int(row[7])
		except: 
			continue
		else:
			if c>=100000000 and company not in companies:
				companies.append(company)
				cm.append(c)
hist = pygal.Bar()
hist.title = "Companies which raised more than 100000000$"
hist.x_labels=companies
hist.x_title = "Company"
hist.y_title = "Raised money($)"
hist.add('Money',cm)
hist.render_to_file('money_visual.svg')
