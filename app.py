import pandas as pd
from flask import Flask, request

app = Flask(__name__)

# This route will handle POST requests from TradingView alerts
@app.route('/webhook', methods=['POST'])
def webhook():
    # Get the data sent by TradingView in JSON format
    data = request.get_json()
    print(f"Received data: {data}")  # Log the data to check if everything is correct
    
    # Convert the received data into a pandas DataFrame (easier to handle for Excel)
    df = pd.DataFrame([data])
    
    # Try to append the data to an existing Excel file
    try:
        df.to_excel('live_trading_data.xlsx', mode='a', header=False, index=False)
    except FileNotFoundError:
        # If the file does not exist, create a new one and write the header
        df.to_excel('live_trading_data.xlsx', mode='w', header=True, index=False)
    
    return "Data received and saved to Excel!", 200  # Send a success response to TradingView

# Run the Flask web server
if __name__ == '__main__':
    app.run(debug=False)  # Running the app with debug off for production
