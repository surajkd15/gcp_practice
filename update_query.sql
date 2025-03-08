update {{dataset}}.prac_1
set gender = "M"
where state='CA';



DELETE from {{dataset}}.prac_1
where state='AK';
