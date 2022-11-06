from fastapi import FastAPI, status
from database import Base, engine
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///library.db")

Base = declarative_base()

Base.metadata.create_all(engine)

app = FastAPI()

@app.get("/", tags=["Books"])
def root():
    return "book"

@app.post("/book", status_code=status.HTTP_201_CREATED, tags=["Books"])
def create_book():
    
    session = Session(bind=engine, expire_on_commit=False)

    tododb = ToDo(task = todo.task)

    session.add(tododb)
    session.commit()

    id = tododb.id

    session.close()

    return f"create {id}"

@app.get("/book/{id}", tags=["Books"])
def read_book(id: int):

    session = Session(bind=engine, expire_on_commit=False)

    todo = session.query(ToDo).get(id)

    session.close()
    return f"read item with id {id}"

@app.put("/book/{id}", tags=["Books"])
def update_book(id: int):
    return "update item with id {id}"

@app.delete("/book/{id}", tags=["Books"])
def delete_book(id: int):
    return "delete item with id {id}"

@app.get("/book", tags=["Books"])
def read_book_list():
    return "read list"

@app.post("/reader", status_code=status.HTTP_201_CREATED, tags=["Reader"])
def create_reader():
    return "create"

@app.get("/reader/{id}", tags=["Reader"])
def read_reader(id: int):
    return "read item with id {id}"

@app.put("/reader/{id}", tags=["Reader"])
def update_reader(id: int):
    return "update item with id {id}"

@app.delete("/reader/{id}", tags=["Reader"])
def delete_reader(id: int):
    return "delete item with id {id}"

@app.post("/author", status_code=status.HTTP_201_CREATED, tags=["Author"])
def create_author():
    return "create"

@app.get("/author/{id}", tags=["Author"])
def read_author(id: int):
    return "read item with id {id}"

@app.put("/author/{id}", tags=["Author"])
def update_author(id: int):
    return "update item with id {id}"

@app.delete("/author/{id}", tags=["Author"])
def delete_author(id: int):
    return "delete item with id {id}"