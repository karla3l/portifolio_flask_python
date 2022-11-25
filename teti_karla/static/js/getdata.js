function getdata(){
    const req = new XMLHttpRequest();
    // req.open("GET", "HTTP://10.8.39.157:5000/getdata", false)
    req.open("GET", "http://10.8.39.157:5000/api-teti?token=ABC", false)
    req.send();
    return req.responseText
}
function resultado(){
    const resultado = document.getElementById('resultado')
    let dados = getdata()
    resultado.innerHTML = `<h2> ${ dados } </h2>`
}