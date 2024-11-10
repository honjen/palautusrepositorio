import toml
from urllib import request
from project import Project

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        content = request.urlopen(self._url).read().decode("utf-8")
        new_content = toml.loads(content)

        name = new_content.get("tool", {}).get("poetry", {}).get("name", "Unknown")
        description = new_content.get("tool", {}).get("poetry", {}).get("description", "No description")
        license = new_content.get("tool", {}).get("poetry", {}).get("license")
        authors = new_content.get("tool", {}).get("poetry", {}).get("authors", [])
        dependencies = list(new_content.get("tool", {}).get("poetry", {}).get("dependencies", {}).keys())
        dev_dependencies = list(new_content.get("tool", {}).get("poetry", {}).get("group", {}).get("dev", {}).get("dependencies", {}).keys()) 

        return Project(name, description, dependencies, dev_dependencies, license, authors)