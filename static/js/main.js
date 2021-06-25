window.onload = () => {
    loadmap();
    getPos();
    getPicture();
    setInterval(interval,10000);
}

function interval(){
    getPos();
    getPicture();
}