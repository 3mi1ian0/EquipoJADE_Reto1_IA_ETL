from flask import Flask, render_template, request
import numpy as np
import xgboost as xgb

app = Flask(__name__)

# Load your XGBoost model for sales prediction
xgboost_model = xgb.Booster(model_file='xgboost_model.txt')

# Define the options for each dropdown
weekday = list(range(0,7))

days = list(range(1, 32))

months = list(range(1,13))

types = list(range(0,5))

store_nbrs = list(range(0, 55))

payday = [0,1]

city = list(range(0,22))

states = list(range(0,16))

families = list(range(0,33))

cluster = list(range(0,17))

event_name = list(range(0,13))

earthquake = days

local_holiday_name = list(range(0,27))

regional_holiday_name = list(range(0,5))

national_holiday_name = list(range(0,67))

onpromotions = [
  0,  1,  2,  3,  4,  5,  6,  7,  8,  9,
 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
 40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
 60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
 70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
 90, 91, 92, 93, 94, 95, 96, 97, 98, 99,
100,101,102,103,104,105,106,107,108,109,
110,111,112,113,114,115,116,117,118,119,
120,121,122,123,124,125,126,127,128,129,
130,131,132,133,134,135,136,137,138,139,
140,141,142,143,144,145,146,147,148,149,
150,151,152,153,154,155,156,157,158,159,
160,161,162,163,164,165,166,167,168,169,
170,171,172,173,174,175,176,177,178,179,
180,181,182,183,184,185,186,187,188,189,
190,191,192,193,194,195,196,197,198,199,
200,201,202,203,204,205,206,207,208,209,
210,211,212,213,214,215,216,217,218,219,
220,221,222,223,224,225,226,227,228,229,
230,231,232,233,234,235,236,237,238,239,
240,241,242,243,244,245,246,247,248,249,
250,251,252,253,254,255,258,259,261,263,
264,269,275,276,277,279,281,282,283,285,
286,289,290,293,294,297,299,300,302,304,
305,306,307,312,313,317,320,322,326,330,
332,333,342,383,391,407,411,420,424,425,
435,441,444,446,452,464,467,469,470,473,
474,476,479,481,485,486,489,496,507,510,
511,512,519,520,528,536,539,543,547,551,
591,600,609,624,626,628,629,630,633,639,
642,644,646,655,657,664,668,672,677,678,
684,697,702,710,716,717,718,719,720,722,
726,741
]

# routes
@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template("index.html", 
                           weekday=weekday, 
                           days=days, 
                           months=months, 
                           types=types, 
                           store_nbrs=store_nbrs, 
                           payday=payday, 
                           city=city, 
                           states=states, 
                           families=families, 
                           cluster=cluster, 
                           event_name=event_name, 
                           earthquake=earthquake, 
                           local_holiday_name=local_holiday_name, 
                           regional_holiday_name=regional_holiday_name, 
                           national_holiday_name=national_holiday_name, 
                           onpromotions=onpromotions)


@app.route("/predict", methods=['POST'])
def predict_sales():
    if request.method == 'POST':
        # Get form data
        weekd = int(request.form['weekd']) 
        day = int(request.form['day'])
        month = int(request.form['month'])
        type_nbr = int(request.form['type_nbr'])
        store_nbr = int(request.form['store_nbr'])
        payd = int(request.form['payd'])
        city_nbr = int(request.form['city_nbr'])
        state = int(request.form['state'])
        family = int(request.form['family'])
        cluster_nbr = int(request.form['cluster_nbr'])
        event_n = int(request.form['event_n'])
        earth = int(request.form['earth'])
        local_h_name = int(request.form['local_h_name'])
        regional_h_name = int(request.form['regional_h_name'])
        national_h_name = int(request.form['national_h_name'])
        onpromotion_nbr = int(request.form['onpromotion_nbr'])
        transactions = 0
        
        # Check if any required parameter is missing
        if any(val == "" for val in [weekd, day, month, type_nbr, store_nbr, payd, city_nbr, state, family, cluster_nbr, event_n, earth, local_h_name, regional_h_name, national_h_name, onpromotion_nbr]):
            return render_template("index.html", error_message="Some columns are missing")
                       
        # Prepare input data for prediction
        input_data = np.array([store_nbr, family, onpromotion_nbr, weekd, month, day, payd, city_nbr, state, type_nbr, cluster_nbr, event_n, earth, local_h_name, regional_h_name, national_h_name, transactions])
        input_data = input_data.reshape(1, -1)  # Reshape to a 2D matrix with one row

        # Make sales prediction using your XGBoost model
        dinput = xgb.DMatrix(input_data)
        predicted_sales = xgboost_model.predict(dinput)


        return render_template("index.html", prediction=predicted_sales[0])

if __name__ == '__main__':
    app.run(debug=True)