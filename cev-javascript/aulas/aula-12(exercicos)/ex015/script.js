function verificar(){
    var agora = new Date().getFullYear()
    var nasc = document.querySelector("input#data")
    var res = document.querySelector("div.res")
    var pres = document.querySelector("p#pres") 

    if (nasc.value.length == 0 || nasc.value > agora){
        window.alert("verifique e tente novamente!")
    } else {
        var sex = document.getElementsByName("radsex")
        var idade = agora - Number(nasc.value)
     
        var img = document.createElement("img")
        img.setAttribute("id", "foto")
        var genero = ""

        if (sex[0].checked){
            genero = "homem"
        } else {
            genero = "mulher"
        }

        pres.innerHTML = `você é ${genero} com ${idade} anos!`
        img.style.height = "15vh"

        if (idade < 4){
            img.setAttribute("src", `images/${genero}/${genero}-bebe.jpg`)
        } else if (idade < 12){
            img.setAttribute("src", `images/${genero}/${genero}-crianca.jpg`)
        } else if (idade < 18){
            img.setAttribute("src", `images/${genero}/${genero}-adolecente.jpg`)
        } else if (idade < 50){
            img.setAttribute("src", `images/${genero}/${genero}-adulto.jpg`)
        } else {
            img.setAttribute("src", `images/${genero}/${genero}-idoso.jpg`)
        }
        
        res.appendChild(img)
    }
}