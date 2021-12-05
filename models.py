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
import matplotlib.pyplot as plt
import pandas as pd

def reg_training_model(df, degree = 1, split_ratio = 0.2 ):
	'''
	function: poly_reg (Gives the polynomial regression for a set of data)
		Using PolymnomialFeatures and LinearRegression functions, fits a polynomial of degree n.  

		parm: 
			1> degree: degree of the polynomial you want to fit
			2> df: pandas df with x and y
			3> split_ratio: testing and training 
		
		retun: 
			1> training error and testing error
		
		Note: This function will also plot n = degree number of plots
	'''
	y = df['y']
	x = df.drop('y', axis = 1)

	x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = split_ratio)


	poly_features = PolynomialFeatures(degree)

	poly_x_train = poly_features.fit_transform(x_train)
	poly_x_test = poly_features.fit_transform(x_test)

	poly_model = LinearRegression().fit(poly_x_train, y_train)

	y_test_pred = poly_model.predict(poly_x_test)  # predicting h(test_data)
	y_train_pred = poly_model.predict(poly_x_train)  #predicting h(training_data)

	test_error = mean_squared_error(y_test, y_test_pred)
	training_error = mean_squared_error(y_train, y_train_pred)



	##@Plotting
	x_test_1d = np.ravel(x_train)
	df = pd.DataFrame({"x_test": x_test_1d, "y_test_pred": y_train_pred})
	df.sort_values(by=["x_test"], inplace = True)

	plt.scatter(x = x_train, y = y_train)
	plt.plot(df.x_test, df.y_test_pred, label = "Polynomial degree = {}".format(degree), color='r')
	plt.legend(loc='upper left')	
	plt.savefig("server_data/fitting.png")



	return 0

