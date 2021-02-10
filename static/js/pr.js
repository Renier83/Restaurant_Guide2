console.log("pr.js");

// var mymap = L.map('mapid').setView([18.220833, -66.590149], 10);

// Create a map object
var mymap = L.map("mapid", {
    center: [18.220833, -66.590149],
    zoom: 10
});

console.log(mymap);

// Define greymap layers
// L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
//     attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
//     tileSize: 512,
//     maxZoom: 18,
//     zoomOffset: -1,
//     id: "mapbox/streets-v11",
//     accessToken: API_KEY
// }).addTo(myMap);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: API_KEY
}).addTo(mymap);

// Change to San Juan information
//18.466333, -66.105721]
// var rinmap = L.map('rnid').setView([18.340111, -67.249947], 13);
// var ponceCoords = [18.012630, -66.626038];
// var farmap = L.map('frid').setView([18.330379, -65.660606], 13);
// var arecibomap = L.map('arid').setView([18.470440, -66.722282], 13);

san_juan = [18.466333, -66.105721, '<a href="/city/San Juan">San Juan<a>']
ponce = [18.01108, -66.61406, '<a href="/city/Ponce">Ponce<a>']
rincon = [18.340216, -67.250015, '<a href="/city/Rincon">Rincon<a>']
fajardo = [18.325787, -65.652382, '<a href="/city/Fajardo">Fajardo<a>']
arecibo = [18.47245, -66.71573, '<a href="/city/Arecibo">Arecibo<a>']
humacao = [18.148750, -65.819099, '<a href="/city/Humacao">Humacao<a>']
mayaguez = [18.201349, -67.139488, '<a href="/city/Mayaguez">Mayaguez<a>']

cities = [san_juan, ponce, rincon, fajardo, arecibo, humacao, mayaguez]

cities.forEach(d => {
    console.log(d);
    var coords = [d[0], d[1]];
    var city = d[2];

    marker = L.marker(d).addTo(mymap);
    marker.bindPopup(`${coords}<hr/>${city}<br>`)
    marker.addTo(mymap);
});


// ALL MARKERS

// d3.json('/api/restaurants').then(data => {
//     console.log(data);

//     data.forEach(d => {

//         var coords = [d['lat'], d['lng']];
//         var name = d['name'];
//         var address = d['address'];

//         marker = L.marker(coords, { 'title': name });
//         marker.bindPopup(`<h4>${name}</h4><hr/><b>${address}</b>`)
//         marker.addTo(mymap);



//         //mymap.setZoom(13);
//         //mymap.setView(new L.LatLng(ponceCoords[0], ponceCoords[1]), 13)




//     });
// });