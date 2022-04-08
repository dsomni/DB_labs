# Before Indexing

### Query

EXPLAIN ANALYZE
SELECT name
FROM customer
WHERE name = 'Aaron Jones'

#### 1000.00..20407.87

### Query

EXPLAIN ANALYZE
SELECT review
FROM customer
WHERE length(review) > 20

#### 0.00..24756.97

### Query

EXPLAIN ANALYZE
SELECT id, name
FROM customer
WHERE id%2 = 0 OR id%7=0

#### 1000.00..22659.76

# After Indexing (hash on name and review; btree on id)

### Query

EXPLAIN ANALYZE
SELECT name
FROM customer
WHERE name = 'Aaron Jones'

#### 4.05..27.78

### Query

EXPLAIN ANALYZE
SELECT review
FROM customer
WHERE length(review) > 20

#### 0.00..24756.97

### Query

EXPLAIN ANALYZE
SELECT id, name
FROM customer
WHERE id%2 = 0 OR id%7=0

#### 1000.00..22647.76

## Conclusion

As we see. using indexes decreases the cost
