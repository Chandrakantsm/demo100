# create a list to store data for each day
data_list = []
import tkinter as tk
import datetime

def date():
    x = datetime.datetime.now()
    print(x)


def submit():
    # get the input values from the text boxes
    
    name = name_entry.get()
    age = age_entry.get()
    profession = profession_entry.get()
    item = item_entry.get()
    amount = amount_entry.get()

    # create a dictionary to store the data for the day
    day_data = {'Name': name, 'Age': age, 'Profession': profession, 'Item': item, 'Amount': amount}

    # append the day's data to the list of data
    data_list.append(day_data)

    # clear the text boxes
    datetime.delete(0,tk.END)
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    profession_entry.delete(0, tk.END)
    item_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

def retrieve_data():
    # loop through the list of data and display it in the console
    for day_data in data_list:
        print('Name:', day_data['Name'])
        print('Age:', day_data['Age'])
        print('Item:', day_data['Item'])
        print('Amount:', day_data['Amount'])
        print('--------------------------')

# create the tkinter window
root = tk.Tk()

name_label = tk.Label(root, text='Date:')
name_label.grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)


# create the input labels and text boxes
name_label = tk.Label(root, text='Name:')
name_label.grid(row=1, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1)

age_label = tk.Label(root, text='Age:')
age_label.grid(row=2, column=0)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1)

profession_label = tk.Label(root, text='Profession:')
profession_label.grid(row=3, column=0)
profession_entry = tk.Entry(root)
profession_entry.grid(row=3, column=1)

item_label = tk.Label(root, text='Item Purchased:')
item_label.grid(row=4, column=0)
item_entry = tk.Entry(root)
item_entry.grid(row=4, column=1)

amount_label = tk.Label(root, text='Amount:')
amount_label.grid(row=5, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=5, column=1)

# create the submit and retrieve buttons
submit_button = tk.Button(root, text='Submit', command=submit)
submit_button.grid(row=6, column=0)

retrieve_button = tk.Button(root, text='Retrieve Data', command=retrieve_data)
retrieve_button.grid(row=6, column=1)

# start the tkinter main loop
root.mainloop()
