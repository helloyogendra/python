import requests

def bodyTemperature(doctorName, diagnosisId):
    try:
        url = "https://jsonmock.hackerrank.com/api/medical_records"
        
        # Initialize variables to store min and max temperatures
        min_temp = float('inf')
        max_temp = float('-inf')
        
        # Start with the first page
        page = 1
        
        while True:
            # Get the response from the API
            response = requests.get(f"{url}?page={page}")
            data = response.json()
            
            # Loop through each record in the current page
            for record in data['data']:
                # Check if the doctor name and diagnosis id match the filter criteria
                if record['doctor']['name'] == doctorName and record['diagnosis']['id'] == diagnosisId:
                    # Get the body temperature
                    body_temperature = record['vitals']['bodyTemperature']
                    
                    # Update min and max temperatures
                    min_temp = min(min_temp, body_temperature)
                    max_temp = max(max_temp, body_temperature)
            
            # Check if we've reached the last page
            if page >= data['total_pages']:
                break
            
            # Move to the next page
            page += 1
    except Exception as ex:
        print(ex)
    # Return the min and max temperatures as integers
    return [int(min_temp), int(max_temp)]

# Example usage
doctorName = "Dr Arnold Bullock"
diagnosisId = 2

result = bodyTemperature(doctorName, diagnosisId)
print(result)



result = bodyTemperature("Dr Allysa Ellis", 2)
print(result)

