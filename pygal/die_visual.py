import pygal
from die import Die

die1 = Die()
die2 = Die()
die3 = Die()
results = []
for roll_num in range(100000):
	result = die1.roll()+die2.roll()
	results.append(result)
frequencies = []
for value in range(2,die1.num_sides+die2.num_sides + 1):
	frequency = results.count(value)
	frequencies.append(frequency)

hist = pygal.Bar()
hist.title = "Results of two rolling dices 1000 times"

hist.x_labels = []
for value in range(2,die1.num_sides + die2.num_sides +1):
	hist.x_labels.append(value)
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6',frequencies)
hist.render_to_file('die_visual.svg')

