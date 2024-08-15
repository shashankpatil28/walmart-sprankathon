from app import app, db
from flask import request, jsonify
from models import Friend

# Get all friends
@app.route("/check",methods=["GET"])
def get_friends():
  friends = Friend.query.all() 
  result = [friend.to_json() for friend in friends]
  return jsonify(result)

# Create a friend
@app.route("/check",methods=["POST"])
def create_friend():
  try:
    data = request.json

    # Validations
    required_fields = ["name","role"]
    for field in required_fields:
      if field not in data or not data.get(field):
        return jsonify({"error":f'Missing required field: {field}'}), 400

    name = data.get("name")
    role = data.get("role")

    new_friend = Friend(name=name, role=role)

    db.session.add(new_friend) 
    db.session.commit()

    return jsonify(new_friend.to_json()), 201
    
  except Exception as e:
    db.session.rollback()
    return jsonify({"error":str(e)}), 500
  
