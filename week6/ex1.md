## Find the names of suppliers who supply some red part.

SELECT DISTINCT(sname)
FROM "Ex1"."Suppliers" as S, "Ex1"."Catalog" as C, "Ex1"."Parts" as P
WHERE S.sid = C.sid and C.pid = P.pid and P.color = 'Red'

_Output: Devil’s canyon, AZ, RR Asylum, NV_

## Find the sids of suppliers who supply some red or green part.

SELECT DISTINCT(S.sid)
FROM "Ex1"."Suppliers" as S, "Ex1"."Catalog" as C, "Ex1"."Parts" as P
WHERE S.sid = C.sid and C.pid = P.pid and (P.color = 'Red' or P.color = 'Green');

_Output: 1, 2_

## Find the sids of suppliers who supply some red part or are at 221 Packer Street

SELECT DISTINCT(S.sid)
FROM "Ex1"."Suppliers" as S, "Ex1"."Catalog" as C, "Ex1"."Parts" as Pa
WHERE (S.sid = C.sid and C.pid = P.pid and P.color = 'Red')
or S.address LIKE '%221 Packer Street%';

_Output: 1, 2_

## Find the sids of suppliers who supply every red or green part.

Select DISTINCT(C.sid)
FROM "Ex1"."Catalog" as C
WHERE NOT EXISTS (
SELECT P.pid
FROM "Ex1"."Parts" as P
WHERE (P.color = 'Red' OR P.color = 'Green')
AND (NOT EXISTS (
SELECT C2.sid
FROM "Ex1"."Catalog" as C2
WHERE C2.sid = C.sid AND C2.pid = P.pid
))
)

_Output: 1_

## Find the sids of suppliers who supply every red part or supply every green part

Select DISTINCT(C.sid)
FROM "Ex1"."Catalog" as C
WHERE (NOT EXISTS (
SELECT P.pid
FROM "Ex1"."Parts" as P
WHERE (P.color = 'Red')
AND (NOT EXISTS (
SELECT C2.sid
FROM "Ex1"."Catalog" as C2
WHERE C2.sid = C.sid AND C2.pid = P.pid
))
)) OR (NOT EXISTS (
SELECT P.pid
FROM "Ex1"."Parts" as P
WHERE (P.color = 'Green')
AND (NOT EXISTS (
SELECT C2.sid
FROM "Ex1"."Catalog" as C2
WHERE C2.sid = C.sid AND C2.pid = P.pid
))
))

_Output: 1, 2_

## Find pairs of sids such that the supplier with the first sid charges more for some part than the supplier with the second sid.

SELECT DISTINCT(C1.sid, C2.sid)
FROM "Ex1"."Catalog" as C1,
"Ex1"."Catalog" as C2
WHERE C1.pid= C2.pid and C1.sid != C2.sid
and C1.cost > C2.cost;

_Output: (1,2), (2,1)_

## Find the pids of parts supplied by at least two different suppliers.

SELECT DISTINCT(C.pid)
FROM "Ex1"."Catalog" as C
WHERE EXISTS (
SELECT C2.sid
FROM "Ex1"."Catalog" as C2
WHERE C.sid != C2.sid AND C.pid = C2.pid
)

_Output: 1, 3, 5_

## Find the average cost of the red parts and green parts for each of the suppliers

SELECT C.sid, P.color, AVG(C.cost) as average_cost
FROM "Ex1"."Catalog" as C, "Ex1"."Parts" as P
WHERE C.pid = P.pid AND (P.color = 'Red' OR P.color = 'Green')
GROUP BY C.sid, P.color

_Output: check output8.jpg_

## Find the sids of suppliers whose most expensive part costs $50 or more

SELECT DISTINCT(C.sid)
FROM "Ex1"."Catalog" as C
WHERE C.cost >= 50.0

_Output: 1_
