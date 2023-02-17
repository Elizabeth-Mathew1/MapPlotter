# MapPlotter
A basic mapplotter using folium and is rendered using flask.
# :world_map:  MapPlotter
#### A simple mapplotter that takes user input images and extracts geo-location from the EXIF data and plots it on the map.

### :mortar_board:  About the project

This is a simple web application for uploading images and plotting their locations on maps. The application uses the Flask web framework and the Jinja2 template language.

The different stages of the project included:
  1) Taking user input in the form of images
  2) Extracting geo-location from EXIF data using exifread
  3) Plotting obtained coordinates on a map using folium marker
  4) Rendered using flask
  


---
### :pencil2: Requirements

1) Python 2.7 or greater
2) Flask
3) Jinja2
4) Exifreader

and a few other libraries and dependencies.

---
### :dart: Usage

1) Clone the repository:
```
git clone https://github.com/Elizabeth-Mathew1/MapPlotter/
```
2) Install the required packages:
```
pip install flask jinja2 exifread
```
3)Run the application:
```
export FLASK_APP=exif_map_plotter.py
flask run
```
Visit the application in your web browser at ```http://localhost:5000/```.




---
### :circus_tent: Screenshots
1) Opening Screen
[![Screenshot-2023-02-10-at-10-53-11-PM.png](https://i.postimg.cc/3NyWfbXt/Screenshot-2023-02-10-at-10-53-11-PM.png)](https://postimg.cc/CngFz768)

2) Choosing file
[![Screenshot-2023-02-10-at-10-53-24-PM.png](https://i.postimg.cc/BbDPQVjX/Screenshot-2023-02-10-at-10-53-24-PM.png)](https://postimg.cc/m1LgmVNs)

3) After uploading image
[![Screenshot-2023-02-10-at-10-53-36-PM.png](https://i.postimg.cc/wTGQBS4j/Screenshot-2023-02-10-at-10-53-36-PM.png)](https://postimg.cc/3d2vSbHs)

4) Plotting on map-Zoomed In

[![Screenshot-2023-02-10-at-10-53-49-PM.png](https://i.postimg.cc/yY17NGgt/Screenshot-2023-02-10-at-10-53-49-PM.png)](https://postimg.cc/Z0MG7VLx)

4) Plotting on map-Zoomed Out
[![Screenshot-2023-02-10-at-10-54-01-PM.png](https://i.postimg.cc/pXT34MnW/Screenshot-2023-02-10-at-10-54-01-PM.png)](https://postimg.cc/8s2yf3H9)
