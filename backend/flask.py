# app.py
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from our React frontend

# Sample data
todos = [
    {"id": 1, "text": "Learn Flask", "completed": True},
    {"id": 2, "text": "Learn React", "completed": False},
    {"id": 3, "text": "Build a Flask-React app", "completed": False}
]

@app.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/api/todos', methods=['POST'])
def add_todo():
    new_todo = request.json
    new_todo['id'] = len(todos) + 1
    new_todo['completed'] = False
    todos.append(new_todo)
    return jsonify(new_todo), 201

@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            todo['completed'] = not todo['completed']
            return jsonify(todo)
    return jsonify({"error": "Todo not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)