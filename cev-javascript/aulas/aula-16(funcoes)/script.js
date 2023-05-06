function parimpar(num){
    if (num % 2 == 0){
        return "par"
    } else{
        return "impar"
    }
}

function soma(n1=0, n2=0){
    return n1 + n2
}

let v = function(x){
    return x * 2
}

let res = parimpar(4)
console.log(res)

console.log(soma(5, 6))

console.log(v(3))