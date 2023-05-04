function confirmar(){
    var inicio = document.querySelector("input#inicio")
    var final = document.querySelector("input#final")
    var passo = document.querySelector("input#passo")

    var inicio_num = Number(inicio.value)
    var final_num = Number(final.value)
    var passo_num = Number(passo.value)

    var res = document.querySelector("p.res")
    res.innerHTML = ""

    for (var i = inicio_num; i <= final_num; i += passo_num){
        res.innerHTML += `${i} |`
    }
}
   