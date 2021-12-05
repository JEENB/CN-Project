from fpdf import FPDF
from datetime import datetime


width = 210
height = 297
degree = 2
split = 20
points = 100
training_points = 80
testing_points = 20

dataset = "dataste.csv"


file_name = "report.pdf"

pdf = FPDF()

def section(string):
	pdf.set_font('Courier','B', 14)  
	pdf.cell(0,7,string, ln = 2)

def line(string):
	pdf.set_font('Courier', '', 11)  
	pdf.cell(0,5,string, ln = 2)

def multi_line(string):
	pdf.set_font('Courier', '', 11) 
	pdf.multi_cell(0,5, string)

def create_report():
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
	line(f"Dataset: {dataset}")
	line(f"Polynomial Degree = {degree}")
	line(f"Train-test-split = {split}%")
	line("")

	section("Dataset Exploration")
	line(f"Total Points = {points}")
	line(f"Training Points = {training_points}")
	line(f"Testing Points = {testing_points}")
	line(f"Max = {testing_points}")
	line(f"Min = {testing_points}")
	line(f"Mean = {testing_points}")
	line(f"Median = {testing_points}")
	line(f"Standard Deviation = {testing_points}")
	line("")

	section("Results")

	section("1. Polynomial Fitting")
	pdf.image("neworignial.jpeg",50,140,w=120, h = 72)
	pdf.ln(84)
	multi_line("The above figure represents the regression line being fitted to the training instances. If the regression line passes through all the points then the polynomial degree chosen overfits the data. Similarly, if the line does not touch even a single point, you might be underfitting the training instances.")


	
	pdf.output("./server_data/report.pdf", 'F')


create_report()