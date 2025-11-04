// Initialize map
var map = L.map('map').setView([28.6139, 77.2090], 13);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution: '© OpenStreetMap'
}).addTo(map);

var busMarker = L.marker([28.6139, 77.2090]).addTo(map)
  .bindPopup("🚌 Bus #001 - Live Location").openPopup();

function updateBusLocation() {
  fetch('http://127.0.0.1:5000/api/location/BUS001')
    .then(res => res.json())
    .then(data => {
      const lat = data.latitude;
      const lon = data.longitude;
      busMarker.setLatLng([lat, lon]);
      map.setView([lat, lon], 14);
    })
    .catch(() => console.log("Error fetching live location"));
}

// Update every 5 seconds
setInterval(updateBusLocation, 5000);
