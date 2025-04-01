from flask import Flask, request, jsonify

app = Flask(__name__)
items = []  # List to store items in memory

# Add a new item
@app.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    if not data or 'item' not in data:
        return jsonify({"error": "Missing 'item' field"}), 400

    item = data['item']
    if item in items:
        return jsonify({"message": f"'{item}' already exists"}), 400

    items.append(item)
    return jsonify({"message": f"'{item}' added successfully", "items": items}), 201

# Delete a specific item
@app.route('/items/<string:item_name>', methods=['DELETE'])
def delete_item(item_name):
    if item_name not in items:
        return jsonify({"error": f"'{item_name}' not found"}), 404

    items.remove(item_name)
    return jsonify({"message": f"'{item_name}' deleted successfully", "items": items}), 200

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

