from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    file = None
    hostname = ''
    start_time = ''
    end_time = ''
    
    if request.method == 'POST':
        file = request.files['file']
        hostname = request.form['hostname']
        start_time = request.form['start_time']
        end_time = request.form['end_time']

        # Read the file into a DataFrame
        df = pd.read_csv(file, names=['timestamp', 'host_from', 'host_to'], delim_whitespace=True)

        # Filter data based on the timestamp range and hostname
        filtered_data = df[(df['timestamp'] >= int(start_time)) & (df['timestamp'] <= int(end_time)) &
                           ((df['host_from'] == hostname) | (df['host_to'] == hostname))]
        
        data = filtered_data.to_html(index=False)

    return render_template('index.html', data=data, hostname=hostname, start_time=start_time, end_time=end_time)

if __name__ == '__main__':
    app.run(debug=True)
