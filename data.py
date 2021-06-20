# importing libraries
import pickle
from re import L
import pandas as pd
import flask
from flask import Flask , request , json, jsonify
import requests
# import sklearn
# from sklearn.preprocessing import OneHotEncoder
# from sklearn.pipeline import make_pipeline
# from sklearn.compose import make_column_transformer
# from sklearn.linear_model import LinearRegression
dd = pd.read_csv("cleaned car data.csv")

# app define

app = Flask(__name__)
loaded_model = pickle.load(open("Linearregcarmodel.sav", "rb"))

# x = dd.drop(["selling_price"], axis= 1)
# # print(loaded_model)
# ohe = OneHotEncoder()
# ohe.fit(x[['name', "fuel","seller_type","transmission","owner"]])

# column_trans = make_column_transformer((OneHotEncoder(categories=ohe.categories_),['name', "fuel","seller_type","transmission","owner"]),remainder = "passthrough")
# lr = LinearRegression()

# pipe = make_pipeline(column_trans, lr)


@app.route("/", methods = ["POST"])
def predict():
    user_input = request.json
    query_df = pd.DataFrame(user_input,columns=["name", "year","km_driven","fuel","seller_type","transmission","owner","engine","seats"])
    print(query_df)
    prediction = loaded_model.predict(query_df)[0]

    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = "5000")