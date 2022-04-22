# Transactions and Rollbacks 1.1

begin;
set transaction ISOLATION LEVEL SERIALIZABLE;
SAVEPOINT T1;
UPDATE account SET credit = credit-500 WHERE account_id = 1;
UPDATE account SET credit = credit+500 WHERE account_id = 3;
SAVEPOINT T2;
UPDATE account SET credit = credit-700 WHERE account_id = 2;
UPDATE account SET credit = credit+700 WHERE account_id = 1;
SAVEPOINT T3;
UPDATE account SET credit = credit-100 WHERE account_id = 2;
UPDATE account SET credit = credit+100 WHERE account_id = 3;
ROLLBACK TO T3;
ROLLBACK TO T2;
ROLLBACK TO T1;
commit;
end;

# Transactions and Rollbacks 1.2

begin;
set transaction ISOLATION LEVEL SERIALIZABLE;
SAVEPOINT T1;
UPDATE account SET credit = credit-500 WHERE account_id = 1;
UPDATE account SET credit = credit+500 WHERE account_id = 3;
SAVEPOINT T2;
UPDATE account SET credit = credit-730 WHERE account_id = 2;
UPDATE account SET credit = credit+30 WHERE account_id = 4;
UPDATE account SET credit = credit+70 WHERE account_id = 1;
SAVEPOINT T3;
UPDATE account SET credit = credit-130 WHERE account_id = 2;
UPDATE account SET credit = credit+30 WHERE account_id = 4;
UPDATE account SET credit = credit+100 WHERE account_id = 3;
ROLLBACK TO T3;
ROLLBACK TO T2;
ROLLBACK TO T1;
commit;
end;

# Transactions and Rollbacks 2.1

SAVEPOINT T1;
UPDATE account SET credit = credit-500 WHERE account_id = 1;
UPDATE account SET credit = credit+500 WHERE account_id = 3;
INSERT INTO ledger (ledger_id, from_id, to_id, amount) VALUES (0,1,3,500);
SAVEPOINT T2;
UPDATE account SET credit = credit-700 WHERE account_id = 2;
UPDATE account SET credit = credit+700 WHERE account_id = 1;
INSERT INTO ledger (ledger_id, from_id, to_id, amount) VALUES (1,2,1,700);
SAVEPOINT T3;
UPDATE account SET credit = credit-100 WHERE account_id = 2;
UPDATE account SET credit = credit+100 WHERE account_id = 3;
INSERT INTO ledger (ledger_id, from_id, to_id, amount) VALUES (2,2,3,100);
ROLLBACK TO T3;
ROLLBACK TO T2;
ROLLBACK TO T1;
commit;
end;

# Transactions and Rollbacks 2.2

begin;
set transaction ISOLATION LEVEL SERIALIZABLE;
SAVEPOINT T1;
UPDATE account SET credit = credit-500 WHERE account_id = 1;
UPDATE account SET credit = credit+500 WHERE account_id = 3;
INSERT INTO ledger (ledger_id, from_id, to_id, fee, amount) VALUES (0,1,3,0,500);
SAVEPOINT T2;
UPDATE account SET credit = credit-730 WHERE account_id = 2;
UPDATE account SET credit = credit+700 WHERE account_id = 1;
INSERT INTO ledger (ledger_id, from_id, to_id, fee, amount) VALUES (1,2,1,30,700);
SAVEPOINT T3;
UPDATE account SET credit = credit-130 WHERE account_id = 2;
UPDATE account SET credit = credit+100 WHERE account_id = 3;
INSERT INTO ledger (ledger_id, from_id, to_id, fee, amount) VALUES (2,2,3,30,100);
ROLLBACK TO T3;
ROLLBACK TO T2;
ROLLBACK TO T1;
commit;
end;
