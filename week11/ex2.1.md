# 1 Read committed

## Step 1

BEGIN; -- 1
set transaction ISOLATION LEVEL Read committed; -- 1
SELECT \* FROM account2; -- 1

### output 1

 username |     fullname     | balance | group_id
----------+------------------+---------+----------
 jones    | Alice Jones      |      82 |        1
 bitdiddl | Ben Bitdiddle    |      65 |        1
 mike     | Michael Dole     |      73 |        2
 alyssa   | Alyssa P. Hacker |      79 |        3
 bbrown   | Bob Brown        |     100 |        3

## Step 2

BEGIN; -- 2
set transaction ISOLATION LEVEL Read committed; -- 2
UPDATE account2 SET username = 'ajones' WHERE fullname = 'Alice Jones'; -- 2

## Step 3

SELECT \* FROM account2; -- 1

### output 1

 username |     fullname     | balance | group_id
----------+------------------+---------+----------
 jones    | Alice Jones      |      82 |        1
 bitdiddl | Ben Bitdiddle    |      65 |        1
 mike     | Michael Dole     |      73 |        2
 alyssa   | Alyssa P. Hacker |      79 |        3
 bbrown   | Bob Brown        |     100 |        3

## Step 4

SELECT \* FROM account2; -- 2

### output 2

 username |     fullname     | balance | group_id
----------+------------------+---------+----------
 bitdiddl | Ben Bitdiddle    |      65 |        1
 mike     | Michael Dole     |      73 |        2
 alyssa   | Alyssa P. Hacker |      79 |        3
 bbrown   | Bob Brown        |     100 |        3
 ajones   | Alice Jones      |      82 |        1

## Step 5

COMMIT; -- 2
SELECT \* FROM account2;

## output 1 & 2
 username |     fullname     | balance | group_id
----------+------------------+---------+----------
 bitdiddl | Ben Bitdiddle    |      65 |        1
 mike     | Michael Dole     |      73 |        2
 alyssa   | Alyssa P. Hacker |      79 |        3
 bbrown   | Bob Brown        |     100 |        3
 ajones   | Alice Jones      |      82 |        1

## Step 6

BEGIN; --2
set transaction ISOLATION LEVEL Read committed; -- 2

## Step 7

UPDATE account2 SET balance = balance + 10 WHERE fullname = 'Alice Jones'; -- 1

## Step 8

UPDATE account2 SET balance = balance + 20 WHERE fullname = 'Alice Jones'; -- 2

### here occurs some error

## Step 9

COMMIT; --1

## Step 10

ROLLBACK ; --2

## output 1 & 2
 username |     fullname     | balance | group_id
----------+------------------+---------+----------
 bitdiddl | Ben Bitdiddle    |      65 |        1
 mike     | Michael Dole     |      73 |        2
 alyssa   | Alyssa P. Hacker |      79 |        3
 bbrown   | Bob Brown        |     100 |        3
 ajones   | Alice Jones      |      92 |        1


# 1 Repeatable read

## Step 1

BEGIN; -- 1
set transaction ISOLATION LEVEL Repeatable read; -- 1
SELECT \* FROM account2; -- 1

### output 1

 username |     fullname     | balance | group_id
----------+------------------+---------+----------
 bitdiddl | Ben Bitdiddle    |      65 |        1
 mike     | Michael Dole     |      73 |        2
 alyssa   | Alyssa P. Hacker |      79 |        3
 bbrown   | Bob Brown        |     100 |        3
 ajones   | Alice Jones      |      92 |        1

## Step 2

BEGIN; -- 2
set transaction ISOLATION LEVEL Repeatable read; -- 2
UPDATE account2 SET username = 'jones' WHERE fullname = 'Alice Jones'; -- 2

## Step 3

SELECT \* FROM account2; -- 1

### output 1

 username |     fullname     | balance | group_id
----------+------------------+---------+----------
 bitdiddl | Ben Bitdiddle    |      65 |        1
 mike     | Michael Dole     |      73 |        2
 alyssa   | Alyssa P. Hacker |      79 |        3
 bbrown   | Bob Brown        |     100 |        3
 ajones   | Alice Jones      |      92 |        1

## Step 4

SELECT \* FROM account2; -- 2

### output 2

 username |     fullname     | balance | group_id
----------+------------------+---------+----------
 jones    | Alice Jones      |      92 |        1
 bitdiddl | Ben Bitdiddle    |      65 |        1
 mike     | Michael Dole     |      73 |        2
 alyssa   | Alyssa P. Hacker |      79 |        3
 bbrown   | Bob Brown        |     100 |        3

## Step 5

COMMIT; -- 2
SELECT \* FROM account2; --2

## output 1 & 2
 username |     fullname     | balance | group_id
----------+------------------+---------+----------
 jones    | Alice Jones      |      92 |        1
 bitdiddl | Ben Bitdiddle    |      65 |        1
 mike     | Michael Dole     |      73 |        2
 alyssa   | Alyssa P. Hacker |      79 |        3
 bbrown   | Bob Brown        |     100 |        3

## Step 6

BEGIN; --2
set transaction ISOLATION LEVEL Repeatable read; -- 2

## Step 7

UPDATE account2 SET balance = balance + 10 WHERE fullname = 'Alice Jones'; -- 1
#### ERROR:  could not serialize access due to concurrent update

## Step 8

UPDATE account2 SET balance = balance + 20 WHERE fullname = 'Alice Jones'; -- 2

## Step 9

COMMIT; --1

## Step 10

ROLLBACK ; --2

## output 1 & 2
 username |     fullname     | balance | group_id
----------+------------------+---------+----------
 bitdiddl | Ben Bitdiddle    |      65 |        1
 mike     | Michael Dole     |      73 |        2
 alyssa   | Alyssa P. Hacker |      79 |        3
 bbrown   | Bob Brown        |     100 |        3
 jones   | Alice Jones      |      92 |        1

