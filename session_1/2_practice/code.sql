-- Enable readable output format
.mode columns
.headers on

-- Instructions for students:
-- 1. Open SQLite in terminal: sqlite3 library.db
-- 2. Load this script: .read code.sql
-- 3. Exit SQLite: .exit


-- write your sql code here

--1. **List all loans**  
--Show book title, member name, and loan date.
--select title, loan_date, name from Loans
--join Books on Books.id=Loans.id
--join Members on Loans.Member_id = Members.id;

--2. **Books and loans**  
--List all books and any loans associated with them.
--select title, loan_date 
--from Books join Loans On Books.id = Loans.book_id;

--3. **Branches and books**  
--List all library branches and the books they hold.
--select name, title
--from Books right join LibraryBranch on Books.branch_id = LibraryBranch.id;

--4. **Branch book counts**  
--Show each library branch and the number of books it holds.
--select LibraryBranch.name, COUNT(Books.id) AS total
--from LibraryBranch left join Books on Books.branch_id = LibraryBranch.id
--group by LibraryBranch.name

--5. **Branches with more than 7 books**  
--Show branches that hold more than 7 books.
select LibraryBranch.name, Books.id, COUNT(Books.id)
from LibraryBranch left join Books on Books.branch_id = LibraryBranch.id
group by LibraryBranch.name
having COUNT(Books.id) > 6;
