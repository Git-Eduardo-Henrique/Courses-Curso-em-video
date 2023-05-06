function contar(){
    // let = so existe dentro da função
    let inicio = document.querySelector("input#inicio")
    let final = document.querySelector("input#final")
    let passo = document.querySelector("input#passo")

    let res = document.querySelector("p.res")
    res.innerHTML = ""

    // verifica se tudo foi digitado
    if (inicio.value.length == 0 || final.value.length == 0 || passo.value.length == 0){
        window.alert("Complete todos os dados!!")
    } else {
        let inicio_num = Number(inicio.value)
        let final_num = Number(final.value)
        let passo_num = Number(passo.value)

        if (passo_num <= 0){
            passo_num = 1
            res.innerHTML = "Considerando passo 1 <br>"
        }

        if (inicio_num < final_num){
            console.log("aaaa1")
            for (var i = inicio_num; i <= final_num; i += passo_num){
                res.innerHTML += ` ${i} \u{1f449}`
                console.log("aaaa1 1")
            }
        } else {
            console.log("aaaa2")
            for (var i = inicio_num; i >= final_num; i -= passo_num){
                res.innerHTML += ` ${i} \u{1f449}`
                console.log("aaaa2 2")
            }
        }
        // \u{} -> adiciona um emoji
        res.innerHTML += "\u{1f3c1}"
    }
}
   