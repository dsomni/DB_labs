## Creation SQL

CREATE TABLE "Ex1"."Items"(
itemId INTEGER PRIMARY KEY,
itemName TEXT
);

CREATE TABLE "Ex1"."Cities"(
cityId INTEGER PRIMARY KEY,
cityName TEXT
);

CREATE TABLE "Ex1"."Customers"(
customerId INTEGER PRIMARY KEY,
customerName TEXT,
cityId INTEGER,
FOREIGN KEY (cityId) REFERENCES "Ex1"."Cities"(cityId)
);

CREATE TABLE "Ex1"."Orders"(
orderId INTEGER PRIMARY KEY,
customerId INTEGER,
orderDate DATE,
FOREIGN KEY (customerId) REFERENCES "Ex1"."Customers"(customerId)
);

CREATE TABLE "Ex1"."Purchases"(
orderId INTEGER,
itemId INTEGER,
quant INTEGER,
price REAL,
PRIMARY KEY (orderId, itemId),
FOREIGN KEY (orderId) REFERENCES "Ex1"."Orders"(orderId),
FOREIGN KEY (itemId) REFERENCES "Ex1"."Items"(itemId)
);

## Insertion SQL

INSERT INTO "Ex1"."Cities"(
cityid, cityname)
VALUES
(0, 'Prague'),
(1, 'Madrid'),
(2, 'Moscow');

INSERT INTO "Ex1"."Items"(
itemId, itemName)
VALUES
(3786, 'Net'),
(4011, 'Racket'),
(9132, 'Pack-3'),
(5794, 'Pack-6'),
(3141, 'Cover');

INSERT INTO "Ex1"."Customers"(
customerId, customerName, cityId)
VALUES
(101, 'Martin', 0),
(107, 'Herman', 1),
(110, 'Pedro', 2);

INSERT INTO "Ex1"."Orders"(
orderId, customerId, orderDate)
VALUES
(2301, 101, '2011-02-23'),
(2302, 107, '2011-02-25'),
(2303, 110, '2011-02-27');

INSERT INTO "Ex1"."Purchases"(
orderId, itemId, quant, price)
VALUES
(2301, 3786,3,35.0),
(2301, 4011,6,65.0),
(2301, 9132,8,4.75),
(2302, 5794,4,5.0),
(2303, 4011,2,65.0),
(2303, 3141,2,10.0);

## Queries

### Calculate the total number of items per order and the total amount to pay for the order.

#### query

SELECT P.orderId, SUM(P.quant) AS totalQuantity, SUM (P.price) AS totalPrice
FROM "Ex1"."Orders" as O
LEFT JOIN "Ex1"."Purchases" as P ON O.orderId = P.orderId
GROUP BY P.orderId

#### output

check ex1.output1.jpg
