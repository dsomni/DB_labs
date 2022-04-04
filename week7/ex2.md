## Creation SQL

CREATE TABLE "Ex2"."Schools"(
schoolId INTEGER PRIMARY KEY,
schoolName TEXT
);

CREATE TABLE "Ex2"."Publishers"(
publisherId INTEGER PRIMARY KEY,
publisherName TEXT
);

CREATE TABLE "Ex2"."Teachers"(
teacherId INTEGER PRIMARY KEY,
teacherName TEXT
);

CREATE TABLE "Ex2"."Rooms"(
roomId INTEGER PRIMARY KEY,
roomTitle TEXT
);

CREATE TABLE "Ex2"."Grades"(
gradeId INTEGER PRIMARY KEY,
gradeTitle TEXT
);

CREATE TABLE "Ex2"."Books"(
bookId INTEGER PRIMARY KEY,
bookTitle TEXT,
publisherId INTEGER,
FOREIGN KEY (publisherId) REFERENCES "Ex2"."Publishers"(publisherId)
);

CREATE TABLE "Ex2"."Courses"(
courseId INTEGER PRIMARY KEY,
courseTitle TEXT
);

CREATE TABLE "Ex2"."Loanings"(
schoolId INTEGER,
teacherId INTEGER,
courseId INTEGER,
roomId INTEGER,
gradeId INTEGER,
bookId INTEGER,
loanDate DATE,
PRIMARY KEY (schoolId, teacherId, courseId, roomId, gradeId, bookId),
FOREIGN KEY (schoolId) REFERENCES "Ex2"."Schools"(schoolId),
FOREIGN KEY (teacherId) REFERENCES "Ex2"."Teachers"(teacherId),
FOREIGN KEY (courseId) REFERENCES "Ex2"."Courses"(courseId),
FOREIGN KEY (roomId) REFERENCES "Ex2"."Rooms"(roomId),
FOREIGN KEY (gradeId) REFERENCES "Ex2"."Grades"(gradeId),
FOREIGN KEY (bookId) REFERENCES "Ex2"."Books"(bookId)
);

## Insertion SQL

INSERT INTO "Ex2"."Schools"(
schoolId, schoolName)
VALUES
(0, 'Horizon Education Institute'),
(1, 'Bright Institution');

INSERT INTO "Ex2"."Publishers"(
publisherId, publisherName)
VALUES
(0, 'BOA Editions'),
(1, 'Taylor & Francis Publishing'),
(2, 'Prentice Hall'),
(3, 'McGraw Hill');

INSERT INTO "Ex2"."Teachers"(
teacherId, teacherName)
VALUES
(0, 'Chad Russel'),
(1, 'E.F.Codd'),
(2, 'Jones Smith'),
(3, 'Adam Baker');

INSERT INTO "Ex2"."Courses"(
courseId, courseTitle)
VALUES
(0, 'Logical thinking'),
(1, 'Wrtting'),
(2, 'Numerical Thinking'),
(3, 'Spatial, Temporal and Causal Thinking'),
(4, 'English');

INSERT INTO "Ex2"."Rooms"(
roomId, roomTitle)
VALUES
(0, '1.A01'),
(1, '1.B01');

INSERT INTO "Ex2"."Grades"(
gradeId, gradeTitle)
VALUES
(1, '1st grade'),
(2, '2nd grade');

INSERT INTO "Ex2"."Books"(
bookId, bookTitle, publisherId)
VALUES
(0, 'Learning and teaching in early childhood', 0),
(1, 'Preschool,N56', 1),
(2, 'Early Childhood Education N9', 2),
(3, 'Know how to educate: guide for Parents and',3);

INSERT INTO "Ex2"."Loanings"(
schoolId, teacherId, courseId, roomId, gradeId, bookId, loanDate)
VALUES
(0, 0,0,0, 1,0,'2010-09-09'),
(0, 0,1,0, 1,1,'2010-05-05'),
(0, 0,2,0, 1,0,'2010-05-05'),

(0, 1,3,1, 1,2,'2010-05-06'),
(0, 1,2,1, 1,0,'2010-05-06'),

(0, 2,1,0, 2,0,'2010-09-09'),
(0, 2,4,0, 2,3,'2010-05-05'),

(1, 3,0,1, 1,3,'2010-12-18'),
(1, 3,2,1, 1,0,'2010-05-06');

## Queries

### Obtain for each of the schools, the number of books that have been loaned to each publishers

#### query

SELECT S.schoolName, P.publisherName, COUNT(L.bookId) as NumberOfBooks
FROM "Ex2"."Loanings" as L
JOIN "Ex2"."Books" as B ON L.bookId = B.bookId
JOIN "Ex2"."Publishers" as P ON B.publisherId = P.publisherId,
"Ex2"."Schools" as S
WHERE S.schoolId = L.schoolId
GROUP BY S.schoolName, P.publisherName;

#### output

check ex2.output1.jpg

### For each school, find the book that has been on loan the longest and the teacher in charge of it

#### query

SELECT S.schoolName, B.bookTitle, T.teacherName
FROM (
SELECT L.schoolId, MIN(L.loanDate) as minDate
FROM "Ex2"."Loanings" as L
GROUP BY L.schoolId
) as minDateInfo, "Ex2"."Schools" as S, "Ex2"."Teachers" as T,
"Ex2"."Loanings" as L,
"Ex2"."Books" as B
WHERE S.schoolId = minDateInfo.schoolId AND
L.bookId = B.bookId AND L.loanDate = minDateInfo.minDate
AND L.teacherId = T.teacherId AND L.schoolId = minDateInfo.schoolId

#### output

check ex2.output2.jpg
