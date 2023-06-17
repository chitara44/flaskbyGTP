import csv
from flask import Flask, jsonify, request

app = Flask(__name__)

# Endpoint GET para obtener la lista completa de sorteos
@app.route('/drafts', methods=['GET'])
def get_drafts():
    # Abrir el archivo CSV y leer los datos
    with open('expdata2.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        users = []
        for row in reader:
            users.append(row)
    # Devolver los datos como un objeto JSON
    return jsonify(users)


# Endpoint POST para crear un nuevo sorteo
@app.route('/drafts', methods=['POST'])
def create_draft():
    # Obtener los datos enviados por el cliente
    data = request.get_json()
    # Agregar el nuevo sorteo al archivo CSV
    with open('expdata2.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['idSorteo', 'fecha', 'tipo', 'ganador', 'nuevo', 'n1', 'n2', 'n3', 'n4', 'n5', 'sb'])
        writer.writerow(data)
    # Devolver los datos del nuevo sorteo como un objeto JSON
    return jsonify(data)


# Endpoint PUT para actualizar un sorteo existente
@app.route('/drafts/<int:idSorteo>', methods=['PUT'])
def update_draft(idSorteo):
    # Obtener los datos enviados por el cliente
    data = request.get_json()
    # Actualizar los datos del sorteo correspondiente en el archivo CSV
    with open('expdata2.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        sorteos = []
        for row in reader:
            if int(row['idSorteo']) == idSorteo:
                row.update(data)
            sorteos.append(row)
    with open('expdata2.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['idSorteo', 'fecha', 'tipo', 'ganador', 'nuevo', 'n1', 'n2', 'n3', 'n4', 'n5', 'sb'])
        writer.writeheader()
        writer.writerows(sorteos)
    # Devolver los datos actualizados del sorteo como un objeto JSON
    return jsonify(data)

# Endpoint DELETE para eliminar un usuario existente
@app.route('/drafts/<int:idSorteo>', methods=['DELETE'])
def delete_draft(idSorteo):
    # Eliminar el usuario correspondiente del archivo CSV
    with open('expdata2.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        users = []
        for row in reader:
            if int(row['idSorteo']) != idSorteo:
                users.append(row)
    with open('expdata2.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['idSorteo', 'fecha', 'tipo', 'ganador', 'nuevo', 'n1', 'n2', 'n3', 'n4', 'n5', 'sb'])
        writer.writeheader()
        writer.writerows(users)
    # Devolver un mensaje indicando que el usuario ha sido eliminado
    return 'El sorteo con ID {} ha sido eliminado'.format(idSorteo)

if __name__ == '__main__':
    app.run()