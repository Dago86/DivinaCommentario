from flask import Flask
from flask_restful import Api



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


'''
TO-DO USER:
POST: Register (username, password) - scrive l'istanza sul db
POST: Auth (username, password) - controlla l'esistenza dell'istanza sul db, restituisce token e refreshtoken utilizzo standard open JWT
'''


if __name__ == '__main__':
    app.run(port=5000, debug=True)