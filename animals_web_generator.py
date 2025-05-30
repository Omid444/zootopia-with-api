import requests
from bs4 import BeautifulSoup


API_KEY = '9TZ4CebQUwCg7QWDtNgDCQ==i4fRE9M3wprRsMzq'


def get_characteristics(animals_info):
    """Get animals characteristics and turn it to suitable text"""
    output =''
    for animal in animals_info:
        try:
            name = animal['name']
            diet = animal['characteristics']['diet']
            location = animal['locations']
            animal_type = animal['characteristics']['type']
            animal_object = (name, diet, location, animal_type)
            if all(animal_object):
                single_animal_info = serialize_animal(animal_object)
                output += single_animal_info
                print('output',output)
            else:
                continue
        except KeyError:
            continue
    return output


def serialize_animal(animal_obj):
    """This function support get_characteristics() to make suitable text"""
    name, diet, location, animal_type = animal_obj
    tag_start = '<li class="cards__item">'
    title = f'<div class="card__title">{name}</div>'
    paragraph = f"<p class=\"card__text\"><strong>Diet:</strong> {diet}<br/>"\
                f"<strong>Location:</strong> {location}<br/>"\
                f"<strong>Type:</strong> {animal_type}<br/></p>"
    tag_end = '</li>'
    final_text = tag_start + title + paragraph + tag_end
    return final_text


def read_html(file_path, animals_info):
    """Read html file and return needed content"""
    with open(file_path, "r") as html_file:
        index = html_file.read()
        soup = BeautifulSoup(index, 'html.parser')
        target = soup.find('ul', class_="cards")
        content_file = index.replace(target.text, animals_info)
        return content_file


def write_html(file_path, index):
    """Write text into html"""
    with open(file_path, "w") as html_file:
        html_file.write(index)


def main():
    animal_name = input('Enter a name of an animal:')
    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        animals_data = response.json()
        print(animals_data)
        animals = get_characteristics(animals_data)
        index = read_html('animals_template.html', animals)
        write_html('animals.html', index)
        print('Website was successfully generated to the file animals.html.')
    else:
        print("Error:", response.status_code, response.text)



if __name__ == "__main__":
    main()