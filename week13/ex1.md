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

#### (3) Return all fighter that can “Khabib Nurmagomedov” beat them and he didn’t have a fight with them yet

MATCH (a:Fighter {name:'Khabib Nurmagomedov'})-[r1:beats*2..]->(b)
RETURN b

#### (4) Return undefeated Fighters(0 loss)

MATCH (a:Fighter)
WHERE NOT ()-[:beats]->(a)
RETURN a

#### (5) Return defeated fighter (0 wins)

MATCH (a:Fighter)
WHERE NOT (a)-[:beats]->()
RETURN a

#### (6) Return all fighters MMA records and create query to enter the record as a property for a fighter {name, weight, record}

MATCH (a:Fighter)
CALL {
WITH a
MATCH (a)-[r:beats]->(c:Fighter)
RETURN count(r) AS wins
}
CALL {
WITH a
MATCH (c:Fighter)-[r:beats]->(a)
RETURN count(r) AS looses
}
SET a.record = toString(wins)+'-'+toString(looses)
return a.name, a.record

#### OUTPUT ex1.6[

{
"a.name": "Jon Jones",
"a.record": "2-1"
},
{
"a.name": "Khabib Nurmagomedov",
"a.record": "1-0"
},
{
"a.name": "Daniel Cormier",
"a.record": "0-1"
},
{
"a.name": "Rafael Dos Anjos",
"a.record": "1-1"
},
{
"a.name": "Michael Bisping",
"a.record": "3-1"
},
{
"a.name": "Neil Magny",
"a.record": "1-1"
},
{
"a.name": "Matt Hamill",
"a.record": "1-2"
},
{
"a.name": "Brandon Vera",
"a.record": "1-1"
},
{
"a.name": "Frank Mir",
"a.record": "1-1"
},
{
"a.name": "Brock Lesnar",
"a.record": "0-1"
},
{
"a.name": "Kelvin Gastelum",
"a.record": "1-2"
}
]
