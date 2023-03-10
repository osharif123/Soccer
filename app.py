from flask import Flask, render_template, request
from datetime import datetime
import pandas as pd

app = Flask(__name__)

# Define the path to the Excel file
excel_path = 'players.xlsx'

# Define the route for the RSVP form
@app.route('/', methods=['GET', 'POST'])
def rsvp():
    if request.method == 'POST':
        # Add the player's name and timestamp to the list
        player_name = request.form['name']
        timestamp = datetime.now()
        players.append((player_name, timestamp))

        # Add the player's name and timestamp to the Excel file
        df = pd.DataFrame(players, columns=['Name', 'Timestamp'])
        df.to_excel(excel_path, index=False)

        return render_template('thanks.html', name=player_name)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    # Load the existing list of players from the Excel file
    try:
        df = pd.read_excel(excel_path)
        players = list(df[['Name', 'Timestamp']].itertuples(index=False, name=None))
    except:
        players = []

    app.run(debug=True)
