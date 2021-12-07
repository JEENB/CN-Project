from fpdf import FPDF
from datetime import datetime





pdf = FPDF()

def section(string, pdf=pdf):
	pdf.set_font('Courier','B', 14)  
	pdf.cell(0,7,string, ln = 2)

def line(string, pdf= pdf):
	pdf.set_font('Courier', '', 11)  
	pdf.cell(0,5,string, ln = 2)

def multi_line(string, pdf=pdf):
	pdf.set_font('Courier', '', 11) 
	pdf.multi_cell(0,5, string)

def c_report(tot, maxi, mini, mean, medi, sd, training_points, testing_points, degree, split, user_dir):
	file_name = "report.pdf"
	width = 210
	height = 297
	pdf.set_margins(15,15)
	pdf.set_title('Regression Report')
	pdf.set_font('Helvetica', '', 14)  

	pdf.add_page()
	pdf.image("./report/1.png",0,0,width)
	pdf.write(20, f"Prepared by:")
	pdf.ln(1.5)
	pdf.set_font('Courier', '', 11)  
	pdf.write(27,"Server.py")

	pdf.add_page()
	pdf.set_font('Courier', 'B', 20)  
	pdf.cell(0,20,"Regression Report", ln = 2, align="C", border='B')
	
	line("")
	section("User Defined Parameters")
	line(f"Dataset: received.txt")
	line(f"Polynomial Degree = {degree}")
	line(f"Train-test-split = {split}%")
	line("")

	section("Dataset Exploration")
	line(f"Total Points = {tot}")
	line(f"Training Points = {training_points}")
	line(f"Testing Points = {testing_points}")
	line(f"Max = {maxi}")
	line(f"Min = {mini}")
	line(f"Mean = {mean}")
	line(f"Median = {medi}")
	line(f"Standard Deviation = {sd}")
	line("")

	section("Results")

	section("1. Polynomial Fitting")
	pdf.image(f"{user_dir}/fitting.png",50,140,w=120, h = 72)
	pdf.ln(84)
	multi_line("The above figure represents the regression line being fitted to the training instances. If the regression line passes through all the points then the polynomial degree chosen overfits the data. Similarly, if the line does not touch even a single point, you might be underfitting the training instances.")

	pdf.add_page()
	section("2. Actual vs Predicted")
	pdf.image(f"{user_dir}/actual_pred.png",50,20,w=120, h = 72)
	pdf.ln(84)
	multi_line("The above scatter plot represents the spread of predicted and actual scores. Assuming out model perfectly fits the data we can expect the points spread across the y = x line.")
	line("")
	

	section("3. Residual vs Predicted")
	pdf.image(f"{user_dir}/actual_pred.png",50,140,w=120, h = 72)
	pdf.ln(84)
	line("Residual = h(x) - f(x)")
	line("where,")
	line("h(x) is the predicted value and f(x) is the actual value")
	line("")
	multi_line("The fitted vs residuals plot is mainly useful for investigating: Whether linearity holds. This is indicated by the mean residual value for every fitted value region being close to 0. In R this is indicated by the red line being close to the dashed line. Whether homoskedasticity holds. The spread of residuals should be approximately the same across the x-axis. Whether there are outliers. This is indicated by some extreme residuals that are far from the rest.")


	pdf.add_page()
	section("4. Mean Squared Error")
	pdf.image(f"{user_dir}/compare_error.png",50,20,w=120, h = 72)
	pdf.ln(80)
	multi_line("The mean squared error is calculated as the sum of differences in actual and predicted result squared. The lower the MSE the better the model performs.")
	line("")

	section("4. Normal Q-Q Plots")
	pdf.image(f"{user_dir}/normalqq.png",50,125,w=120, h = 72)
	pdf.ln(75)
	line("")
	multi_line("The Q-Q plot, or quantile-quantile plot, is a graphical tool to help us assess if a set of data plausibly came from some theoretical distribution such as a Normal or exponential. For example, if we run a statistical analysis that assumes our dependent variable is Normally distributed, we can use a Normal Q-Q plot to check that assumption. It's just a visual check, not an air-tight proof, so it is somewhat subjective. But it allows us to see at-a-glance if our assumption is plausible, and if not, how the assumption is violated and what data points contribute to the violation.")
	line('')
	multi_line("A Q-Q plot is a scatterplot created by plotting two sets of quantiles against one another. If both sets of quantiles came from the same distribution, we should see the points forming a line that's roughly straight. Here's an example of a Normal Q-Q plot when both sets of quantiles truly come from Normal distributions.")

	pdf.add_page()
	pdf.image("./report/2.png",0,0,width)

	pdf.output(f"{user_dir}/report.pdf", 'F')
	return 0

