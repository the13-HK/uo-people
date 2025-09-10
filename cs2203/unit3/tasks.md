Question:
A bookstore is interested in storing information about authors and their books in a database. For this purpose, the following relations are created:

Authors (AuthorID, AuthorName) [AuthorID is the primary key]

Books (BookID, Title, Genre, AuthorID) [BookID is the primary key, AuthorID is a foreign key referencing the Authors table]

Given the above scenario, engage yourself in a discussion by answering the questions below.

Discuss why this schema might encounter difficulties when dealing with books that have multiple authors. Your discussion should focus on primary key and functional dependency concepts.

Analyse the functional dependencies present in the schema and explain how they impact the representation of books authored by multiple individuals.

Also, propose potential modifications to the schema to address these limitations.
End your discussion post with one question related to the concepts learned in this unit from which your colleagues can formulate a response or generate further discussion.


### Answers:
1. **Difficulties with Multiple Authors**:
   The current schema presents challenges when dealing with books that have multiple authors because the `Books` table uses a single `AuthorID` as a foreign key referencing the `Authors` table. This design implies a one-to-one relationship between books and authors, which does not accommodate the many-to-many relationship that can exist when a book is co-authored by multiple individuals. In such cases, it becomes difficult to represent all authors of a book without violating the primary key constraint, as each book can only reference one author. 
   This limitation arises from the functional dependency where `BookID` determines `AuthorID`, which does not hold true for books with multiple authors. If a book has two or more authors, it cannot be accurately represented in the current schema without duplicating book entries or creating ambiguity in author attribution.

2. **Functional Dependencies**:
  The functional dependencies in the schema can be summarized as follows:
     - `AuthorID` → `AuthorName`
     - `BookID` → `Title`, `Genre`, `AuthorID`
  These functional dependencies indicate that each author is uniquely identified by their `AuthorID`, and each book is uniquely identified by its `BookID`. However, the current schema does not account for the possibility of multiple authors for a single book, which complicates the representation of books authored by multiple individuals. In a many-to-many relationship, we would need a way to associate multiple authors with a single book without violating the functional dependencies.

3. **Proposed Modifications to the Schema**:
  To address the limitations of the current schema, we can introduce a junction table (also known as a join table or associative entity) to represent the many-to-many relationship between authors and books. The modified schema would look like this:

```
Authors (AuthorID, AuthorName) [AuthorID is the primary key]
Books (BookID, Title, Genre) [BookID is the primary key]
AuthorsBooks (AuthorID, BookID) [Composite primary key: AuthorID, BookID]
```

  In this modified schema:
     - The `AuthorsBooks` table serves as a junction table that links authors and books, allowing for multiple authors to be associated with a single book and vice versa.
     - The composite primary key of `AuthorsBooks` ensures that each combination of `AuthorID` and `BookID` is unique, thus allowing for accurate representation of books with multiple authors.
     - This design maintains the functional dependencies while accommodating the many-to-many relationship, enabling better data integrity and flexibility in representing authorship.
4. **Discussion Question**:
  I don't think that overdoing normalization is necessarily a good thing. I think the balance of normalization varies from person to person, but what is your standard for thinking about the balance of normalization?




Program Assignment:
Given the following unnormalized relation representing a library database:

Books (Book_ID, Title, Author, Genre, Publisher, Publication_Year, ISBN, Price)

a) Define normalization in the context of database management systems (DBMS). Explain why normalization is essential for database design.

b) Normalize this relation into First Normal Form (1NF), Second Normal Form (2NF), Third Normal Form (3NF) and Boyce-Codd Normal Form (BCNF).

c) For each normalization step (1NF, 2NF, 3NF, BCNF) performed in Part (b), explain the specific functional dependencies present in the original relation and how they are addressed through normalization.

d) Discuss the advantages and potential drawbacks of achieving higher normal forms (3NF and BCNF) compared to lower normal forms (1NF and 2NF) in terms of database design, querying efficiency, and data integrity.

### Answers:
1. **Normalization in DBMS**:
   Normalization is the process of organizing data in a database to reduce redundancy and improve data integrity. It involves decomposing a relation into smaller, related relations while preserving the original data's semantics. Normalization is essential for database design because it helps eliminate anomalies such as insertion, deletion, and update anomalies, ensuring that the database remains consistent and efficient for querying.
2. **Normalization Steps**:
   a) **First Normal Form (1NF)**:
      To achieve 1NF, we need to ensure that all attributes contain atomic values and that each record is unique. In the original relation, the `Author` attribute may contain multiple authors for a single book, violating 1NF. We can create separate records for each author-book combination, resulting in the following 1NF relation:
```
Books (Book_ID, Title, Author, Genre, Publisher, Publication_Year, ISBN, Price)
```
   b) **Second Normal Form (2NF)**:
      To achieve 2NF, we need to eliminate partial dependencies, where non-key attributes depend on only part of a composite primary key. In this case, `Author`, `Genre`, `Publisher`, `Publication_Year`, `ISBN`, and `Price` depend on `Book_ID` but not on the entire primary key. We can separate the relation into two relations:
```
Books (Book_ID, Title, Genre, Publisher, Publication_Year, ISBN, Price)
Authors (Book_ID, Author_ID, Author_Name)

```
   c) **Third Normal Form (3NF)**:
      To achieve 3NF, we need to eliminate transitive dependencies, where non-key attributes depend on other non-key attributes. In this case, `Publisher` and `Publication_Year` depend on `ISBN`, which is not a primary key. We can further separate the relation:
```
Books (Book_ID, Title, Genre, ISBN, Price)
Publishers (Publisher_ID, Publisher_Name, Publication_Year)
Authors (Book_ID, Author_ID, Author_Name)
```
   d) **Boyce-Codd Normal Form (BCNF)**:
      To achieve BCNF, we need to isolate Book_ID of the `Authors` relation as a primary key, ensuring that every determinant is a candidate key. The final relations in BCNF would be:
```
Books (Book_ID, Title, Genre, ISBN, Price)
Publishers (Publisher_ID, Publisher_Name, Publication_Year)
Authors (Author_ID, Author_Name)
AuthorsBooks (Author_ID, Book_ID)

```
3. **Functional Dependencies**:
   - In the original relation, the functional dependencies are:
     - `Book_ID` → `Title`, `Author`, `Genre`, `Publisher`, `Publication_Year`, `ISBN`, `Price`
     - `ISBN` → `Publisher`, `Publication_Year`
   - In 1NF, we address the atomicity of values.
   - In 2NF, we eliminate partial dependencies by separating authors and books.
   - In 3NF, we eliminate transitive dependencies by separating publishers.
   - In BCNF, we ensure that every determinant is a candidate key.
4. **Advantages and Drawbacks of Higher Normal Forms**:
   - **Advantages**:
     - Improved data integrity: Higher normal forms reduce redundancy and the potential for anomalies.
     - Easier maintenance: Changes to data structures are less likely to introduce inconsistencies.
     - Better query performance: Well-structured databases can lead to more efficient queries.
   - **Drawbacks**:
     - Complexity: Higher normal forms can lead to more complex schemas, making them harder to understand.
     - Performance trade-offs: In some cases, normalization can lead to more joins in queries, potentially impacting performance.
     - Loss of denormalization benefits: In certain scenarios, denormalization may be preferred for performance reasons, especially in read-heavy applications.
     - In conclusion, while higher normal forms provide significant advantages in terms of data integrity and maintenance, they also introduce complexity and potential performance trade-offs that must be carefully considered in the context of the specific application and its requirements.