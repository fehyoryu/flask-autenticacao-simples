from flask import Flask, request, jsonify
# from database import db
from models.user import User
from database import db
from flask_login import LoginManager, login_user, current_user, logout_user, login_required

app = Flask(__name__)
# secret key: por ser teste, deixar algo simples
app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
login_manager = LoginManager()

db.init_app(app)
login_manager.init_app(app)
# view obrigatória para autenticar
login_manager.login_view = "login"

# vai ser possível recuperar o usuário logado em qualquer rota
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        # filtra no bd o usuario (unico) e retorna na variavel user
        user = User.query.filter_by(username = username).first()
        if user and user.password == password:
            login_user(user)
            print(current_user.is_authenticated)
            return jsonify({"message": "Autenticação realizada com sucesso"})
        else:
            return jsonify({"error": "Usuário não encontrado"}),404

    return jsonify({"message": "Credenciais inválidas"}), 400

@app.route("/logout", methods=["GET"])
# rota utilizada apenas enquanto tiver um usuário autenticado
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout realizado com sucesso"})

# criação de usuário
@app.route("/user", methods=["POST"])
@login_required
def create_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    if username and password:
        user = User(
            username = username,
            password = password
        )
        db.session.add(user)
        db.session.commit()

        return jsonify({"message": "Usuário cadastrado com sucesso"})
    return jsonify({"error": "Dados inválidos"}), 400

@app.route("/user/<int:id_user>", methods=["GET"])
@login_required
def get_usuario(id_user):
    user = User.query.get(id_user)
    if user:
        return jsonify({"username": user.username})
    return jsonify({"message": "Usuário não encontrado"}),404

@app.route("/user/<int:id_user>", methods=['PUT'])
@login_required
def update_user(id_user):
    user = User.query.get(id_user)
    data = request.json
    if user and data.get("password"):
        user.password = data.get("password")
        db.session.commit()
        return jsonify({"message": f"Usuário {user.id} atualizado com sucesso"})
    return jsonify({"message": "Usuário não encontrado"}),404

@app.route("/user/<int:id_user>", methods=["DELETE"])
@login_required
def delete_usuario(id_user):
    user = User.query.get(id_user)
    if id_user == current_user.id:
        return jsonify({"message": "Deleção do usuário logado não permitido"}),403
    
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": f"Usuário {id_user} deletado com sucesso"})
    
    return jsonify({"message": "Usuário não encontrado"}),404


@app.route("/hello-world", methods=["GET"])
def hello_world():
    return "Ola"


if __name__ == "__main__":
    app.run(debug=True)