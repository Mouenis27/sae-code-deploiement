from flask import Flask, jsonify, request

# Créer l'application Flask (web)
app = Flask(__name__)

# Sauvegarder les étudiants dans une liste
students = [
    {"id": 1, "prenom": "Samir", "age": 31},
    {"id": 2, "prenom": "Safa", "age": 22},
]

# Définir la racine de l'API
@app.route("/")
def home():
    return """
    <html>
    <head>
        <style>
            body {
                background: #0d0d0d;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                margin: 0;
                font-family: Arial, sans-serif;
            }

            .neon-box {
                width: 300px;
                height: 300px;
                border: 4px solid #00f5ff;
                box-shadow: 0 0 20px #00f5ff, inset 0 0 20px #00f5ff;
                animation: pulse 2s infinite alternate;
                display: flex;
                justify-content: center;
                align-items: center;
                font-size: 28px;
                color: #00f5ff;
                text-shadow: 0 0 10px #00f5ff;
                border-radius: 10px;
            }

            @keyframes pulse {
                from { box-shadow: 0 0 10px #00f5ff; }
                to { box-shadow: 0 0 40px #00f5ff; }
            }
        </style>
    </head>

    <body>
        <div class="neon-box">Hamon Hamon Hamon</div>
    </body>
    </html>
    """


# --------- CRUD ÉTUDIANTS ---------

# GET /students : récupérer tous les étudiants
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)


# POST /students : ajouter un étudiant
@app.route("/students", methods=["POST"])
def add_student():
    if not request.is_json:
        return jsonify({"erreur": "Le corps de la requête doit être en JSON"}), 400

    new_student = request.get_json()

    # Vérif simple (optionnelle)
    if "prenom" not in new_student or "age" not in new_student:
        return jsonify({"erreur": "Champs 'prenom' et 'age' obligatoires"}), 400

    # Assigner un ID automatique (simple, pour l'exercice)
    new_student["id"] = len(students) + 1
    students.append(new_student)
    return jsonify(new_student), 201


# GET /students/<id> : récupérer un étudiant par id
@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    student = next((s for s in students if s["id"] == id), None)

    if student:
        return jsonify(student)

    return jsonify({"erreur": "L'étudiant n'a pas été trouvé"}), 404


# PUT /students/<id> : mettre à jour un étudiant
@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    student = next((s for s in students if s["id"] == id), None)
    if not student:
        return jsonify({"erreur": "L'étudiant n'existe pas"}), 404

    if not request.is_json:
        return jsonify({"erreur": "Le corps de la requête doit être en JSON"}), 400

    data = request.get_json()

    # On évite de modifier l'id par erreur
    data.pop("id", None)

    student.update(data)
    return jsonify(student)


# DELETE /students/<id> : supprimer un étudiant
@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    global students
    student = next((s for s in students if s["id"] == id), None)

    if not student:
        return jsonify({"erreur": "L'étudiant n'existe pas"}), 404

    students = [s for s in students if s["id"] != id]
    return jsonify({"message": "Étudiant supprimé avec succès"}), 200


# Lancer l'application
if __name__ == "__main__":
    app.run(host='0.0.0.0' , port=80 ,debug=True)
