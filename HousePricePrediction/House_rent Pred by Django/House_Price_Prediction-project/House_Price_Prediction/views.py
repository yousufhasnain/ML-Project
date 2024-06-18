from sklearn.preprocessing import StandardScaler,OneHotEncoder
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer
from scipy.stats import t
import math,os

from django.shortcuts import render
def home(request):
    return render(request,"home.html")

def predict(request):
    return render(request,"predict.html")

def  result(request):
    path = r"D:\python project\House_rent Pred by Django\dataset\Clean_data.csv"
    rent_df = pd.read_csv(path)
    rent_df=rent_df.drop(columns=['Unnamed: 0'])
    x = rent_df.drop(columns=["Rent","Location"])
    y = rent_df["Rent"]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

    # column_trans = make_column_transformer(
    #     (OneHotEncoder(sparse=False), ['Location']),
    #     remainder='passthrough'
    # )
    # column_trans,

    pipe = make_pipeline( StandardScaler(), DecisionTreeRegressor())
    pipe.fit(x_train, y_train)
    y_pred=pipe.predict(x_test)
    
    size = int(request.GET['size'])
    room = int(request.GET['room'])
    total_bathroom = int(request.GET['total bathroom'])
    attached_bathroom = int(request.GET['attached bathroom'])
    varanda = int(request.GET['varanda'])
    dinning = int(request.GET['dinning'])
    floor = int(request.GET['floor'])
    lift = int(request.GET['lift'])
    input_data = pd.DataFrame([[size, room, total_bathroom, attached_bathroom, varanda, dinning, floor, lift]],
                              columns=['Size', 'Room', 'Total Bathroom', 'Attached Bathroom', 'Varanda', 'Dining', 'Floor', 'Lift'])
    prediction = pipe.predict(input_data)[0]
    def calculate_prediction_interval(y_pred, rmse, confidence=0.50):
        df = len(y_pred) - 1
        std_error = rmse * np.sqrt(1 + 1/len(y_pred))
        t_statistic = t.ppf((1 + confidence) / 2, df=df)
        margin_of_error = t_statistic * std_error
        return margin_of_error
    Mse=mean_squared_error(y_test,y_pred)
    Rmse=math.sqrt(Mse)
    
    margin_error = calculate_prediction_interval(y_pred, Rmse)
    lower_bound=round(prediction-margin_error)
    upper_bound=round(prediction+margin_error)
    rent=f"The Predicted Rent is: TK {str(lower_bound)} - {str(upper_bound)}"

    return render(request,"predict.html",{"result2":rent}) 