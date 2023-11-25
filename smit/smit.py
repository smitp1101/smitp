from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def studentID():
    # return student ID
    return jsonify(studentID="200575834")

@app.route('/webhook', methods=['POST'])
def webhook():
    request1 = request.get_json(force=True)
    intent = request1['queryResult']['intent']['displayName']
    
    if intent == 'closing':
        response_text = "Okay. See you later."

        response = {
            "fulfillmentText": response_text,
            "fulfillmentMessages": [
                {
                    "text": {"text": [response_text]}
                }
            ]
        }
    else:
        response = {
            "fulfillmentText": "Sorry, I can't respond that",
            "fulfillmentMessages": [
                {
                    "text": {"text": ["Sorry, I can't respond that"]}
                }
            ]
        }

    return jsonify(response)

if __name__ == '__main__':
    app.run()