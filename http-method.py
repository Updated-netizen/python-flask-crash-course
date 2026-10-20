from flask import Flask, request

app = Flask(__name__)

@app.route('/users', methods=['Get'])
def get_users():
    return '<li> User 1<li>' \
    '<li> User 2 </li>' \
    '<li> User 3 </li>' 

#Http STATUS CODES 
@app.route("users", methods=['POST'])
def create_user():
    data = request.get_json()
    return f'user{data['name']} createsd succesfully', 201

@app.route('/users',methods=['GET'])
def search_users():
    name = request.args.get('name')
    age = request.args.get('age')

    return {
           "name":name,
           "age":age,


    }

