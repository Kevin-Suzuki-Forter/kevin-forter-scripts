import csv
import json

# Specify the path to your CSV file
csv_file_path = 'fedex_fraud_order_check_2023112206.csv'

# Specify the path where you want to save the JSON file
json_file_path = 'output.json'

# Define key mappings
key_mapping = {
    'ORDER_NUM': 'orderId',
    'ORDER_DATE': 'checkoutTime',
    'SHIPPING_METHOD': 'primaryDeliveryDetails.deliveryMethod',
    'ORDER_TYPE': 'ORDER_TYPE'

    # Add more mappings as needed
}

# Read CSV file and convert to JSON
data = []
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # Apply key mapping during the iteration
        translated_row = {key_mapping.get(key, key): value for key, value in row.items()}
        data.append(translated_row)

# Write JSON data to a file
with open(json_file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)

print(f'Conversion complete. JSON file saved at {json_file_path}')