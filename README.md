# Anti Discord Webhook Steal Code
## Overview
This Python code is designed to prevent the stealing of Discord webhooks by implementing a simple Flask application. The script listens for incoming POST requests on the /we endpoint and forwards the data to the specified Discord webhook.

## Prerequisites
- Python 3.x
## Requests library
```bash
pip install Flask requests
```
## Usage
1. Clone the repository:
```bash
git clone https://github.com/yourusername/anti-discord-webhook-steal.git
cd anti-discord-webhook-steal
```
2. Open the app.py file and replace "Webhook Url" with your actual Discord webhook URL.
```python
webhook_url = "Your Webhook URL"
```
3. Run the Flask application:
```bash
python app.py
```
The application will start listening on IP Address in the console
![image](https://github.com/AxMilin/Anti-Webhook-Steal/assets/151182569/a81281f7-ee21-41a8-811b-c30c5b47b693)



## Features
- **Secure Webhook Posting**: The script ensures that the Discord webhook URL is not exposed in the client-side code, reducing the risk of theft.

- **Error Handling**: The code includes basic error handling to gracefully handle exceptions and provide informative responses.

## Disclaimer
This code serves as a basic example and should not be solely relied upon for security. It is essential to implement additional security measures based on your application's specific needs.

## Contributing
Feel free to contribute to the project by submitting issues or pull requests.

## License
This code is licensed under the <a target="LICENSE">MIT License</a>. See the LICENSE file for details.
