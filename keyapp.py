from flask import Flask, render_template, request, jsonify
import time
import pandas as pd
import numpy as np
import os

app = Flask(__name__)

def classify_typing_speed(avg_speed):
    if avg_speed < 0.2:
        return "Fast Typer"
    elif avg_speed < 0.5:
        return "Moderate Typer"
    else:
        return "Slow Typer"

@app.route('/')
def index():
    return render_template('keyindex.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data.get("text", "")
    timestamps = data.get("timestamps", [])
    
    # Basic validation
    if len(timestamps) < 2:
        return jsonify({"message": "Not enough data"}), 400
     
    # Calculate time differences between keystrokes
    time_diffs = [timestamps[i] - timestamps[i-1] for i in range(1, len(timestamps))]
    
    # Filter out outliers - remove pauses over 3 seconds
    filtered_diffs = [diff for diff in time_diffs if diff < 3.0]
    
    # Calculate average speed
    if filtered_diffs:
        avg_speed = sum(filtered_diffs) / len(filtered_diffs)
    else:
        avg_speed = sum(time_diffs) / len(time_diffs)
    
    # Classify typing pattern
    classification = classify_typing_speed(avg_speed)
    
    # Log data for further analysis (optional)
    log_keystroke_data(text, timestamps, classification)
    
    return jsonify({
        "speed": avg_speed,
        "classification": classification
    })

def log_keystroke_data(text, timestamps, classification):
    """Optional function to log keystroke data for later analysis"""
    try:
        # Create logs directory if it doesn't exist
        if not os.path.exists('logs'):
            os.makedirs('logs')
        
        # Generate timestamp for the log file
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"logs/keystroke_log_{timestamp}.txt"
        
        # Write log data
        with open(filename, 'w') as f:
            f.write(f"Text: {text}\n")
            f.write(f"Classification: {classification}\n")
            f.write("Timestamps:\n")
            for i, ts in enumerate(timestamps):
                f.write(f"{i}: {ts}\n")
                
            # Write intervals
            if len(timestamps) > 1:
                f.write("Intervals:\n")
                for i in range(1, len(timestamps)):
                    interval = timestamps[i] - timestamps[i-1]
                    f.write(f"{i-1} to {i}: {interval:.4f}s\n")
    except:
        # Silently handle errors - don't interrupt main functionality
        pass

if __name__ == '__main__':
    app.run(debug=True)