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
import statsmodels.api as sm


def reg_training_model(df, user_dir, degree = 1, split_ratio = 0.2):
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


	##-------------------------------------------------
	#---------- Regression Line ----- -----------------
	##-------------------------------------------------

	plt.figure(0,figsize=(8,5))
	plt.scatter(x = x_train, y = y_train, label = "Training Set")
	plt.xlabel("X")
	plt.ylabel("Y")
	plt.plot(df.x_test, df.y_test_pred, label = "Polynomial degree = {}".format(degree), color='r')
	plt.legend(loc='upper left')	
	plt.title("Polynomial Fitting")
	plt.savefig(f"{user_dir}/fitting.png")
	plt.show()


	##-------------------------------------------------
	#---------- Ac vs Predicted -----------------
	##-------------------------------------------------
	
	# x axis = actual 
	# y axis = predicted
	plt.figure(1,figsize=(8,5))
	plt.scatter(x = y_train, y = y_train_pred, label = "Training Set", color = 'b')
	plt.scatter(x = y_test, y = y_test_pred, label = "Testing Set", color = 'r')

	# y = x line
	y = max(max(y_test),max(y_test_pred), max(y_train), max(y_train_pred))
	y_= min(min(y_test), min(y_test_pred), min(y_train), min(y_train_pred))
	x = np.linspace(y_,y,1000)
	plt.plot(x,x, color = "g")
	plt.xlabel("Actual Results")
	plt.ylabel("Predicted Results")
	plt.legend(loc='upper left')	
	plt.title("Actual VS Predicted")
	plt.savefig(f"{user_dir}/actual_pred.png")



	##------------------------------------
	#---------- Bar Plot -----------------
	##------------------------------------
	plt.figure(2,figsize=(8,5))
	plt.bar(["Test", "Training"], [test_error, training_error], color=['r','b'])
	plt.ylabel("Dataset")
	plt.ylabel("Mean Square Error")
	plt.title("Comparing Errors")
	plt.savefig(f"{user_dir}/compare_error.png")



	##-------------------------------------------------
	#---------- Resudal vs Predicted ------------------
	##-------------------------------------------------

	residual_test = np.subtract(y_test_pred,y_test)
	residual_train = np.subtract(y_train_pred, y_train)
	plt.figure(3,figsize=(8,5))
	plt.scatter(x =y_test_pred, y = residual_test,label = "Testing Set", color = 'r')
	plt.scatter(x =y_train_pred, y = residual_train, label = "Training Set", color = 'b')
	plt.xlabel("Predicted")
	plt.ylabel("Residual")
	plt.legend(loc='upper left')	
	plt.title("Residual VS Predicted")
	plt.savefig(f"{user_dir}/residual_pred.png")



	
	##-------------------------------------------------
	#---------- Normal Q- Q----------------------------
	##-------------------------------------------------
	fig, (ax1, ax2) = plt.subplots(1,2, figsize=(10,6))
	fig.suptitle('Normal Q-Q')
	sm.qqplot(residual_train, line='45',  ax = ax1)
	ax1.set_title("Train")
	ax1.set_ylabel("Standard Residual")
	sm.qqplot(residual_test, line='45',  ax = ax2)
	ax2.set_title("Test")
	ax2.set_ylabel("Standard Residual")
	plt.savefig(f"{user_dir}/normalqq.png")
	return 0

