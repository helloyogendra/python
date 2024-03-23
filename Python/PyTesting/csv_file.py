def csv_data():
   
    # Replace 'data.csv' with the actual path to your CSV file
    csv_path = 'data.csv'
    
    # Read CSV file into a list of dictionaries
    with open(csv_path, 'r') as file:
        rows = [tuple(line.strip().split(',')) for line in file.readlines()]
    
    # Provide rows as parameters
    print (rows)
    print(type(rows))



csv_data()
