import phonenumbers
import opencage
from myphone import number 
import folium

from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
loc = geocoder.description_for_number(pepnumber, "en")

print(f"Location: {loc}")

if not loc:
    print("Could not determine location from the phone number.")
else:
    from phonenumbers import carrier

    service_provider = phonenumbers.parse(number)
    print(carrier.name_for_number(service_provider, "en"))

    from opencage.geocoder import OpenCageGeocode

    key = "3e3deb8ebd5c4694a3fc23adbcb27c11"  # OpenCage API key
    geocoder = OpenCageGeocode(key)

    query = str(loc)
    print(f"Query: {query}")
    results = geocoder.geocode(query)

    if results and len(results) > 0:
        lat = results[0]["geometry"]["lat"]
        lng = results[0]["geometry"]["lng"]

        print(f"Latitude: {lat}, Longitude: {lng}")

        myMap = folium.Map(location=[lat, lng], zoom_start=9)
        folium.Marker([lat, lng], popup=loc).add_to(myMap)

        myMap.save("mylocation.html")
        print("Map saved as mylocation.html")
    else:
        print("Could not find coordinates for the location.")
