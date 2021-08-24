### Required Packages 

pip install zipcode-to-map\
pip install folium\
pip install pgeocode

### Import the class

from zipcode_to_map import ZipcodeToMap

### Instantiate the object

result_map = ZipcodeToMap()

### usage: result_map.zipcode_to_map('country_code', 'zipcode')

result_map.zipcode_to_map('us','29582')

