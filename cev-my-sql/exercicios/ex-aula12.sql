use cadastro;
describe gafanhotos;

# ex - 01
select nome from gafanhotos where sexo = "F" order by nome;



# ex - 02
select nome, nascimento from gafanhotos where nascimento between "2000-01-01" and "2015-12-31" order by nascimento;

# ex - 03
select nome, profissao from gafanhotos where profissao = "Programador" order by nome;

# ex -  04
select sexo, nome, nacionalidade from gafanhotos where sexo = "F" and nacionalidade = "Brasil" and nome like "j%";

# ex - 05
select nome, nacionalidade from gafanhotos where sexo = "M" and nome like"%Silva%" and nacionalidade != "Brasil" and peso < 100;

# ex - 06
select max(altura) from gafanhotos where sexo = "M" and nacionalidade = "Brasil";

# ex - 07
select avg(peso) from gafanhotos;

# ex - 08
select min(peso) from gafanhotos where sexo = "F" and nacionalidade <> "Brasil" and nascimento between "1990-01-01" and "2000-12-31";

# ex - 09
select count(*) from gafanhotos where altura >= 1.90;