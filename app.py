from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system username
    system_username = os.getenv("USER") or os.getenv("USERNAME")

    # Get server time in IST (UTC+5:30)
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)

    # Get system's top output (first 10 lines)
    top_output = subprocess.run(["top", "-b", "-n", "1"], capture_output=True, text=True).stdout
    top_output = "\n".join(top_output.split("\n")[:10])  # Show only first 10 lines

    return f"""
    <h1>System Info</h1>
    <p><strong>Name:</strong> Pragati priya </p>
    <p><strong>Username:</strong> {system_username}</p>
    <p><strong>Server Time (IST):</strong> {ist_time.strftime('%Y-%m-%d %H:%M:%S')}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
