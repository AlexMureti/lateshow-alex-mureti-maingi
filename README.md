# Late Show API

## Project Description

A simple Flask REST API for managing Late Show episodes, guests, and their appearances.

This project is built as a **Phase 4 code challenge** and focuses on:

* Flask
* SQLAlchemy ORM
* Database relationships
* Seeding a database

---

## Project Structure

```
lateshow-alex-mureti-maingi/
├── server/
│   ├── app.py
│   ├── config.py
│   ├── models.py
│   ├── seed.py
│   ├── __init__.py
│   └── app.db
├── Pipfile
├── Pipfile.lock
└── README.md
```

---

## Models

### Episode

* id
* date
* number
* has many appearances

### Guest

* id
* name
* number
* has many appearances

### Appearance

* id
* rating (1–5)
* episode_id (FK)
* guest_id (FK)

---

## Relationships

* An Episode has many Guests through Appearances
* A Guest has many Episodes through Appearances
* An Appearance belongs to one Episode and one Guest

---

## Setup Instructions

1. Clone the repository
2. Install dependencies

```bash
pipenv install
pipenv shell
```

3. Run database seed

```bash
python -m server.seed
```

---

## Running the Application

```bash
python server/app.py
```

---

## Technologies Used

* Python
* Flask
* Flask-SQLAlchemy
* SQLite

---

## Author

**Alex Mureti Maingi**

### Collaborator

Peter Muturi
