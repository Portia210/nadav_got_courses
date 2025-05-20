from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = {}

MAX_ID = len(tasks)

@app.route("/tasks", methods=["GET"])
def getTasks():
    return jsonify(tasks), 200


@app.route("/tasks/<int:task_id>", methods=["GET"])
def getTask(task_id):
    if task_id in tasks:
        return jsonify(tasks[task_id]), 200
    return jsonify({"error": "Task not found"}), 404


@app.route("/tasks", methods=["POST"])
def addTask():
    global MAX_ID
    data = request.get_json()
    if not data or "title" not in data or "description" not in data:
       return jsonify({"error": "Bad Request, data must include 'title' and 'description'"}), 400
    MAX_ID += 1
    data = {**data, "completed": False, "id": MAX_ID}
    tasks[MAX_ID] = data
    return jsonify(tasks[MAX_ID]), 201


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def deleteTask(task_id):
    if task_id in tasks:
       del tasks[task_id]
    return jsonify({"message": "Task deleted"}), 200


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def updateTask(task_id):
    data = request.get_json()
    if not data or "title" not in data or "description" not in data:
       return jsonify({"error": "Bad Request, data must include 'title' and 'description'"}), 400
    if task_id in tasks:
        task_to_update = tasks[task_id]
        task_to_update["title"] = data["title"] 
        task_to_update["description"] = data["description"] 
        return jsonify(tasks[task_id]), 200
    return jsonify({"error": "Task not found"}), 404   

@app.route("/tasks/<int:task_id>/completed", methods = ["GET"])
def completeTask(task_id):
    if task_id in tasks:
        tasks[task_id]["completed"] = True
        return jsonify(tasks[task_id]), 200
    return jsonify({"error": "task not found"}), 404

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)