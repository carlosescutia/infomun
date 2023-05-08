{% load static %}
// crear layer openstreetmap
var backgUrl = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
backgAttrib = '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>';
var backg_lyr = L.tileLayer(backgUrl, {maxZoom: 18, attribution: backgAttrib});                        

// crear capa_municipios desde geojson
var capa_municipios = new L.GeoJSON.AJAX("{% static 'infomun/js/municipios_gto.geojson' %}", {
    style: style,
    onEachFeature: onEachFeature
});

function style(feature){
    cve_mun = "{{ municipio.cve_mun }}";
    if (feature.properties.CVE_MUN == cve_mun ) {
        return {
            fillColor: '#00f',
            weight: 2,
            opacity: 1,
            color: '#00f',
            dashArray: '',
            fillOpacity: 0.8
        };
    } else {
        return {
            weight: 1,
            opacity: 0.5,
            color: '#000',
            fillOpacity: 0
        };
    }
}

function onEachFeature(feature, layer) {
    layer.on({
        mouseover: highlightFeature,
        mouseout: resetHighlight,
        click: function(e){
            baseurl = '/infomun/';
            newmun = feature.properties.CVE_MUN;
            url = baseurl + newmun;
            window.open(url, '_self');
        }
    });
}

// control de informacion
var info = L.control();
info.onAdd = function(map) {
    this._div = L.DomUtil.create('div', 'info');
    this.update();
    return this._div;
}

info.update = function(props) {
    this._div.innerHTML = (props ? '<b>' + props.NOM_MUN + '</b>' : 'Seleccione un municipio');
}

function highlightFeature(e) {
    var layer = e.target;

    layer.setStyle({
        weight: 4,
        color: '#00f',
        dashArray: '',
        fillOpacity: 0.2
    });

    if (!L.Browser.ie && !L.Browser.opera) {
        layer.bringToFront();
    }

    info.update(layer.feature.properties);
}

function resetHighlight(e) {
    capa_municipios.resetStyle(e.target);
    info.update();
}

// crear mapa en el div "mapa_municipios" y centrarlo en Guanajuato
var map = L.map('mapa_municipios', {
center: new L.LatLng(20.89304, -100.84788), 
zoom: 8,
zoomControl: false,
scrollWheelZoom: false,
dragging: false,
layers: [backg_lyr, capa_municipios]
});

// agregar control info
info.addTo(map);

// ajustar visualizacion del mapa al tamaño de ventana
capa_municipios.on('data:loaded', function() {
    map.fitBounds(capa_municipios.getBounds(), {animate:false})
})

