import dearpygui.dearpygui as dpg
import os


#client code starts#
import os
import socket
import time


PORT = 2223
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), PORT))
print("[INFO] Connected to server")
 #client code ends#




def login_callback(sender, app_data, user_data):
   
    print("Save Clicked")
    print(f"sender is {sender}")
    print(f"app_data is {app_data}")
    print(f"user data is {user_data}")
    print(dpg.get_value("username"))
    print(dpg.get_value("password"))
    dpg.delete_item("original")
    
    with dpg.window(label="Example Window", width=500, height=500, tag="original"):
        dpg.add_text("you have logged in")
        with dpg.file_dialog(directory_selector=False, show=False, callback=choose_file_callback, id="file_dialog_id"):
            dpg.add_file_extension(".csv")
            # dpg.add_file_extension("", color=(150, 255, 150, 255))
            # dpg.add_file_extension("Source files (*.cpp *.h *.hpp){.cpp,.h,.hpp}", color=(0, 255, 255, 255))
            # dpg.add_file_extension(".h", color=(255, 0, 255, 255), custom_text="[header]")
            # dpg.add_file_extension(".py", color=(0, 255, 0, 255), custom_text="[Python]")
        dpg.add_button(label="File Selector", callback=lambda: dpg.show_item("file_dialog_id"))




def choose_file_callback(sender, app_data):
    print(f"Sender: {sender}")
    print(f"App Data: {app_data}")
    file_name = app_data["file_name"]
    file_path = app_data["file_path_name"]
    print(file_name)

    #============client code starts===========#
    file_size = os.path.getsize(file_path)
    print(file_size)
    print("[INFO] sending file size")
    client.send(str(file_size).encode())
    

    # Opening file and sending data.
    with open(file_name, "rb") as file:
        c = 0
        # Starting the time capture.
        start_time = time.time()

        # Running loop while c != file_size.
        while c <= file_size:
            data = file.read(1024)
            if not (data):
                break
            client.sendall(data)
            c += len(data)

        # Ending the time capture.
        end_time = time.time()

    print("[INFO] File Transfer Complete.Total time: ", end_time - start_time)
    #============client code ends==========#
    dpg.delete_item("original")
    with dpg.window(label="Example Window", width=500, height=500, tag="original"):
        dpg.add_text("Your file has been selected and sent to server.")
        dpg.add_text("Enter the desired degree of your regression model. Eg-3")
        dpg.add_input_text(label="Regression Degree", tag="model_degree")
        dpg.add_text("Slide to choose the desired percentage of dataset for testing. Rest will be used for training")
        dpg.add_slider_int(label="Testing percentage", tag="model_test_percentage")
        dpg.add_button(label="Send to server", callback=send_model_data)
    

def send_model_data():
    model_degree = dpg.get_value("model_degree")
    client.send(model_degree.encode())
    print(f"model degree is {model_degree}")
    model_test_percentage = str(dpg.get_value("model_test_percentage"))
    print(dpg.get_value("model_degree"))
    print(dpg.get_value("model_test_percentage"))
    #======client code starts=====
    
    client.send(model_test_percentage.encode())
    #========client code ends=======


    dpg.delete_item("original")
    with dpg.window(label="Example Window", width=500, height=500, tag="original"):
        dpg.add_text("Data sent to server")
        dpg.add_text("Model is getting trained by the model.....")

    #==============client code starts===========
            #Receive Report from server
    file_size = client.recv(1024).decode()
    print(file_size)
    file_path = 'sentreport.pdf'
    file = open(file_path, "wb")
    c = 0
    # Starting the time capture.
    start_time = time.time()

    # Running the loop while file is recieved.
    while c < int(file_size):
        data = client.recv(1024)
        if not (data):
            break
        file.write(data)
        c += len(data)
    file.close()

    # Ending the time capture.
    end_time = time.time()

    print("[INFO]: Report file received. Total time: ", end_time - start_time)


    #===========client code ends========

def get_model_inputs():
    pass


















dpg.create_context()
dpg.create_viewport(title="Machine Learning on Server", width=500, height=500)
dpg.setup_dearpygui()





with dpg.window(label="Example Window", width=500, height=500, tag="original"):
    dpg.add_text("Enter your login credentials")
    dpg.add_input_text(label="User Name", tag="username")
    dpg.add_input_text(label="Password", tag="password")
    dpg.add_button(label="Login", callback=login_callback)
    # dpg.add_slider_float(label="float")





dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()


