from flask import Flask, request, jsonify
from nlp import analyze_intent
from dialogue_manager import get_response
from integration import fetch_train_schedule

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    """
    Endpoint to process chat messages from users.
    It extracts the message from the request, determines the intent,
    and returns a corresponding response.
    """
    data = request.get_json()
    user_input = data.get('message', '')
    
    # Determine intent using the NLP module
    intent = analyze_intent(user_input)
    # Fetch the dialogue response based on recognized intent
    response_message = get_response(intent, user_input)

    return jsonify({'response': response_message, 'intent': intent})


@app.route('/train-schedule', methods=['GET'])
def train_schedule():
    """
    Endpoint to simulate retrieval of a train's schedule.  
    Query parameter 'train_id' is used to identify a train.
    """
    train_id = request.args.get('train_id', '12345')  # Default train ID for simulation
    schedule = fetch_train_schedule(train_id)
    return jsonify({'train_id': train_id, 'schedule': schedule})


if __name__ == '__main__':
    app.run(debug=True)
