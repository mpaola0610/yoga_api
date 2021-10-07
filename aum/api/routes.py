
from flask import Blueprint, request, jsonify
from aum.helpers import token_required
from aum.models import db,User,Sequence,sequence_schema,sequences_schema

api = Blueprint('api',__name__, url_prefix = '/api')

@api.route('/getdata')
@token_required

def get_data(current_user_token):
    return {'some' : 'value'}

#create
@api.route('/sequences', methods = ['POST'])
@token_required
def create_sequence(current_user_token):
    warmups = request.json['warmups']
    warriors = request.json['warriors']
    balance = request.json['balance']
    cooldown = request.json['cooldown']
    user_token = current_user_token.token

    sequence = Sequence(warmups,warriors,balance,cooldown, user_token)
    db.session.add(sequence)
    db.session.commit()

    response = sequence_schema.dump(sequence)
    return jsonify(response)

#retrieve all
@api.route('/sequences', methods = ['GET'])
@token_required
def get_sequences(current_user_token):
    owner = current_user_token.token
    sequences = Sequence.query.filter_by(user_token = owner).all()
    response = sequences_schema.dump(sequences)
    return jsonify(response)

#retrieve one 
@api.route('/sequences/<id>',methods = ['GET'])
@token_required
def get_sequence(current_user_token,id):
    owner = current_user_token.token
    if owner == current_user_token.token:
        sequence = Sequence.query.get(id)
        response = sequence_schema.dump(sequence)
        return jsonify(response)
    else:
        return jsonify({'message': 'Valid Token Required'}),401

#update
@api.route('/sequences/<id>', methods = ['POST','PUT'])
@token_required
def update_sequence(current_user_token, id):
    sequence = Sequence.query.get(id)

    sequence.warmups = request.json['warmups']
    sequence.warriors = request.json['warriors']
    sequence.balance = request.json['balance']
    sequence.cooldown = request.json['cooldown']
    sequence.user_token = current_user_token.token

    db.session.commit()
    response = sequence_schema.dump(sequence)
    return jsonify(response)

#delete
@api.route('/sequences/<id>', methods = ['DELETE'])
@token_required
def delete_sequence(current_user_token, id):
    sequence = Sequence.query.get(id)
    db.session.delete(sequence)
    db.session.commit()

    response = sequence_schema.dump(sequence)
    return jsonify(response)








    