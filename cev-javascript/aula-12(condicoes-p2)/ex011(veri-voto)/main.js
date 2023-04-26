var idade = 22

console.log(`você tem ${idade} anos e`)

if (idade >= 18 && idade < 65){
    console.log("Tem que votar")
} else if (idade >= 16 || idade >= 65){
    console.log("pode votar se quiser")
} else {
    console.log("não pode votar")
}