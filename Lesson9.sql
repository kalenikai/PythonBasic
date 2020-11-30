-- В базе данных shop и sample присутствуют одни и те же таблицы, учебной базы данных. 
-- Переместите запись id = 1 из таблицы shop.users в таблицу sample.users. Используйте транзакции.
use shop;

delimiter ;
start transaction;
	insert into sample.users 
    select * from shop.users
    where id = 1;
commit;
    
-- Создайте представление, которое выводит название name товарной позиции из таблицы products и соответствующее название каталога name из таблицы catalogs.    
create view v_getProductName 
as
	select p.name, c.name
    from products p
    inner join catalogs c on p.catalog_id = c.id;
    
-- Пусть имеется таблица с календарным полем created_at. 
-- В ней размещены разряженые календарные записи за август 2018 года '2018-08-01', '2016-08-04', '2018-08-16' и 2018-08-17. 
-- Составьте запрос, который выводит полный список дат за август, выставляя в соседнем поле значение 1, если дата присутствует в исходном таблице и 0, если она отсутствует.

select p.*, case
				when created_at is not null then 1
				when created_at is null then 0
             end as 'Status'   
from products p;

-- Пусть имеется любая таблица с календарным полем created_at. 
-- Создайте запрос, который удаляет устаревшие записи из таблицы, оставляя только 5 самых свежих записей.

delete 
from products 
where id not in (select id from products order by created_at desc limit 5);
        
-- Создайте двух пользователей которые имеют доступ к базе данных shop. 
-- Первому пользователю shop_read должны быть доступны только запросы на чтение данных, 
-- второму пользователю shop — любые операции в пределах базы данных shop.

CREATE USER shop_read IDENTIFIED WITH sha256_password BY 'pass';
GRANT SELECT ON *.* TO shop_read;

CREATE USER shop IDENTIFIED WITH sha256_password BY 'pass';
GRANT ALL ON *.* TO shop;

 
-- Пусть имеется таблица accounts содержащая три столбца id, name, password, содержащие первичный ключ, имя пользователя и его пароль. 
-- Создайте представление username таблицы accounts, предоставляющий доступ к столбца id и name. 
-- Создайте пользователя user_read, который бы не имел доступа к таблице accounts, однако, мог бы извлекать записи из представления username.
create view v_username
as
	select id, name
    from accounts;
    
CREATE USER user_read IDENTIFIED WITH sha256_password BY 'pass';
REVOKE SELECT, DELETE, INSERT, DELETE ON accounts FROM user_read;
GRANT SELECT ON v_username TO user_read;

-- Создайте хранимую функцию hello(), которая будет возвращать приветствие, в зависимости от текущего времени суток. 
--  С 6:00 до 12:00 функция должна возвращать фразу "Доброе утро", 
-- с 12:00 до 18:00 функция должна возвращать фразу "Добрый день", 
-- с 18:00 до 00:00 — "Добрый вечер", 
-- с 00:00 до 6:00 — "Доброй ночи".

delimiter //
create function hello()
RETURNS TEXT DETERMINISTIC
begin
	declare current time(0);
    declare msg varchar(20);
    set current = HOUR(now());
	if (current >= 6 and current <12) then
		set msg = 'Доброе утро';
    elseif (current >= 12 and current <18) then
		set msg = 'Добрый день';
    elseif (current >= 18 and current <=23) then
		set msg = 'Добрый вечер';
    elseif (current >= 0 and current <6) then
		set msg = 'Добрый ночи';
    end if;
    return msg;
end//			
delimiter ;
select hello();
    

delimiter //
-- Напишите хранимую функцию для вычисления произвольного числа Фибоначчи. 
-- Числами Фибоначчи называется последовательность в которой число равно сумме двух предыдущих чисел. 
-- Вызов функции FIBONACCI(10) должен возвращать число 55.

-- Это не рекурсивная функция. Рекурсивную было писать лень. :)

CREATE function fibonaci(n INT)
returns int DETERMINISTIC
begin
  declare m int default 0;
  declare k int DEFAULT 1;
  declare i int;
  declare tmp int;
  set m=0;
  set k=1;
  set i=1;
  while (i<=n) do
    SET tmp=m+k;
    SET m=k;
    SET k=tmp;
    SET i=i+1;
  end while;
  return m;
 end//
 
delimiter ;
select fibonaci(10);

