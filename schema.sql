CREATE DATABASE bookstore;

USE bookstore;

CREATE TABLE Books (
  id INT PRIMARY KEY,
  title VARCHAR(255),
  author_id INT,
  price DECIMAL(10, 2),
  published_date DATE,
  FOREIGN KEY (author_id) REFERENCES Authors(id)
);

CREATE TABLE Authors (
  id INT PRIMARY KEY,
  name VARCHAR(255),
  bio TEXT
);

CREATE TABLE Customers (
  id INT PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255)
);

CREATE TABLE Orders (
  id INT PRIMARY KEY,
  customer_id INT,
  book_id INT,
  order_date DATE,
  FOREIGN KEY (customer_id) REFERENCES Customers(id),
  FOREIGN KEY (book_id) REFERENCES Books(id)
);
