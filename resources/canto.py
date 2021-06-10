from flask_restful import Resource, reqparse
from models.canto import CantoModel
from typing import Text

class Canto(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('parte',
    type=Text,
    required=False,
    help="Parte non trovata"
    )
    parser.add_argument('author',
    type=Text,
    required=False,
    help="Autore non trovato"
    )

    parser_CantoByNameAndParte = reqparse.RequestParser()
    parser_CantoByNameAndParte.add_argument('name',
    type=Text,
    required=True,
    help="Nome non trovato"
    )
    parser_CantoByNameAndParte.add_argument('parte',
    type=Text,
    required=True,
    help="Parte non trovata"
    )


    def get(self, name):
        canto = CantoModel.find_by_name(name)
        if canto:
            return canto.json()
        return {'message': 'Canto non trovato'}, 404

    def post(self, name):
        if CantoModel.find_by_name(name):
            return {'message': "Il canto {} esiste già".format(name)}, 400

        canto = CantoModel(name)
        try:
            canto.save_to_db()
        except:
            return {"message": "Errore nel salvataggio del canto nel db."}, 500

        return canto.json(), 201

    def delete(self, name):
        canto = CantoModel.find_by_name(name)
        if canto:
            canto.delete_from_db()

        return {'message': 'Canto cancellato'}


class CantoByNameAndParte(Resource):
    def get(self):
        data= Canto.parser_CantoByNameAndParte.parse_args()
        return {'canti': list(map(lambda x: x.json(), CantoModel.query.filter_by(name=data['name'], parte=data['parte'])))}


class CantoList(Resource):
    def get(self):
        return {'canti': list(map(lambda x: x.json(), CantoModel.query.all()))}

class CantoListByParte(Resource):
    def get(self):
        data= Canto.parser.parse_args()
        return {'canti': list(map(lambda x: x.json(), CantoModel.query.filter_by(parte=data['parte'])))}


def get_canto_id(name, parte):
    canto = CantoModel.find_by_nameAndParte(name, parte)
    if canto:
        return canto.id
    return {'message:':'Canto non trovato'},404
    
