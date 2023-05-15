import csv

# function to retrieve data for a given query
def retrieve_data(date=None, name=None, age=None, profession=None, item=None, amount=None):
    # read in the data from the CSV file
    with open('data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = []

        # loop through each row in the CSV file
        for row in reader:
            # check if the row matches the query
            if (date is None or row['Date'] == date) and \
               (name is None or row['Name'] == name) and \
               (age is None or row['Age'] == age) and \
               (profession is None or row['Profession'] == profession) and \
               (item is None or row['Item'] == item) and \
               (amount is None or row['Amount'] == amount):
                # if the row matches the query, append it to the list of matching rows
                rows.append(row)

        # return the list of matching rows
        return rows

# function to add data for a new day
def add_data(date, name, age, profession, item, amount):
    # open the CSV file in append mode and write the new row of data
    with open('data.csv', 'a', newline='') as csvfile:
        fieldnames = ['Date', 'Name', 'Age', 'Profession', 'Item', 'Amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'Date': date, 'Name': name, 'Age': age, 'Profession': profession, 'Item': item, 'Amount': amount})

# example usage
add_data('2023-05-15', 'John', '28', 'Engineer', 'Laptop', '1500')
add_data('2023-05-15', 'Mary', '35', 'Doctor', 'Stethoscope', '100')
add_data('2023-05-14', 'Bob', '42', 'Teacher', 'Textbook', '50')

rows = retrieve_data(date='2023-05-15', profession='Engineer')
for row in rows:
    print(row)
# In this program, the add_data() function is used to add a new row of data to a CSV file. The function takes in the date, name, age, profession, item purchased, and amount as arguments and writes them as a new row to a CSV file called data.csv.

# The retrieve_data() function is used to retrieve rows of data from the CSV file based on a given query. The function takes in optional arguments for date, name, age, profession, item, and amount. It reads in the data from the CSV file and loops through each row to check if it matches the query. If a row matches the query, it is appended to a list of matching rows. The function then returns the list of matching rows.

# In the example usage, three rows of data are added to the CSV file using the add_data() function. The retrieve_data() function is then called with a query for all rows with a date of '2023-05-15' and a profession of 'Engineer'. The matching rows are printed to the console.

# You can modify the queries passed to retrieve_data() to search for specific values in the CSV file

