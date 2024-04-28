import requests
import urllib3

urllib3.disable_warnings()  # for remove warnings


class Swapi:
    """Work with Swapi API"""

    def __init__(self):
        self.file_name = "Darth_Vader_films.txt"
        self.file_name_2 = "All_characters.txt"
        self.base_url = "https://swapi.dev"  # base url
        self.get_resourse = "api/people"  # get resourse
        self.darth_vader = "4"  # darth vader id
        self.get_url = f"{self.base_url}/{self.get_resourse}/"  # get url

    def get_darth_vader(self):
        """Get all films with Darth Vader and save to txt"""

        get_url = self.get_url + self.darth_vader
        response = requests.get(get_url, verify=False)
        data = response.json()

        if 'films' in data:
            films = data['films']
            with open(self.file_name, 'a') as file:
                for film_url in films:
                    file.write(film_url + '\n')  # save films to txt
            print(f"All films saved in {self.file_name}")
        else:
            print("Error!")

    def get_names_from_txt(self):
        """Get n data"""

        with open(self.file_name, 'r') as file:  # read txt
            films = file.readlines()  # get list of films
            strip_urls = [film.strip() for film in films]  # delete all /n
            for film_url in strip_urls:
                get_urls = requests.get(film_url, verify=False)
                get_urls_json = get_urls.json()
                get_characters = get_urls_json.get('characters')  # get all characters in films
                for characters in get_characters:
                    get_names = requests.get(characters, verify=False)
                    get_names_json = get_names.json()
                    get_characters = get_names_json.get('name')  # get all names in all films
                    print(get_characters)
                    with open(self.file_name_2, 'a', encoding='utf-8') as file_2:  # save all names in empty txt file
                        file_2.write(get_characters + '\n')

    def remove_duplicates(self):
        """Remove duplicate values from the file"""

        with open(self.file_name_2, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        unique_lines = set(lines)  #
        with open(self.file_name_2, 'w', encoding='utf-8') as file:
            for line in unique_lines:  # check and remove duplicates
                file.write(line)

    # add some data

f = Swapi()
f.get_darth_vader()
f.get_names_from_txt()
f.remove_duplicates()
