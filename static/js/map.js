map = "";
polyline = "";
info = document.getElementById('info');
last = {};
window.onload = () => {
    loadmap();
    getPos();
    setInterval(getPos,10000);
}

loadmap = () => {
         map = L.map('map').setView([47.0024, 7.0126], 10);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);
}

async function getPos(){
        let latlngs = [];
        if(polyline != ""){
            map.removeLayer(polyline);
        }
        let data = await (await fetch('http://panama.internet-box.ch/gps')).json();
        if (data.length != 0){
          for(let i= 0; i < data.length; i++){
            if(data[i].lat !=0 && data[i].long!=0){
              latlngs.push(new L.LatLng(data[i].lat, data[i].long));
              last[data[i].name] = data[i].date;
            }
          }
          info.innerHTML = "";
          for (const [key, value] of Object.entries(last)) {
            let date = new Date(value*1000)
                info.innerHTML += `<p>Last update <b>${key}</b> : ${date.getDate()}.${date.getMonth()}.${date.getFullYear()} ${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}</p>`
          }
          polyline = L.polyline(latlngs, {color: 'red'});
          map.addLayer(polyline);
        }
}