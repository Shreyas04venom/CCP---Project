import folium
from folium import IFrame
import pandas as pd

# Sample data: Cultural Heritage sites (Latitude, Longitude, Title, Description, Image URL)
data = [
    {"name": "Great Wall of China", "latitude": 40.4319, "longitude": 116.5704, 
     "description": "A historic wall built to protect Chinese states and empires.", 
     "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Great_Wall_of_China_July_2007.jpg/640px-Great_Wall_of_China_July_2007.jpg"},
    
    {"name": "Machu Picchu", "latitude": -13.1631, "longitude": -72.5450, 
     "description": "An ancient Incan city high in the Andes mountains of Peru.", 
     "image": "https://upload.wikimedia.org/wikipedia/commons/5/59/Machu_Picchu_%28anaglyph%29.jpg"},
    
    {"name": "Eiffel Tower", "latitude": 48.8584, "longitude": 2.2945, 
     "description": "A wrought-iron lattice tower on the Champ de Mars in Paris.", 
     "image": "https://upload.wikimedia.org/wikipedia/commons/a/a8/Eiffel_Tower_%28crop2%29.jpg"}
]

# Create a map centered around a central location
m = folium.Map(location=[20.0, 0.0], zoom_start=2)

# Add markers for each cultural site
for site in data:
    iframe = IFrame(f'<b>{site["name"]}</b><br>{site["description"]}<br><img src="{site["image"]}" width="200">', width=300, height=300)
    popup = folium.Popup(iframe, max_width=2650)
    folium.Marker([site["latitude"], site["longitude"]], popup=popup).add_to(m)

# Save the map as an HTML file
m.save("cultural_heritage_map.html")

print("Map saved as 'cultural_heritage_map.html'. Open this file in your browser to explore!")
