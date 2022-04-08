# query 1

SELECT film.film_id, film.title
FROM film, film_category, category
WHERE (film.rating = 'R' OR film.rating = 'PG-13') AND
film_category.film_id = film.film_id AND
film_category.category_id = category.category_id AND
(category.name ='Horror' OR category.name = 'Sci-Fi' ) AND
film.film_id NOT IN ( SELECT DISTINCT(inventory.film_id)
FROM rental JOIN inventory ON (rental.inventory_id = inventory.inventory_id)
);

# output

check ex2.output1.jpg

# analysis

The most expensive steps were sequential scanning
This can be fixed by using Indexes

# query 2

SELECT city.city, storeInfo.store_id, maxCityInfo.max_payment_sum
FROM (
SELECT store.store_id, store.address_id, SUM(payment.amount) as payment_sum
FROM (payment JOIN staff ON payment.staff_id = staff.staff_id)
JOIN store ON (store.store_id = staff.staff_id )
GROUP BY store.store_id) as storeInfo,
(
SELECT city.city_id, MAX(storeInfo.payment_sum) as max_payment_sum
FROM city JOIN address ON (city.city_id = address.city_id) JOIN
(
SELECT store.store_id, store.address_id, SUM(payment.amount) as payment_sum
FROM (payment JOIN staff ON payment.staff_id = staff.staff_id)
JOIN store ON (store.store_id = staff.staff_id )
GROUP BY store.store_id) as storeInfo ON (address.address_id = storeInfo.address_id)
GROUP BY city.city_id
) as maxCityInfo,
city, address
WHERE city.city_id = address.city_id AND
address.address_id = storeInfo.address_id AND
maxCityInfo.city_id = city.city_id

# output

check ex2.output2.jpg

# analysis

The most expensive steps were nested loops (storeInfo, maxCityInfo)
This can be fixed by using memorization, if is is possible in sql
