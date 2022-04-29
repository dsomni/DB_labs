###### CREATING Queries

Create(p:Fighter {name: 'Khabib Nurmagomedov',weight:'155'});
Create(p:Fighter {name: 'Rafael Dos Anjos',weight:'155'});

Create(p:Fighter {name: 'Neil Magny',weight:'170'});
Create(p:Fighter {name: 'Jon Jones',weight:'205'});
Create(p:Fighter {name: 'Daniel Cormier',weight:'205'});
Create(p:Fighter {name: 'Michael Bisping',weight:'185'});
Create(p:Fighter {name: 'Matt Hamill',weight:'185'});
Create(p:Fighter {name: 'Brandon Vera',weight:'205'});
Create(p:Fighter {name: 'Frank Mir',weight:'230'});
Create(p:Fighter {name: 'Brock Lesnar',weight:'230'});
Create(p:Fighter {name: 'Kelvin Gastelum',weight:'185'});

MATCH
(a:Fighter),
(b:Fighter)
WHERE
(a.name = 'Khabib Nurmagomedov' AND b.name = 'Rafael Dos Anjos') OR
(a.name = 'Rafael Dos Anjos' AND b.name = 'Neil Magny') OR
(a.name = 'Jon Jones' AND b.name = 'Daniel Cormier') OR
(a.name = 'Michael Bisping' AND b.name = 'Matt Hamill') OR
(a.name = 'Jon Jones' AND b.name = 'Brandon Vera') OR
(a.name = 'Brandon Vera' AND b.name = 'Frank Mir') OR
(a.name = 'Frank Mir' AND b.name = 'Brock Lesnar') OR
(a.name = 'Neil Magny' AND b.name = 'Kelvin Gastelum') OR
(a.name = 'Kelvin Gastelum' AND b.name = 'Michael Bisping') OR
(a.name = 'Michael Bisping' AND b.name = 'Matt Hamill') OR
(a.name = 'Michael Bisping' AND b.name = 'Kelvin Gastelum') OR
(a.name = 'Matt Hamill' AND b.name = 'Jon Jones')
CREATE (a)-[r:beats]->(b);

MATCH
(a:Fighter),
(b:Fighter)
WHERE
(a.name = 'Michael Bisping' AND b.name = 'Matt Hamill')
CREATE (a)-[r:beats]->(b);

#### (1) Return all middle/Walter/light weight fighters (155,170,185) who at least have one win

MATCH (n:Fighter)-[beats]-> (p:Fighter)
WHERE (n.weight = '155' OR n.weight = '170' OR n.weight = '185')
RETURN n

#### (2) Return fighters who had 1-1 record with each other. Use Count from the aggregation functions.

MATCH (a)-[r1:beats]->(b)
MATCH (b)-[r2:beats]->(a)
WITH a, b, COUNT(r1) AS t1, COUNT(r2) AS t2
WHERE t1 = t2 = 1
RETURN a,b
