import re
import json
from pathlib import Path

from attrs import field, define

from jinja2 import Environment, FileSystemLoader


FILEPATH_BASE_SCRIPT = Path("config/base_script.py")
FILEPATH_README = Path("config/README.md")
FILEPATH_EXERCISES = Path("exercises")
FILEPATH_CONFIG = Path("config")
FILEPATH_TOPICS = Path("topics")


@define(slots=False)
class Training:
    """Base training module.

    Training modules provide methods for detailing specific configurations
    for each topic as well as populating them in the Topics folder.

    TODO: include validations; ensure up to date so modules can be compiled
    """

    name: str
    description: str = field(factory=str)
    topics: list[str] = field(factory=list)
    contents: dict[str, str] = field(factory=dict)

    def __attrs_post_init__(self):
        """Define constants, relevent paths for training module"""
        self.filepath = re.sub("\s+", "_", self.name.strip().lower())
        self.directory = FILEPATH_TOPICS.joinpath(self.filepath)

    def update(self, config: dict[str, str]) -> None:
        """Update configuration given dictionary"""
        for item in config:
            setattr(self, item, config.get(item))

    def load_config(self, filepath_config: Path = FILEPATH_CONFIG) -> None:
        """Load, pass configurations to be updated"""
        with filepath_config.open() as fc:
            config = json.load(fc)[0]
            self.update(config)

    def create_training(self) -> None:
        """Create default training folder"""

        if f"{self.filepath}.json" in map(
            lambda fp: fp.name, FILEPATH_CONFIG.rglob("*.json")
        ):
            self.load_config(FILEPATH_CONFIG.joinpath(f"{self.filepath}.json"))

        if not self.directory.is_dir():
            self.directory.mkdir(parents=True)

        self.create_readme()
        self.create_exercises()

    def create_readme(self) -> None:
        """Write README contents to README file"""
        readme_page = {
            "header": self.name,
            "description": self.description,
            "topics": self.topics,
            "resources": self.contents.get("resources"),
        }

        jinja_env = Environment(loader=FileSystemLoader("config"))
        readme_template = jinja_env.get_template("README.md")
        readme_rendered = readme_template.render(readme_page)

        readme_filepath = self.directory.joinpath("README.md")
        readme_filepath.write_text(readme_rendered)

    def create_exercises(self) -> None:
        """Iteratively pouplate Exercises folder with exercises"""
        exercises_filepath = self.directory.joinpath(FILEPATH_EXERCISES)
        if not exercises_filepath.is_dir():
            exercises_filepath.mkdir()

        base_script = FILEPATH_BASE_SCRIPT.read_text()
        for exercise in self.contents.get("exercises"):
            # files must begin with test; requirement for pytest
            fp_exercise = exercises_filepath.joinpath(
                f"test_{self.filepath}_{exercise}.py"
            )
            if not fp_exercise.is_file():
                fp_exercise.touch()
                fp_exercise.write_text(base_script)
