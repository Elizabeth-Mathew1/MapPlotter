import io
import os
import exifread
import folium
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot_location', methods=['POST'])
def plot_location():
    if 'image' in request.files:
        image = request.files['image']
        image_stream = io.BytesIO(image.read())
        tags = exifread.process_file(image_stream)
        latitude = tags.get('GPS GPSLatitude')
        latitude_ref = tags.get('GPS GPSLatitudeRef')
        longitude = tags.get('GPS GPSLongitude')
        longitude_ref = tags.get('GPS GPSLongitudeRef')

        if latitude and latitude_ref and longitude and longitude_ref:
            latitude = _convert_to_degrees(latitude)
            longitude = _convert_to_degrees(longitude)
            if latitude_ref.values == 'S':
                latitude = -latitude
            if longitude_ref.values == 'W':
                longitude = -longitude

            map = folium.Map(location=[latitude, longitude], zoom_start=13)
            folium.Marker([latitude, longitude]).add_to(map)
            map.save('templates/map.html')
            return render_template('map.html')
        else:
            return "Image does not contain location information"
    else:
        return "No image uploaded"

def _convert_to_degrees(value):
    d = float(value.values[0].num) / float(value.values[0].den)
    m = float(value.values[1].num) / float(value.values[1].den)
    s = float(value.values[2].num) / float(value.values[2].den)
    return d + (m / 60.0) + (s / 3600.0)

if __name__ == '__main__':
    app.run(debug=True)
