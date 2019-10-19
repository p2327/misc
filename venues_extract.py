def venues_extract(coords: List[Tuple[str, str]) -> List[str]:
    """
    Extract data from Foursquare API from a list of coordinates.
    Returns a list of addresses. If no hit, an exception message is printed.
    ----
    Example usage:

    >>> latlongs = [('51.5315955', '-0.104803')]
    >>> venues_list = venues_extract(latlongs)
    >>> df_venues = pd.DataFrame(venues_list)
    """
    output = []
    for j in range(len(coords)):
        
        url = 'https://api.foursquare.com/v2/venues/search?&client_id={}'\
        '&client_secret={}&v={}&ll={},{}&radius={}&limit={}'\
        '&categoryId={}'.format(
            CLIENT_ID, 
            CLIENT_SECRET, 
            VERSION, 
            cords[j][1], 
            cords[j][2], 
            radius, 
            limit,
            CATEGORY_ID)
        
        result = requests.get(url).json()
        
        try: 
            output.append([cords[j][0],
                           cords[j][1],
                           cords[j][2],
                           result['response']['venues'][0]['name'],
                           'Yes'])
            print(result['response']['venues'][0]['name'])
            
        except:
            output.append([cords[j][0],
                           cords[j][1],
                           cords[j][2],
                           'No result',
                           'No'])
            print(f'{cords[j][0]} has no venue')
            if result['response'] == {}:
                break
            print(result['response'])
        
    return output
