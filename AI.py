from flask import Flask, jsonify

app = Flask(__name__)

# Sample data (can be replaced with a database)
sample_data = [{'id': 1, 'name': 'vasiliy'}, {'id': 2, 'name': 'PS'}]

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify({'users': sample_data})

if __name__ == '__main__':
    app.run(debug=True)
