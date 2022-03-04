# My First API

This is a sample API created in Python using Flask to simulate a book API that allows you to **GET, POST, UPDATE** and **DELETE** items.

This application creates a database called 'books.db' using SQLite so that information can persist when the program closes.

## Database

#### A. Resetting the Database

**/api/books/db_populate**

This will re-initialize the database with 5 entries.

## B. Endpoints

#### 1\. Getting Current Listing of Books

**GET /api/books**

This will give you the current listing of all books that are in the database.

#### 2\. Posting New Books

**POST /api/books**

Use this to add a book and be sure to include the sample Json in the body. You may use the following format:

> {  
> "author": "Antoine de Saint-Exupery",  
> "book_id": "1",  
> "id": 1,  
> "name": "The Little Prince"  
> }

#### 3\. Getting a Specific Book by ID

**GET /api/books/**

By using the **GET** request that includes the "book_id" of the book, you can see that information.

#### 4\. Update a Book by ID

**PUT /api/books/**

By using a **PUT** request along with the "book_id" of the book **in the body text as json** you can update that particular book. Be sure to include the updated Json in the body of the request.

It is **not** necessary to include the "id" or the "book_id" in the URL as that will be automatically created from the Json of the body text.

#### 5\. Delete a Book by ID

**DELETE /api/books/**

You can delete a book by it's "id" by placing the number right after "/api/books/".