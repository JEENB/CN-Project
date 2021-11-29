from sklearn import neighbors, datasets
from sklearn.linear_model import LinearRegression #regression
from sklearn.neighbors import KNeighborsRegressor #KNN
from sklearn.model_selection import train_test_split #splitting data into train and test sets
from sklearn import datasets #importing dummy data 
from sklearn.metrics import mean_squared_error # to measure the error between predicted value and actual value
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import accuracy_score
import numpy as np
from random import randint, sample
import pandas as pd


def reg_training_model(df, degree = 1):
	'''
	function: poly_reg (Gives the polynomial regression for a set of data)
		Using PolymnomialFeatures and LinearRegression functions, fits a polynomial of degree n.  

		parm: 
			1> degree: degree of the polynomial you want to fit
			2> x_train, y_train : training dataset 1d array 
			3> x_test, y_test: testing dataset 1d array 
		
		retun: 
			1> training error and testing error
		
		Note: This function will also plot n = degree number of plots
	'''
	x = df.drop('y', axis = 1)
	y = df["y"]
	x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)


	poly_features = PolynomialFeatures(degree)

	poly_x_train = poly_features.fit_transform(x_train)
	poly_x_test = poly_features.fit_transform(x_test)

	poly_model = LinearRegression().fit(poly_x_train, y_train)

	y_test_pred = poly_model.predict(poly_x_test)  # predicting h(test_data)
	y_train_pred = poly_model.predict(poly_x_train)  #predicting h(training_data)

	test_error = mean_squared_error(y_test, y_test_pred)
	training_error = mean_squared_error(y_train, y_train_pred)

	return test_error, training_error, y_test_pred

