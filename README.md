# Price prediction and Trend analysis of the real estate market in Sydney from 2000-2019: Project overview

- Created a tool that predicts house prices given the number of beds, bathrooms, cars and location desired. Thanks to this tool, housebuyers/real estate investors will be able to make better decisions. 
- Acquired and cleaned a 200k rows dataset from Kaggle.
- Compared Linear, Lasso, decision tree and XGBRegressor to reach the best model.
- Deployed the model to production using Flask and AWS

## Code and Resources used
Python version: 3.8.8    
Packages: pandas, numpy, sklearn, xgboost, missingno, matplotlib, seaborn, flask, json, pickle    
For Web app requirements:
```
pip3 install -r requirements.txt
```
Dataset used: [Sydney house price](https://www.kaggle.com/mihirhalai/sydney-house-prices)

## Data Cleaning
After obtaining the data, I cleaned it so that I could use it to build our model. I made the following changes:
- Changed the date column format to datetime, split it, and kept only the Year and Month columns.
- Dropped the Id, postalCode and Month columns.
- Removed outliers.
- Built a new DataFrame with House as the only property type, and kept the last two years as well as the 100 most popular suburbs.

## EDA
I looked at the distribution of each property type as well as the price trend over the years. Here are a few samples:
![house_trend](house_price_trend.png)    
![evo_prop](property_price_trend.png)    


## Model Building
First, I transformed the suburb column into dummy variables. I then did a 80/20 train-test split.    
I tried four different models and evaluated them by looking at their Mean Squared Error and Root Mean Squared Error. I chose these metrics because they are easy to interpret and give us a good idea of the goodness of the fit.    

## Model Performance
XGBRegressor far outperformed the other models. Here are the results:
- Multiple Linear Regression: MSE=0.756, RMSE = 0.378
- Lasso: MSE = 1.736, RMSE = 0.868
- Decision Tree Regressor: MSE=0.750, RMSE=0.375
- XGBRegressor: MSE=0.673, RMSE=0.338

## Deployment 
In this step, I built a flask API endpoint that is hosted on AWS. The API endpoint takes in a request with a list of values, i.e number of bath/beds/cars/suburbs, and returns an estimated price.

# Deployment to the cloud (AWS EC2)
1. Connect the EC2 instance using this command: 
```
ssh -i "C:\Users\YourUserName\.ssh\SHP.pem" ubuntu@ec2-54-144-107-20.compute-1.amazonaws.com
```
2. Install nginx on the EC2 instance.
3. Copy the client, model, and server folders on the EC2 instance.
4. Install the required libraries with:
```
pip3 install -r requirements.txt
```
5. Finally, run the flask server:
```
python3 /home/ubuntu/CodeFolder/client/server.py
```
Alternatively, you can see what the app looks like [here](http://ec2-54-144-107-20.compute-1.amazonaws.com/), but you won't be able to make a prediction since the server won't be up.
