import psycopg2
from geopy import Nominatim

geolocator = Nominatim(
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36")

con = psycopg2.connect(database="dvdrental", user="postgres",
                       password="11111", host="127.0.0.1", port="5432")

print("Database opened successfully")
cur = con.cursor()
cur.execute('''SELECT * FROM get_addresses_with_11_and_city_btw_400_600()''')
records = cur.fetchall()
for address_id, address in records:
    try:
        location = geolocator.geocode(address)
        lat, lon = location.latitude, location.longitude
    except:
        lat, lon = 0, 0
    cur.execute(
        f'UPDATE address SET latitude = {lat}, longitude = {lon} WHERE address_id = {address_id};')
con.commit()
