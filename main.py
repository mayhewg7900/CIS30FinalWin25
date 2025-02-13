import tkinter
import tkcalendar
import Restaurant as r

r1 = r.Restaurant("Chilis", {'Burger':15.99, 'Fries':12.99, 'Nachos':11.99, 'Wings':5.99})
r2 = r.Restaurant("Panda Express", {'Chow Mein':10.99, 'White Rice':7.99, 'Orange Chicken':13.99, 'Fried Rice':15.99})
r3 = r.Restaurant("Taco Bell", {'Burrito':6.99, 'Taco':2.99, 'Soda':3.99, 'Refried Beans':4.99, 'Rice':3.49})



index = 0
total = 0
appointment_items = []
selected_items = []
item_buttons = []
time_buttons = []
selected_time = ''

root = tkinter.Tk()
root.title("Calendar")


# Checks if any of the appointment items have the same date as the one selected when selecting "Show Appointments"
def date_exists(date):
    global appointment_items
    for item in appointment_items:
        if item.date == date:
            return item
    return False


# If selected, checks if there is an appointment that already exists on the date selected by the user and displays the information if there is
def show_appointment():
    global appointment_items
    current_date = cal.get_date()
    item = date_exists(current_date)
    if item:
        appt_label.config(text='Upcoming Appointment - {0}: \nName: {1} \nItems: {2} \n Total: {3} \nTime: {4}'.format(item.date, item.name, item.items, item.total, item.time))
    else:
        appt_label.config(text='Upcoming Appointment - {0}: \nName: N/A \nItems: N/A \nTime: N/A'.format(current_date))


# If selected, record the time and date of the appointment, and call the function to create the restaurant selection buttons
def new_appointment(hour, minute):
    global appointment_items, index, selected_items
    selected_items.clear()
    selected_date = cal.get_date()
    time = '{:02}:{:.2f}'.format(hour,minute)
    appointment_items.append(r.Appointments())
    appointment_items[index].date = selected_date
    appointment_items[index].time = time
    for time_button in time_buttons:
        time_button.grid_forget()
    time_label.grid_forget()

    rest_label.pack()
    select_restaurant()

# Function to create all of the time option buttons, with it increasing in 15 minute increments, and laid out on a grid
def show_time_buttons():
    appt_label.pack_forget()
    new_btn.pack_forget()
    show_btn.pack_forget()
    welcomeLabel.pack_forget()
    cal.pack_forget()
    time_label.grid(row=0,column=0)
    counter = 1
    counter2 = 1
    for time_button in time_buttons:
        if counter % 4 == 0 and counter != 0:
            time_button.grid(row=counter2, column=counter)
            counter2 += 1
            counter = 1
        elif counter % 4 == 0 and counter == 0:
            time_button.grid(row=counter2,column=counter)
            counter += 1
        else:
            time_button.grid(row=counter2, column=counter)
            counter += 1

# When all items have been chosen and the player selects "NO" to adding more items, set the object total and items, output the receipt file, and redisplay the calendar and menu options from the start
def chosen_items(items):
    global total, index, appointment_items
    appointment_items[index].total = total
    total = 0

    appointment_items[index].setItems(items)
    store_receipt(appointment_items, index)
    print("\n**Receipt printed to file 'receipt.txt'**\n")
    index += 1
    display_calendar()

# Function responsible for opening and outputting text to the file
def store_receipt(appointment, i):
    fout = open('receipt.txt','w')
    fout.write("*****RECEIPT*****\n")
    fout.write("\nRestaurant:     {0}".format(appointment[i].name))
    fout.write("\nPurchased Items:     {0}".format(appointment[i].items))
    fout.write("\nTotal:     {0}".format(appointment[i].total))
    fout.write("\n\nDate:     {0}".format(appointment[i].date))
    fout.write("\nTime:     {0}".format(appointment[i].time))
    fout.close()

# Packs the restaurant buttons that were already created
def select_restaurant():
    rest1.pack()
    rest2.pack()
    rest3.pack()

# Once the restaurant has been selected, display all items listed in that restaurant object as buttons
def create_item_buttons(restaurant, first):
    global index, appointment_items
    appointment_items[index].name = restaurant.name
    if first:
        rest_label.pack_forget()
        rest1.pack_forget()
        rest2.pack_forget()
        rest3.pack_forget()
        
    else:
        add_item_label.pack_forget()
        yes_btn.pack_forget()
        no_btn.pack_forget()
        
    
    item_label.pack()
    for key, value in restaurant.items.items():
        newButton = tkinter.Button(root, text='{0} ${1}'.format(key, value), command=lambda key=key, value=value:request_item(restaurant, key, value))
        newButton.pack()
        item_buttons.append(newButton)

# When the user selects an item, display a message prompting if they want additional items. Additionally, add the current item to the object as well as add it to the object's total        
def request_item(restaurant, key, value):
    global total, selected_items
    selected_items.append(key)
    total += value
    item_label.pack_forget()
    for item_button in item_buttons:
        item_button.pack_forget()
    
    add_item_label.pack()
    yes_btn.config(command=lambda:create_item_buttons(restaurant, False))
    no_btn.config(command=lambda:chosen_items(selected_items))

    yes_btn.pack()
    no_btn.pack()

def display_calendar():
    add_item_label.pack_forget()
    yes_btn.pack_forget()
    no_btn.pack_forget()
    
    welcomeLabel.pack()
    cal.pack()
    show_btn.pack()
    new_btn.pack()
    appt_label.pack()

welcomeLabel = tkinter.Label(root, text="Welcome to the calendar program! \n Please select a date on the calendar and a button option below to get started!")
welcomeLabel.pack()

cal = tkcalendar.Calendar(root, selectmode='day', year=2025, month=2, day=12)
cal.pack()


rest1 = tkinter.Button(root, text='{0}'.format(r1.name), command=lambda:create_item_buttons(r1, True))
rest2 = tkinter.Button(root, text='{0}'.format(r2.name), command=lambda:create_item_buttons(r2, True))
rest3 = tkinter.Button(root, text='{0}'.format(r3.name), command=lambda:create_item_buttons(r3, True))

show_btn = tkinter.Button(root, text="Show Appointment", command=show_appointment)
show_btn.pack()

new_btn = tkinter.Button(root, text="New Appointment", command=lambda:show_time_buttons())
new_btn.pack()

yes_btn = tkinter.Button(root, text="YES")

no_btn = tkinter.Button(root, text="NO")

appt_label = tkinter.Label(root, text='Upcoming Appointment - {0}: \nName: N/A \nItems: N/A \nTime: N/A'.format(cal.get_date()))
appt_label.pack()

rest_label = tkinter.Label(root, text='Select the restaurant of choice: ')
item_label = tkinter.Label(root, text='Select an item of choice: ')

add_item_label = tkinter.Label(root, text='Would you like to select another item?')

time_label = tkinter.Label(root, text="Please select a time for your appointment:")


# Creates all of the time buttons and stores them in a list
for i in range(1,24):
    for j in range(0,4):
        time_button = tkinter.Button(text='{:02}:{:01}'.format(i, j*15), command=lambda i=i, j=j*15: new_appointment(i,j))
        time_buttons.append(time_button)
        

root.mainloop()