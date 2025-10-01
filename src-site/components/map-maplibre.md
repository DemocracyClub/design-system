---
title: Map (Maplibre)
---

<link href="https://unpkg.com/maplibre-gl@^5.7.3/dist/maplibre-gl.css" rel="stylesheet" integrity="sha256-Q8HYhrX98KrE5xNb1vhLgj2fSCg6ZIASZl+b5SwBOJ8=" crossorigin=""/>
<script src="https://unpkg.com/maplibre-gl@^5.7.3/dist/maplibre-gl.js" integrity="sha256-/Ze3rEckk2nOh+JKg3ReMZWTVxlO83FchrHF+EyCS7Y" crossorigin=""></script>

Use the Maplibre Map component to show the user geographic information with <a href="https://maplibre.org/maplibre-gl-js/docs/" target="_blank">Maplibre</a>. Unlike Leaflet.js, Maplibre supports interactive layers when displaying pmtiles. However, it is a slightly larger library. 

An example of a maplibre map in the wild:
- In a card, showing a multi-layer pmtiles file (with a layer toggle): <a href="https://elections.democracyclub.org.uk/organisations/divisionsets/822/">Every Election</a>


{% ds-example %}
    <div id="map" class="ds-map-maplibre"></div>
{% endds-example %}

<script>
    var style = {
                    "version": 8,
                    "sources": {
                        "os": {
                            "type": "raster",
                            "tiles": [
                                "https://tile.openstreetmap.org/{z}/{x}/{y}.png"
                            ],
                            "tileSize": 256,
                            "attribution": "© OpenStreetMap contributors"
                        },
                    },
                    layers: [
                        {
                            "id": "os-baselayer",
                            "type": "raster",
                            "source": "os",
                            "minzoom": 0,
                            "maxzoom": 19
                        }
                    ]
                }

    // light mode
    const map = new maplibregl.Map({
                    container: 'map',
                    center: [-0.09, 51.515], 
                    zoom: 13,
                    style: style,
                });
    // dark mode
    const dark_map = new maplibregl.Map({
                        container: 'dark_map',
                        center: [-0.09, 51.515], 
                        zoom: 13,
                        style: style,
                    });

</script>

```html
Here’s a demo:
    <div id="map" class="ds-map-maplibre"></div>
```
