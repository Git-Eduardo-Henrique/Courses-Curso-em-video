function datastyle(){
    var horas = new Date().getHours()
    var minutos = new Date().getMinutes()
    var segundos = new Date().getSeconds()

    var titulo = document.querySelector("header")
    var body = document.querySelector("body")
    var bloco_hora = document.querySelector("section")
    var image = document.querySelector("img")
    var p_hora = document.querySelector("h2.bloco-hora-paragrafo")

    p_hora.innerHTML = `agora são ${horas}:${minutos}:${segundos}`

    if (horas < 6){
        body.style.background = "black"
        bloco_hora.style.background = "white"
        p_hora.style.color = "black"
        titulo.style.color = "white"
        image.src = "images/madru.jpg"
    } else if (horas < 12) {
        body.style.background = "#BF2626"
        bloco_hora.style.background = "#F29E38"
        p_hora.style.color = "#BF2626"
        titulo.style.color = "#F2B138"
        image.src = "images/manha.jpg"
    } else if (horas < 18){
        body.style.background = "#B55931"
        bloco_hora.style.background = "#704D45"
        p_hora.style.color = "#171518"
        titulo.style.color = "#171518"
        image.src = "images/tarde.jpg"
    } else {
        body.style.background = "#0D1322"
        bloco_hora.style.background = "#96A4AE"
        p_hora.style.color = "#0D1322"
        titulo.style.color = "#DDDCDA"
        image.src = "images/noite.jpg"
    }
}