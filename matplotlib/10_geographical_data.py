# https://www.tutorialspoint.com/python/python_geographical_data.htm

"""
Many open source python libraries now have been created to represent the geographical maps. One such package is Cartopy.

Here, we show a portion of the world map showing parts of Asia and Australia. You can adjust the values of the parameters in the method
set_extent to locate different areas of world map.
"""

import cartopy.crs as ccrs
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

# make the map global rather than have it zoom in to
# the extents of any plotted data

ax.set_extent((60, 150, 55, -25))

ax.stock_img()
ax.coastlines()

ax.tissot(facecolor='purple', alpha=0.8)

plt.show()
