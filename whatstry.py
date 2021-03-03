import socket
import tkinter as tk
from datetime import datetime
from time import sleep
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

now = datetime.now()

# driver = webdriver.Chrome(executable_path="/home/beldozer/Desktop/sadasd1231/chromedriver")

#Keep the current chrome session
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=./User_Data')

master = tk.Tk()
master.title("Whatsapp Bot Made by NonameNowifeⒸ")
width = 500
height = 500
canvas1 = tk.Canvas(master, width=width, height=height, relief='raised', bg='white')
canvas1.pack()

# load the .gif image file
# canvas1.create_line(15, 25, 200, 25)
canvas1.create_line(width / 1, 0, width / 1, height, dash=(1, 1))
canvas1.create_line(800, height / 1, 0, height / 1, dash=(1, 1))

cx = canvas1.canvasx(width / 1)
cy = canvas1.canvasy(height / 1)
cid = canvas1.find_closest(cx, cy)[0]
canvas1.itemconfigure(cid, fill="blue")

canvas1.create_line(55, 85, 155, 85, 105, 180, 55, 85)
# canvas1.create_text(400, 10, fill="black", font="Times 20 italic bold",
#                  text="Whatsapp Bot")
gif1 = tk.PhotoImage(file='images/logo1.png')

# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
#canvas1.create_image(500, 500, image=gif1)

# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
canvas1.create_image(width / 2, height / 3, image=gif1)

def blueSelection(event=None):
    l1 = tk.Label(master,
                  text="Enter the Message ", bg="blue")
    l2 = tk.Label(master,
                  text="How many message do you want to send ?", bg="blue")
    l3 = tk.Label(master,
                  text="Enter the Phone Number ", bg="blue")

    canvas1.create_window(100, 250, window=l1)
    canvas1.create_window(150, 290, window=l2)
    canvas1.create_window(100, 330, window=l3)

    e1 = tk.Entry(master)

    e2 = tk.Entry(master)

    e3 = tk.Entry(master)

    canvas1.create_window(400, 250, window=e1)
    canvas1.create_window(400, 290, window=e2)
    canvas1.create_window(400, 330, window=e3)

    def Driver():
        message_text = e1.get()  # message you want to send
        no_of_message = e2.get()
        if type(no_of_message) == int:
            print("The number is integer" + str(no_of_message))
        else:
            try:
                no_of_message = int(no_of_message)
            except:
                m1 = tk.Label(master,
                              text="ERROR : Please enter digits for No of Messages.", fg="red", bg="black")

                canvas1.create_window(250, 170, window=m1)
                m1.after(5000, m1.destroy)

        if len(message_text) == 0 or len(str(no_of_message)) == 0:
            m1 = tk.Label(master,
                          text="ERROR : Please fill the blanks.", fg="red", bg="black")

            canvas1.create_window(250, 140, window=m1)
            m1.after(5000, m1.destroy)

        phone_number = int(e3.get())

        if len(str(phone_number)) != 12:
            m1 = tk.Label(master,
                          text="ERROR : Please enter 12 digits for Phone Number.", fg="red", bg="black")

            canvas1.create_window(250, 200, window=m1)
            m1.after(5000, m1.destroy)
        else:
            phone_number = [phone_number]
            driver = webdriver.Chrome(executable_path="/home/beldozer/Desktop/sadasd1231/chromedriver", options=options)
            driver.get("http://web.whatsapp.com")
            sleep(15)  # wait time to scan the code in second

            def element_presence(driver, by, xpath, time):
                element_present = EC.presence_of_element_located((By.XPATH, xpath))
                WebDriverWait(driver, time).until(element_present)

            def is_connected():
                try:
                    # connect to the host -- tells us if the host is actually
                    # reachable
                    socket.create_connection(("www.google.com", 80))
                    return True
                except:
                    is_connected()

            def send_whatsapp_msg(driver, phone_no, text, no):
                sleep(5)
                driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))

                try:
                    sleep(7)
                    element_presence(driver, By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]', 30)
                    txt_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                    for x in range(no):
                        txt_box.send_keys(text)
                        txt_box.send_keys("\n")

                except Exception as e:
                    print("Invalid Phone Number:" + str(phone_no))

            for mobile_no in phone_number:
                try:
                    sleep(5)
                    send_whatsapp_msg(driver, mobile_no, message_text, no_of_message)

                except Exception as e:
                    sleep(10)
                    is_connected()
                    
    c1 = tk.Button(text='Send', command=Driver, bg='blue', fg='white',
    font=('helvetica', 9, 'bold'))
    canvas1.create_window(250, 380, window=c1)
    
    
    
ch = tk.Label(master, text="Send Message X Times", fg="white", bg="lightblue")
ch.bind("<Button-1>", blueSelection)
ch.config(font=('helvetica', 14))
canvas1.create_window(120, 270, window=ch)








master.mainloop()
