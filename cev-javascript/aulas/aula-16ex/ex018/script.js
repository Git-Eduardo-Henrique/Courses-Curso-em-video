var list = []

function checar_lista(n){
    for (let pos in list){
        if (list[pos] == n){
            window.alert("Numero já cadastrado")
            return false
        }
    } 
    return true
}

function analisar(){
    let num = document.querySelector("input#numeros")
    let slt = document.querySelector("select")
    
    number = Number(num.value)

    if (num.length == 0 || (number > 100 || number < 1)){
        window.alert("Valor invalido! tente novamente")
    } else {
        if (checar_lista(number)){
            let p = document.querySelector("p#res")
            p.innerHTML = ""
            
            list.push(number)

            let opt = document.createElement("option")
            opt.text = list[list.indexOf(number)]

            slt.appendChild(opt)
        }
    }
}

function avancar(){
    if (list.length == 0){
        window.alert("Adicione valores!!!")
    } else {
        let p = document.querySelector("p#res")
        p.innerHTML = ""
    
        p.innerHTML += `numeros cadastrados: ${list.length}<br>`
    
        p.innerHTML += `maior numero: ${Math.max(...list)} <br>`
    
        p.innerHTML += `menor numero: ${Math.min(...list)} <br>`
    
        sum = 0
        for (let pos in list){
            sum += list[pos]
        }
    
        p.innerHTML += `soma de todos os valores: ${sum}<br>` 
    
        media = 0
        for (let pos in list){
            media += list[pos]
        }
        media /= list.length
    
        p.innerHTML += `media de todos os valores: ${media}`
    }
}