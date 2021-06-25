picture = document.getElementById('picture');

async function getPicture(){
        let data = await (await fetch('http://panama.internet-box.ch/image')).json();
        if (data.length != 0){
          for(let i= 0; i < data.length; i++){
               let date = new Date(data[i].date*1000)
             picture.innerHTML += `<img src="/static/img/${data[i].id}.jpg" alt="${data[i].id}" width="320" height="240">
               <p>date :  ${date.getDate()}.${date.getMonth()}.${date.getFullYear()} ${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}</p>`
          }


        }
}