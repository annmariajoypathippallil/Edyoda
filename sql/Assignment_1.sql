CREATE TABLE SalesPeople (
  Snum INT PRIMARY KEY,
  Sname VARCHAR(255) UNIQUE,
  City VARCHAR(255),
  Comm DECIMAL(5, 2)
);
insert into SalesPeople values(1001,"Peel","London",12);
insert into SalesPeople values(1002,"Serres","Sanjose",13);
insert into SalesPeople values(1004,"Motika","London",11);
insert into SalesPeople values(1007,"Rifkin","Barcelona",15);
insert into SalesPeople values(1003,"Axelrod","Newyork",10);


CREATE TABLE Customers (
  Cnum INT PRIMARY KEY,
  Cname VARCHAR(255),
  City VARCHAR(255) NOT NULL,
  Snum INT,
  FOREIGN KEY (Snum) REFERENCES SalesPeople(Snum)
);


insert into Customers values(2001,"Hoffman","London",1001);
insert into Customers values(2002,"Giovanni","Rome",1003);
insert into Customers values(2003,"Liu","Sanjose",1002);
insert into Customers values(2004,"Grass ","Berlin",1002);
insert into Customers values(2006,"Clemens","London",1001);
insert into Customers values(2008,"Cisneros","Sanjose",1007);
insert into Customers values(2007,"Pereira","Rome",1004);


CREATE TABLE Orders (
  Onum INT PRIMARY KEY,
  Amt DECIMAL(8, 2),
  Odate DATE,
  Cnum INT,
  Snum INT,
  FOREIGN KEY (Cnum) REFERENCES Customers(Cnum),
  FOREIGN KEY (Snum) REFERENCES SalesPeople(Snum)
);


INSERT INTO Orders VALUES (3001, 18.69, '1990-10-03', 2008, 1007);

INSERT INTO Orders VALUES (3003, 767.19, '1990-10-03', 2001, 1001);

INSERT INTO Orders VALUES (3002, 1900.10, '1990-10-03', 2007, 1004);

INSERT INTO Orders VALUES (3005, 5160.45, '1990-10-03', 2003, 1002);

INSERT INTO Orders VALUES (3006, 1098.16, '1990-10-03', 2008, 1007);

INSERT INTO Orders VALUES (3009, 1713.23, '1990-10-04', 2002, 1003);

INSERT INTO Orders VALUES (3007, 75.75, '1990-10-04', 2004, 1002);

INSERT INTO Orders VALUES (3008, 4273.00, '1990-10-05', 2006, 1001);

INSERT INTO Orders VALUES (3010, 1309.95, '1990-10-06', 2004, 1002);

INSERT INTO Orders VALUES (3011, 9891.88, '1990-10-06', 2006, 1001);



SELECT COUNT(*) AS CountOfSalespeople
FROM SalesPeople
WHERE UPPER(Sname) LIKE 'A%'

SELECT S.*
FROM SalesPeople S
INNER JOIN (
    SELECT Snum, SUM(Amt) AS TotalAmount
    FROM Orders
    GROUP BY Snum
    HAVING SUM(Amt) > 2000
) O ON S.Snum = O.Snum

SELECT COUNT(*) AS CountOfSalespeople
FROM SalesPeople
WHERE City = 'Newyork'


SELECT City, COUNT(*) AS CountOfSalespeople
FROM SalesPeople
WHERE City IN ('London', 'Paris')
GROUP BY City

SELECT S.Sname, O.Snum, COUNT(*) AS OrderCount, O.Odate
FROM SalesPeople S
INNER JOIN Orders O ON S.Snum = O.Snum
GROUP BY S.Sname, O.Snum, O.Odate


