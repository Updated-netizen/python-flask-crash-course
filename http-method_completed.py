from flask import Flask, request, jsonify

app = Flask(__name__)



@app.route('/users', methods=['GET'])
def get_users():
    return f'All Users', 200


# POST /users
# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    return 'Users Created',201




# PUT /users/<user_id>
# Update an existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    return f'User With ID: {user_id} updated! ,200'
 
    


# DELETE /users/<user_id>
# Delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return f'user {user_id} deleted succcessfully!', 204
      

if __name__ == '__main__':
    app.run(debug=True)


