import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt_extended import(

 create_access_token, 
 create_refresh_token, 
 jwt_required, 
 get_jwt_identity
)
from werkzeug.security import safe_str_cmp 

from models.user import UserModel

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('username',
    type= str,
    required=True,
    help= "Campo obbligatorio, username")

_user_parser.add_argument('password',
    type= str,
    required=True,
    help= "Campo obbligatorio, password")

"""La registrazione utilizza il parser per controllare la presenza di username e password"""
class UserRegister(Resource):
    def post(self):
        data = _user_parser.parse_args() 

        if UserModel.find_by_username(data['username']):
            return {"message": "L'utente esiste già"}, 400

        user = UserModel(data['username'], data['password'])
        user.save_to_db()

        return {"message": "User creato e salvato su db."}, 201

class User(Resource):
    @classmethod
    def get(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message':'Utente non trovato.'}
        return user.json()

    @classmethod
    def delete(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message':'Utente non trovato.'}
        user.delete_from_db()
        return {'message': 'Utente cancellato.'}


class UserLogin(Resource):
    def post(self):
        data = _user_parser.parse_args()
        user = UserModel.find_by_username(data['username'])


        if user and safe_str_cmp(user.password, data['password']):
            access_token= create_access_token(identity=user.id, fresh=True)
            refresh_token= create_refresh_token(user.id)
            return {
                'access_token':access_token,
                'refresh_token':refresh_token
            }, 200

        return {'message':'Credenziali non valide'}, 401


class TokenRefresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {'access_token': new_token}, 200

        

