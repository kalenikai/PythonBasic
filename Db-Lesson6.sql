use snet2910;
-- Пусть задан некоторый пользователь. 
-- Из всех друзей этого пользователя найдите человека, который больше всех общался с нашим пользователем.
select initiator_user_id, target_user_id, count(*)
from friend_requests
where initiator_user_id = 1
group by initiator_user_id, target_user_id
order by 3 desc
limit 1;

-- Подсчитать общее количество лайков, которые получили 10 самых молодых пользователей.
select count(*) as 'Number likes'
from user_likes ul
join (
	select id 
    from users u 
    order by u.birtday asc 
    limit 10) u 
on ul.user_id = u.id;

-- Определить кто больше поставил лайков (всего) - мужчины или женщины?
set @female := 0;
set @male := 0;

select @female := count(*)
from user_likes ul
join users u on ul.user_id = u.id
where u.gender = 'f';

select @male := count(*)
from user_likes ul
join users u on ul.user_id = u.id
where u.gender = 'm';

select @female, @male;

-- Найти 10 пользователей, которые проявляют наименьшую активность в использовании социальной сети.
select from_user_id, count(*)
from messages
group by from_user_id
order by 2 asc
limit 10; 



