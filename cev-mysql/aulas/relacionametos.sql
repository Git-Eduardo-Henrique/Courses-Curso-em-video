use cadastro;

describe gafanhotos;
describe cursos;
describe gafanhotos_cursos;
select * from gafanhotos;
select * from cursos;
select * from gafanhotos_cursos;

# aula 15
alter table gafanhotos add idcurso_fav int;
alter table gafanhotos add foreign key(idcurso_fav) references cursos(idcurso);

update gafanhotos set idcurso_fav = "6" where id = "1";

select gafanhotos.nome, gafanhotos.idcurso_fav, cursos.nome from gafanhotos 
join cursos on cursos.idcurso = gafanhotos.idcurso_fav order by gafanhotos.nome;

select gafanhotos.nome, gafanhotos.idcurso_fav, cursos.nome from gafanhotos 
left join cursos on cursos.idcurso = gafanhotos.idcurso_fav order by gafanhotos.nome;

# aula 16
create table gafanhotos_cursos(
	id int auto_increment,
    data_curso date,
    idgaf int,
    idcurso int,
    primary key(id),
    foreign key(idgaf) references gafanhotos(id),
    foreign key(idcurso) references cursos(idcurso)
);

insert into gafanhotos_cursos values 
(default, "2023-01-01", "9", "1"),
(default, "2023-01-01", "10", "2"),
(default, "2023-01-01", "12", "11"),
(default, "2023-01-01", "1", "5");

select gafanhotos.nome, gafanhotos_cursos.data_curso, gafanhotos_cursos.idcurso, cursos.nome from gafanhotos 
join gafanhotos_cursos on gafanhotos.id = gafanhotos_cursos.idgaf 
join cursos on cursos.idcurso = gafanhotos_cursos.idcurso order by gafanhotos.nome;
