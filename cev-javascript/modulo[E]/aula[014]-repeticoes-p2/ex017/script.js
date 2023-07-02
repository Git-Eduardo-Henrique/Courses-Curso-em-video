function tabuada(){
    let input = document.querySelector("input#numero")
    let select = document.querySelector("#res")

    if (input.value.length == 0){
        window.alert("Digite um numero!")
    } else {
        let num_input = Number(input.value)

        select.innerHTML = ""
        for (let n = 1; n <= 10; n++){
            let res = document.createElement("option")
            res.text = `${num_input} x ${n} = ${num_input * n}`
            select.appendChild(res)
        }
    }
}