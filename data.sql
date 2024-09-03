INSERT INTO Authors (id, name, bio) VALUES
  (1, 'John Doe', 'John Doe is a renowned author known for his thriller novels.'),
  (2, 'Jane Smith', 'Jane Smith is a bestselling author of romance novels.'),
  (3, 'Bob Johnson', 'Bob Johnson is a popular author of science fiction novels.'),
  (4, 'Agatha Christie', 'Agatha Christie is the Queen of Crime fiction, famous for her detective novels.'),
  (5, 'Stephen King', 'Stephen King is a master of horror fiction, known for his chilling stories.'),
  (6, 'J.K. Rowling', 'J.K. Rowling is the creator of the beloved Harry Potter fantasy series.'),
  (7, 'Harper Lee', 'Harper Lee wrote the Pulitzer Prize-winning novel To Kill a Mockingbird.'),
  (8, 'Margaret Atwood', 'Margaret Atwood is a renowned author of dystopian fiction and feminist literature.'),
  (9, 'George R.R. Martin', 'George R.R. Martin is the author of the epic fantasy series A Song of Ice and Fire.'),
  (10, 'Paulo Coelho', 'Paulo Coelho is a bestselling author known for his inspirational novels.');

INSERT INTO Books (id, title, author_id, price, published_date) VALUES
  (1, 'The Lost City', 1, 19.99, '2018-01-01'),
  (2, 'The Romance Novel', 2, 14.99, '2019-02-01'),
  (3, 'The Space Odyssey', 3, 24.99, '2020-03-01'),
  (4, 'The Thriller', 1, 19.99, '2019-04-01'),
  (5, 'The Love Story', 2, 14.99, '2020-05-01'),
  (6, 'Murder on the Orient Express', 4, 18.99, '1934-01-01'),
  (7, 'The Shining', 5, 22.99, '1977-01-01'),
  (8, 'Harry Potter and the Sorcerer's Stone', 6, 16.99, '1997-06-26'),
  (9, 'To Kill a Mockingbird', 7, 19.99, '1960-07-11'),
  (10, 'The Handmaid's Tale', 8, 17.99, '1985-04-26'),
  (11, 'A Game of Thrones', 9, 24.99, '1996-08-01'),
  (12, 'The Alchemist', 10, 15.99, '1988-01-01'),
  (13, 'The Da Vinci Code', 4, 19.99, '2003-03-18'),
  (14, 'Pride and Prejudice', 7, 18.99, '1813-01-28'),
  (15, 'The Lord of the Rings: The Fellowship of the Ring', 6, 29.99, '1954-07-29');

INSERT INTO Customers (id, name, email) VALUES
  (1, 'Alice Brown', 'alice.brown@example.com'),
  (2, 'Bob Davis', 'bob.davis@example.com'),
  (3, 'Charlie Evans', 'charlie.evans@example.com'),
  (4, 'Diana Garcia', 'diana.garcia@example.com'),
  (5, 'Ethan Hernandez', 'ethan.hernandez@example.com'),
  (6, 'Isabella Jackson', 'isabella.jackson@example.com'),
  (7, 'Jacob Kim', 'jacob.kim@example.com'),
  (8, 'Lily Martinez', 'lily.martinez@example.com'),
  (9, 'Noah Miller', 'noah.miller@example.com');

INSERT INTO Orders (id, customer_id, book_id, order_date) VALUES
  (1, 1, 1, '2020-06-01'),
  (2, 1, 2, '2020-07-01'),
  (3, 2, 3, '2020-08-01'),
  (4, 3, 4, '2020-09-01'),
  (5, 1, 5, '2020-10-01'),
  (6, 2, 6, '2020-11-01'),
  (7, 3, 7, '2020-12-01'),
  (8, 4, 8, '2021-01-01'),
  (9, 5, 9, '2021-02-01'),
  (10, 6, 10, '2021-03-01'),
  (11, 7, 11, '2021-04-01'),
  (12, 8, 12, '2021-05-01'),
  (13, 9, 13, '2021-06-01'),
  (14, 1, 14, '2021-07-01'),
  (15, 2, 15, '2021-08-01');
