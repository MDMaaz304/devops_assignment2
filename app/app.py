from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Temporary in-memory storage
tickets_data = []
ticket_counter = 1

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/api/tickets', methods=['GET'])
def get_all_tickets():
    return jsonify(tickets_data)

@app.route('/api/tickets', methods=['POST'])
def add_ticket():
    global ticket_counter
    data = request.json

    ticket = {
        'id': ticket_counter,
        'event': data.get('event'),
        'name': data.get('name'),
        'email': data.get('email'),
        'quantity': int(data.get('quantity', 1)),
        'price': data.get('price', 100)  # default price
    }

    tickets_data.append(ticket)
    ticket_counter += 1

    return jsonify(ticket), 201

@app.route('/api/tickets/<int:ticket_id>', methods=['DELETE'])
def remove_ticket(ticket_id):
    global tickets_data
    tickets_data = [t for t in tickets_data if t['id'] != ticket_id]
    return jsonify({'message': 'Ticket cancelled successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
