from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        deserialized_toml = toml.loads(content)
        print(deserialized_toml)
        
        return Project(
            deserialized_toml['tool']['poetry']['name'],
            deserialized_toml['tool']['poetry']['description'],
            deserialized_toml['tool']['poetry']['dependencies'],
            deserialized_toml['tool']['poetry']['dev-dependencies']
        )
