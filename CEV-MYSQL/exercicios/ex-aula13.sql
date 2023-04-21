use cadastro;
select * from gafanhotos;
describe gafanhotos;

# ex - 01
select profissao, count(*) as num_pessoas from gafanhotos group by profissao order by count(*) desc;

# ex - 02
select sexo, count(sexo) as depois_de_2005 from gafanhotos where nascimento > "2005-01-01" group by sexo;

# ex - 03
select nacionalidade, count(*) as pessoas from gafanhotos where nacionalidade <> "Brasil" group by nacionalidade 
having count(*) > 3 order by count(*) desc;

# ex - 04
select altura, count(*) as mais_100kg from gafanhotos where peso > 100 group by altura 
having (select avg(altura) from gafanhotos) order by peso desc;