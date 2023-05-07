let amigo = {nome: "jose", sexo: "M", peso: 85.5, engordar(p=0){
    this.peso += p
}}
amigo.engordar(3)
console.log(amigo)