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


if __name__ == '__main__':
    app.run(port=5000, debug=True)