import folium

points =[    

(23.7501817, 90.3928485), (23.7447125, 90.3901305),
(23.7447537, 90.3900568), (23.7415059, 90.391801),
(23.741552, 90.3918246), (23.7272204, 90.3897453),
(23.7261438, 90.3921712), (23.7243877, 90.3958591)


]

mymap = folium.Map(location=points[0], zoom_start=13)


for i, point in enumerate(points):
    if i == 0:
        icon = folium.Icon(color='green', icon='play')
    elif i == len(points) - 1:
        icon = folium.Icon(color='red', icon='stop')
    else:
        icon = folium.Icon(color='blue')
    folium.Marker(point, icon=icon).add_to(mymap)


mymap
