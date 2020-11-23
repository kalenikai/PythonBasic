-- Составьте список пользователей users, которые осуществили хотя бы один заказ orders в интернет магазине.
select u.name
from users u
inner join  orders o on u.id = o.user_id;

-- Выведите список товаров products и разделов catalogs, который соответствует товару.
select p.name, c.name
from catalogs c
inner join products p on c.id = p.catalog_id;

-- Пусть имеется таблица рейсов flights (id, from, to) и таблица городов cities (label, name). 
-- Поля from, to и label содержат английские названия городов, поле name — русское. 
-- Выведите список рейсов flights с русскими названиями городов.
select f.id, c.name
from flights f
inner join cities c on f.from = c.label;
 

