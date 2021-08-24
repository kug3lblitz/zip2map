from zipcode_to_map.zipcode_to_map import ZipcodeToMap

result_map = ZipcodeToMap()

zipcodes = ['29582', '37920', '22448', '15422']

try:
	for zipcode in zipcodes:
		result_map.zipcode_to_map('us',zipcode)

except Exception as e:
	print("Not a valid pincode. Try with a valid one.")
