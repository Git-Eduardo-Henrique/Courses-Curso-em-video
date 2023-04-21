use cadastro;

select * from cursos;

select * from cursos order by nome asc;
select * from cursos order by nome desc;

select nome, carga, ano from cursos order by ano, nome desc;

select nome, descricao, carga from cursos where ano = "2019" order by nome desc;
select nome, descricao, carga from cursos where ano <= "2015" order by nome desc;

select nome, descricao, totaulas from cursos where totaulas between 20 and 30 order by nome desc;
select nome, descricao, ano from cursos where ano in ("2015", "2019") order by nome desc;

# aula 12

select nome from cursos where nome like "P%";
select nome from cursos where nome like "%A";
select nome from cursos where nome like "%A%";

select distinct nacionalidade from gafanhotos order by nacionalidade;

select count(*) from cursos;

select max(carga) from cursos;
select min(carga) from cursos;
select sum(totaulas) from cursos;
select avg(totaulas) from cursos;

# aula 13
select carga from cursos group by carga order by carga desc;
select carga, count(nome) from cursos group by carga order by count(nome) desc;

select carga, count(nome) from cursos group by carga having carga > (select avg(carga) from cursos) order by count(nome) desc;

select ano, count(*) from cursos group by ano having count(*) >= 5;