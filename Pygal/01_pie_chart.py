# https://www.pluralsight.com/guides/creating-interactive-charts-with-python-pygal

import pygal

pie_chart = pygal.Pie()
pie_chart.title = 'Favourite Pets'

elements = [
    ('Dog', 6),
    ('Cat', 4),
    ('Hamster', 3),
    ('Fish', 2),
    ('Snake', 1)
]

for e in elements:
    pie_chart.add(e[0], e[1])

pie_chart.render_in_browser()
# pie_chart.render_to_file('piechart.png')
