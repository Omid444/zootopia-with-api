import requests


API_KEY = '9TZ4CebQUwCg7QWDtNgDCQ==i4fRE9M3wprRsMzq'




def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    """
    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'

    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})

    animals_data = response.json()

    if response.status_code == requests.codes.ok:

        output = []

        for animal in animals_data:
            try:
                name = animal['name']
                taxonomy = animal['taxonomy']
                locations = animal['locations']
                characteristics = animal['characteristics']
                animal_object = (name, taxonomy, locations, characteristics)
                if all(animal_object):

                    output.append({'name':name, 'taxonomy':taxonomy, 'locations': locations, 'characteristics':characteristics})

                else:
                    continue
            except KeyError:
                continue
        return output
    else:
        print("Error:", response.status_code, response.text)






