class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, license=None, authors=None):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license = license
        self.authors = authors or []

    def _stringify_dependencies(self, dependencies):
        return "\n- ".join(dependencies) if dependencies else "-"

    def __str__(self):
        authors_str = "\n- ".join(self.authors) if self.authors else "-"
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\n\nAuthors:\n- {authors_str}"
            f"\n\nDependencies:\n- {self._stringify_dependencies(self.dependencies)}"
            f"\n\nDevelopment dependencies:\n- {self._stringify_dependencies(self.dev_dependencies)}"
        )