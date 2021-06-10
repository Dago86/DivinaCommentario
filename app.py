from flask import Flask
from flask_restful import Api
from resources.user import User, UserRegister, UserLogin, TokenRefresh
from utils.cantigenerator import add_canti_to_db
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///divina.db' #nome del db 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'test'
api = Api(app)


#Temporanea, per controllare che il server si esegui correttamente
@app.route('/')
def home():
    return "Ok, ci siamo!"


@app.before_first_request
def create_tables():
    db.create_all()
    add_canti_to_db() #funzione da utilizzare solamente la prima volta che si esegue il server, serve a a popolare il db con i Canti


jwt = JWTManager(app)

'''
DONE USER:
POST: Register (username, password) - scrive l'istanza sul db
POST: Auth (username, password) - controlla l'esistenza dell'istanza sul db, restituisce token e refreshtoken utilizzo standard open JWT

TO-DO CANTO MODEL (id PK, nome, parte, testo)
TO-DO COMMENTO MODEL (id PK, id_canto FK, author, text)
'''



api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserLogin, '/login')
api.add_resource(TokenRefresh, '/refresh')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)