import csv

from database import Base, engine, ToDo
from pydantic import BaseModel
from sqlalchemy.orm import Session
from filemanager import Files
from db_connection import DB_connection
from dfs_data_class import dfs_data_class as dfs
from flask import Flask, jsonify, request


class ToDoRequest(BaseModel):
    task: str

# Create the database
Base.metadata.create_all(engine)

app = Flask(__name__)

arrayfiles = Files()

db_con = DB_connection()

# Endpoint GET to get all the drafts results
@app.route('/drafts', methods=['GET'])
def get_drafts():
    # Reads a CSV file to get all the information within
    with open('expdata.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        users = []
        for row in reader:
            users.append(row)
    # retrieves a draft data as a JSON object
    return jsonify(users)

@app.route('/drafts/{id}', methods=['GET'])
def read_todo(id: int):
    idStr = str(id)
    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)
    # get the todo item with the given id
    todo = session.query(ToDo).get(id)
    # close the session
    session.close()
    return f"todo item with id: {todo.id} and task: {todo.task} then parameter is {idStr} "


# Endpoint POST to create a newdraft
@app.route('/drafts', methods=['POST'])
def create_draft():
    # get the customers data
    data = request.get_json()
    # Add a new draft to CSV file
    with open('expdata.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['idSorteo', 'fecha', 'tipo', 'ganador', 'nuevo', 'n1', 'n2', 'n3', 'n4', 'n5', 'sb'])
        writer.writerow(data)
    # retrieves new draft data as a JSON object
    return jsonify(data)


# Endpoint to update an existing draft through a PUT operation
@app.route('/drafts/<int:idSorteo>', methods=['PUT'])
def update_draft(idSorteo):
    # get the customers data
    data = request.get_json()
    # Update a draft to CSV file
    with open('expdata.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        sorteos = []
        for row in reader:
            if int(row['idSorteo']) == idSorteo:
                row.update(data)
            sorteos.append(row)
    with open('expdata.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['idSorteo', 'fecha', 'tipo', 'ganador', 'nuevo', 'n1', 'n2', 'n3', 'n4', 'n5', 'sb'])
        writer.writeheader()
        writer.writerows(sorteos)
    # retrieves an updated draft data as a JSON object
    return jsonify(data)

# Endpoint DELETE for deleting an existing draft
@app.route('/drafts/<int:idSorteo>', methods=['DELETE'])
def delete_draft(idSorteo):
    # Deletes a draft from CSV file
    with open('expdata.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        users = []
        for row in reader:
            if int(row['idSorteo']) != idSorteo:
                users.append(row)
    with open('expdata.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['idSorteo', 'fecha', 'tipo', 'ganador', 'nuevo', 'n1', 'n2', 'n3', 'n4', 'n5', 'sb'])
        writer.writeheader()
        writer.writerows(users)
    # retrieves a message indicating that a draft has been deleted
    return 'El sorteo con ID {} ha sido eliminado'.format(idSorteo)

if __name__ == '__main__':
    app.run()