from flask import Flask, request, jsonify
import requests, os, json

app = Flask(__name__)

def post_to_discord_webhook(json_data):
    webhook_url = "webhook url"

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(webhook_url, data=json.dumps(json_data), headers=headers)

    if response.status_code == 204:
        print("Message successfully sent to Discord webhook.")
    else:
        print(f"Failed to send message. Status code: {response.status_code}, Response content: {response.text}")


@app.route('/')
def main():
  return "Star The Repository: https://github.com/AxMilin/Anti-Webhook-Steal"

@app.route('/we', methods=['POST'])
def post_to_discord():
    try:
        data = request.json 
        post_to_discord_webhook(data)
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
