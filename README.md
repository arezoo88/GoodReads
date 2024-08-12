GoodReads App Project

The goal of the project is to design and implement the APIs of a website where users can access the books they read, Record their points and comments (simplified version of GoodReads).

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [API Documentation](#api-documentation)
- [Postman Collection](#postman-collection)
- [Admin Panel SCREEN](#admin-panel-screen)



## Features

- Register and login
- Get list of books
- Get Details of books
- Comment and rate to each book
- Bookmark books

## Requirements

- Docker
- Docker Compose

## Installation

1. **Clone the repository:**

   ```sh
   git clone git@github.com:arezoo88/GoodReads.git
   cd source
   ```

2. **Create a `.env` file:**

   ```sh
   touch .env in source folder
   ```

   Add the content of .env-sample into your `.env` file in source folder:

3. **Build and start the Docker containers:**

   ```sh
   docker-compose up --build
   ```
4. **Load data for testing project:**

   ```sh
   docker-compose exec web bash -c "cd /home/app/source && python manage.py initdata && python manage.py loaddata apps/book/fixtures/books.json && python manage.py loaddata apps/book/fixtures/ratingcomments.json"
   ```
5. **Create superuser:**

   ```sh
   docker-compose exec web bash -c "cd /home/app/source && python manage.py createsuperuser"
   ```

## Running the Project

1. **Start the Docker containers:**

   ```sh
   docker-compose up -d
   ```

2. **Access the application:**

   - Swagger UI: `http://127.0.0.1:8000/swagger/`
   - Admin: `http://127.0.0.1:8000/admin/`

## API Documentation

Access the Swagger UI at `http://127.0.0.1:8000/swagger/` for interactive API documentation.

## Postman Collection

<a href="https://github.com/arezoo88/GoodReads/blob/master/source/assets/Goodreads App.postman_collection.json" download>Click to Download Postman Collection</a>

## Admin Panel SCREEN
![Admin Panel SCREEN](https://github.com/arezoo88/GoodReads/blob/master/source/assets/admin_panel_screen.png)
