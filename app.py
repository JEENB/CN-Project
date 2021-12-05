import dearpygui.dearpygui as dpg



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
            dpg.add_file_extension(".*")
            # dpg.add_file_extension("", color=(150, 255, 150, 255))
            # dpg.add_file_extension("Source files (*.cpp *.h *.hpp){.cpp,.h,.hpp}", color=(0, 255, 255, 255))
            # dpg.add_file_extension(".h", color=(255, 0, 255, 255), custom_text="[header]")
            # dpg.add_file_extension(".py", color=(0, 255, 0, 255), custom_text="[Python]")
        dpg.add_button(label="File Selector", callback=lambda: dpg.show_item("file_dialog_id"))




def choose_file_callback(sender, app_data):
    print(f"Sender: {sender}")
    print(f"App Data: {app_data}")
    dpg.delete_item("original")
    with dpg.window(label="Example Window", width=500, height=500, tag="original"):
        dpg.add_text("Your file has been selected and sent to server.")
        dpg.add_text("Enter the desired degree of your regression model. Eg-3")
        dpg.add_input_text(label="Regression Degree", tag="model_degree")
        dpg.add_text("Slide to choose the desired percentage of dataset for testing. Rest will be used for training")
        dpg.add_slider_int(label="Testing percentage", tag="model_test_percentage")
        dpg.add_button(label="Send to server", callback=send_model_data)
    

def send_model_data():
    print(dpg.get_value("model_degree"))
    print(dpg.get_value("model_test_percentage"))
    dpg.delete_item("original")
    with dpg.window(label="Example Window", width=500, height=500, tag="original"):
        dpg.add_text("Data sent to server")
        dpg.add_text("Model is getting trained by the model.....")


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

# import dearpygui.dearpygui as dpg

# dpg.create_context()

# def callback(sender, app_data, user_data):
#     print("Sender: ", sender)
#     print("App Data: ", app_data)

# with dpg.file_dialog(directory_selector=False, show=False, callback=callback, id="file_dialog_id"):
#     dpg.add_file_extension(".*")
#     dpg.add_file_extension("", color=(150, 255, 150, 255))
#     dpg.add_file_extension("Source files (*.cpp *.h *.hpp){.cpp,.h,.hpp}", color=(0, 255, 255, 255))
#     dpg.add_file_extension(".h", color=(255, 0, 255, 255), custom_text="[header]")
#     dpg.add_file_extension(".py", color=(0, 255, 0, 255), custom_text="[Python]")

# with dpg.window(label="Tutorial", width=800, height=300):
#     dpg.add_button(label="File Selector", callback=lambda: dpg.show_item("file_dialog_id"))

# dpg.create_viewport(title='Custom Title', width=800, height=600)
# dpg.setup_dearpygui()
# dpg.show_viewport()
# dpg.start_dearpygui()
# dpg.destroy_context()

