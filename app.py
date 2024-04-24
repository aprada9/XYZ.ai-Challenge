from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        hostname = request.form['hostname']
        start_time = int(request.form['start_time'])
        end_time = int(request.form['end_time'])

        # Read the file into a DataFrame
        df = pd.read_csv(file, names=['timestamp', 'host_from', 'host_to'], delim_whitespace=True)

        # Filter data based on the timestamp range and hostname
        filtered_data = df[(df['timestamp'] >= start_time) & (df['timestamp'] <= end_time) &
                           ((df['host_from'] == hostname) | (df['host_to'] == hostname))]

        return render_template('index.html', data=filtered_data.to_html(index=False))
    else:
        return render_template('index.html', data=None)

if __name__ == '__main__':
    app.run(debug=True)
