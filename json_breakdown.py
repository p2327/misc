''' Code to use in python tutor to quickly indicise json payload for extracting data.
Usage
    Copy and paste in python tutor
    Edit json
    run the code
    
'''


def venues(cords):
    output = []
    for j in range(len(cords)):
              
        result = {'meta': {'code': 200, 'requestId': '5d84ce676adbf5002c058857'},
 'response': {'confident': True,
  'venues': [{'categories': [{'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/building/gym_',
       'suffix': '.png'},
      'id': '4bf58dd8d48988d175941735',
      'name': 'Gym / Fitness Center',
      'pluralName': 'Gyms or Fitness Centers',
      'primary': True,
      'shortName': 'Gym / Fitness'}],
    'hasPerk': False,
    'id': '4afff888f964a520623a22e3',
    'location': {'address': '333 Goswell Road',
     'cc': 'GB',
     'city': 'London',
     'country': 'United Kingdom',
     'distance': 36,
     'formattedAddress': ['333 Goswell Road',
      'London',
      'Greater London',
      'EC1V 7DG',
      'United Kingdom'],
     'labeledLatLngs': [{'label': 'display',
       'lat': 51.5313435,
       'lng': -0.1051354}],
     'lat': 51.5313435,
     'lng': -0.1051354,
     'postalCode': 'EC1V 7DG',
     'state': 'Greater London'},
    'name': 'Virgin Active',
    'referralId': 'v-1568984679'}]}}
             
        
        try: 
            output.append([cords[j][0],
                           cords[j][1],
                           cords[j][2],
                           result['response']['venues'][0]['name'],
                           'Yes'])
        except:
            output.append([cords[j][0],
                           cords[j][1],
                           cords[j][2],
                           'No result',
                           'No'])
            # print(f'{cords[j][0]} has no venue')
        
        outputA = output
        
    return outputA
    
latlongs = [['E1 0Ad', 51.51291, -0.055323000000000004],
['E1 0As', 51.511571999999994, -0.052685],
['E1 0Bw', 51.510758, -0.05676900000000001]]
 
ans = venues(latlongs)
