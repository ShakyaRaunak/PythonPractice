# https://www.pluralsight.com/guides/creating-interactive-charts-with-python-pygal

import pygal
from pygal.style import Style

custom_style = Style(
    colors=('#E80080', '#404040', '#9BC850')
)

bar_chart = pygal.Bar(style=custom_style)
bar_chart.title = "Destiny Kill/Death Ratio"

elements = [
    ("Dijiphos", [0.94]),
    ("Punisherdonk", [1.05]),
    ("Musclemuffins20", [1.10])
]

for e in elements:
    bar_chart.add(e[0], e[1])

bar_chart.render_in_browser()
