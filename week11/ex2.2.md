# 2 Read committed

## Step 1

BEGIN; -- both
set transaction ISOLATION LEVEL Read committed; -- both

## Step 2

SELECT \* FROM account2 WHERE group_id = 2; -- 1

### output 1
 username |   fullname   | balance | group_id
----------+--------------+---------+----------
 mike     | Michael Dole |      73 |        2


## Step 3

UPDATE account2 SET group_id = 2 WHERE fullname = 'Bob Brown'; -- 2

## Step 4

SELECT \* FROM account2 WHERE group_id = 2; -- 1

### output 1
 username |   fullname   | balance | group_id
----------+--------------+---------+----------
 mike     | Michael Dole |      73 |        2

## Step 5

UPDATE account2 SET balance = balance+15 WHERE group_id = 2; -- 1

## Step 6

COMMIT; --both
SELECT * FROM account2 WHERE group_id = 2; -- both

## output 1 & 2
 username |   fullname   | balance | group_id
----------+--------------+---------+----------
 bbrown   | Bob Brown    |     100 |        2
 mike     | Michael Dole |      88 |        2

# 2 Repeatable read

BEGIN; -- both
set transaction ISOLATION LEVEL Repeatable read; -- both

## Step 2

SELECT \* FROM account2 WHERE group_id = 2; -- 1

### output 1
 username |   fullname   | balance | group_id
----------+--------------+---------+----------
 bbrown   | Bob Brown    |     100 |        2
 mike     | Michael Dole |      88 |        2

## Step 3

UPDATE account2 SET group_id = 2 WHERE fullname = 'Alice Jones'; -- 2

## Step 4

SELECT \* FROM account2 WHERE group_id = 2; -- 1

### output 1
 username |   fullname   | balance | group_id
----------+--------------+---------+----------
 bbrown   | Bob Brown    |     100 |        2
 mike     | Michael Dole |      88 |        2

## Step 5

UPDATE account2 SET balance = balance+15 WHERE group_id = 2; -- 1

## Step 6

COMMIT; --both
SELECT * FROM account2 WHERE group_id = 2; -- both

## output 1 & 2
 username |   fullname   | balance | group_id
----------+--------------+---------+----------
 bbrown   | Bob Brown    |     115 |        2
 mike     | Michael Dole |     103 |        2
 jones    | Alice Jones  |     107 |        2