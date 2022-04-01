## Find the distinct names of all students who score more than 90% in the course numbered 107

#### SQL

SELECT DISTINCT(S.sname)
FROM Students as S, Courses as C, Registration as R
WHERE R.sid = S.sid AND R.cid = 107 AND R.percent > 90

#### RA

π<sub>s.sname</sub>(σ<sub>r.sid = s.sid AND r.cid = 107 AND r.percent > 90</sub>(ρ<sub>s</sub>Students × ρ<sub>c</sub>Courses × ρ<sub>R</sub>Registration))

## Find the number of student whose score is 75% or above in each course.

#### SQL

SELECT DISTINCT(S.sid)
FROM Students as S
WHERE NOT EXISTS (
SELECT R.cid
FROM Registration as R
WHERE R.sid = S.sid AND R.percent < 75
)

#### RA

π<sub>s.sid</sub>(σ<sub>π<sub>r.cid</sub>(σ<sub>r.cid = s.sid and r.percent <75</sub>(ρ<sub>r</sub>Registration))= null</sub>(ρ<sub>s</sub>Students))

## Find those students who are registered on no more than 2 courses

#### SQL

SELECT R.sid
FROM Registration as R
GROUP BY R.sid
HAVING COUNT(DISTINCT R.cid) <= 2

#### RA

π<sub>r.sid</sub>(σ<sub>COUNT(cid)<=2</sub>(γ<sub>sid</sub>(ρ<sub>r</sub>Registration)))
