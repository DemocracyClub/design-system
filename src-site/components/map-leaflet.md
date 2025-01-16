---
title: Map (Leaflet)
---

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>

Use the Leaflet Map component to show the user geographic information with <a href="https://leafletjs.com/" target="_blank">Leaflet.js</a>. For example:

- An electoral boundary (e.g: their constituency/ward)
- The location of a place (e.g: their assigned polling station)
- The route to a place (e.g: from their house to their assigned polling station)

Some examples of leaflet maps in the wild:

- In a card, showing a route: <a href="https://wheredoivote.co.uk/example/">Where Do I Vote</a>
- In a details/summary, showing a boundary: <a href="https://elections.democracyclub.org.uk/elections/local.bath-and-north-east-somerset.2025-01-16/">Every Election</a>

{% ds-example %}
    <div id="area_map" class="ds-map-leaflet"></div>
{% endds-example %}

<script>
    // light mode
    L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 19,
        attribution:
            '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(L.map("area_map").setView([51.505, -0.09], 13));

    // dark mode
    L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 19,
        attribution:
            '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(L.map("dark_area_map").setView([51.505, -0.09], 13));
</script>

```html
Here’s a demo:

<div id="area_map" class="ds-map-leaflet"></div>
```
