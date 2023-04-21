use cadastro;

describe gafanhotos;
describe cursos;
select * from gafanhotos;
select * from cursos;

# aula 15
alter table gafanhotos add idcurso_fav int;
alter table gafanhotos add foreign key(idcurso_fav) references cursos(idcurso);

update gafanhotos set idcurso_fav = "6" where id = "1";

select gafanhotos.nome, gafanhotos.idcurso_fav, cursos.nome from gafanhotos 
join cursos on cursos.idcurso = gafanhotos.idcurso_fav order by gafanhotos.nome;

select gafanhotos.nome, gafanhotos.idcurso_fav, cursos.nome from gafanhotos 
left join cursos on cursos.idcurso = gafanhotos.idcurso_fav order by gafanhotos.nome;