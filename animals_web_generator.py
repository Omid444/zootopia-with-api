import data_fetcher
from bs4 import BeautifulSoup



def serialize_animal(animals_list):
    """This function support dict from data fetcher to make suitable text"""
    final_text = ''
    for animal in animals_list:
        tag_start = '<li class="cards__item">'
        title = f'<div class="card__title">{animal['name']}</div>'
        paragraph = f"<p class=\"card__text\"><strong>taxonomy:</strong> {animal['name']}<br/>"\
                    f"<strong>Location:</strong> {animal['locations']}<br/>"\
                    f"<strong>characteristics:</strong> {animal['characteristics']}<br/></p>"
        tag_end = '</li>'
        text = tag_start + title + paragraph + tag_end
        final_text += text
    return final_text


def read_html(file_path, animals_info):
    """Read html file and return needed content"""
    with open(file_path, "r", encoding="utf-8") as html_file:
        index = html_file.read()
        soup = BeautifulSoup(index, 'html.parser')
        target = soup.find('ul', class_="cards")
        content_file = index.replace(target.text, animals_info)
        return content_file


def write_html(file_path, index):
    """Write text into html"""
    with open(file_path, "w", encoding="utf-8") as html_file:
        html_file.write(index)


def main():

    animal_name = input('Enter a name of an animal:')

    data = data_fetcher.fetch_data(animal_name)

    if data:
        animals_info = serialize_animal(data)
        index = read_html('animals_template.html', animals_info)
        write_html('animals.html', index)
        print('Website was successfully generated to the file animals.html.')
    else:
        print(f'The animal {animal_name} does not exist')
        header = f"<h2 style='font-family: sans-serif;'>The animal {animal_name} doesn't exist.</h2>"
        index = read_html('animals_template.html', header)
        write_html('animals.html', index )


if __name__ == "__main__":
    main()