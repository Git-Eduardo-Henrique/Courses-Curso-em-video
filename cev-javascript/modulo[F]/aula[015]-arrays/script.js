let num = [5, 2, 9, 3]

num[4] = 7
// adiciona um valor no array
num.push(0)

// length = mostra o tamanho do vetor
console.log(`valores do vetor: ${num} | tamanho do vetor: ${num.length}`)
// sort() = deixa em order crescente
console.log(`vetor em order crescente: ${num.sort()}`)
// indexOf = procura o valor em um array
console.log(`o valor 5 esta na posição ${num.indexOf(5)}`)

for (let pos = 0; pos < num.length; pos++){
    console.log(`${pos} = ${num[pos]}`)
}

for (let pos in num){
    console.log(`${pos} = ${num[pos]} (versao simples)`)
}