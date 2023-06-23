import string

from fastapi import FastAPI, status
from database import Base, engine, ToDo
from pydantic import BaseModel
from sqlalchemy.orm import Session
from filemanager import Files
from db_connection import DB_connection
from dfs_data_class import dfs_data_class as dfs

# Create ToDoRequest Base Model
class ToDoRequest(BaseModel):
    task: str

# Create the database
Base.metadata.create_all(engine)

# Initialize app
app = FastAPI()

arrayfiles = Files()

db_con = DB_connection()
#df = arrayfiles.initial_load()

@app.get("/")
def root():
    return "todooo"

@app.post("/todo", status_code=status.HTTP_201_CREATED)
def create_todo(todo: ToDoRequest):

    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # create an instance of the ToDo database model
    tododb = ToDo(task = todo.task)

    # add it to the session and commit it
    session.add(tododb)
    session.commit()

    # grab the id given to the object from the database
    id = tododb.id

    # close the session
    session.close()

    # return the id
    return f"created todo item with id {id}"


@app.get("/todo/{id}")
def read_todo(id: int):

    return "read todo item with id: " + str(id)

@app.get("/todo/{id}")
def read_todo(id: int):
    idStr = str(id)

    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # get the todo item with the given id
    todo = session.query(ToDo).get(id)

    # close the session
    session.close()

    return f"todo item with id: {todo.id} and task: {todo.task} then parameter is {idStr} "


@app.put("/todo/{id}")
def update_todo(id: int):
    idStr = str(id)
    return "update todo item with id: " + idStr

@app.delete("/todo/{id}")
def delete_todo(id: int):
    idStr = str(id)
    return "delete todo item with id" + idStr

@app.get("/todo")
def read_todo_list():
    df, dfs, dfc = entireflow()
    response = str(dfc)
    return str(response)


@app.get("/conteo/{type}/{size}", status_code=status.HTTP_200_OK)
def read_todo_list(type: str, size: int):
    dfr = conteos(type, size)
    response = str(dfr)
    return str(response)

@app.get("/find/{type}/{num}", status_code=status.HTTP_200_OK)
def read_todo_list(type: str, num: int):
    df = arrayfiles.initial_load()
    newdf = df[(df.idSorteo == num) & (df.tipo == type)]
    #newdf = df.query('sorteo == num) & (df.tipo == type')
    response = str(newdf)
    return str(response)

def entireflow():
    df = arrayfiles.initial_load()
    dfs = arrayfiles.files_loader()
    dfc = arrayfiles.counting_readers()
    return df, dfs, dfc

def conteos(type, size):
    dfc = arrayfiles.counting_readers()
    dfr = []
    if (type =='tr' ):
        dfr = retrieve_df_tr(dfc, size)
        return dfr
    elif(type == 're'):
        dfr=retrieve_df_re(dfc, size)
        return dfr
    else:
        return dfr
    return dfc

def alldataframes():
    dfs = arrayfiles.files_loader()
    return dfs

def retrieve_df_tr(dfc, num):
    if (num == 1):
        return dfc.conteos_1d_tr
    elif (num == 2):
        return dfc.conteos_2d_tr
    elif (num == 3):
        return dfc.conteos_3d_tr
    elif (num == 4):
        return dfc.conteos_4d_tr
    else:
        return dfc.conteos_5d_tr

def retrieve_df_re(dfc, num):
    if (num == 1):
        return dfc.conteos_1d_re
    elif (num == 2):
        return dfc.conteos_2d_re
    elif (num == 3):
        return dfc.conteos_3d_re
    elif (num == 4):
        return dfc.conteos_4d_re
    else:
        return dfc.conteos_5d_re



#def connect_db(pwd):
