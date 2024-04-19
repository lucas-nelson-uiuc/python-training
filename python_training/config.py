import re
import json
from pathlib import Path

from attrs import field, define


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
        self.filepath_topics = Path("topics")
        self.filepath_config = Path("config")
        self.filepath_exercises = Path("exercises")
        self.filepath = re.sub("\s+", "_", self.name.strip().lower())
        self.directory = self.filepath_topics.joinpath(self.filepath)

    def update(self, config: dict[str, str]) -> None:
        """Update configuration given dictionary"""
        for item in config:
            setattr(self, item, config.get(item))

    def load_config(self, filepath_config: Path) -> None:
        """Load, pass configurations to be updated"""
        with filepath_config.open() as fc:
            config = json.load(fc)[0]
            self.update(config)

    def create_training(self) -> None:
        """Create default training folder"""

        if f"{self.filepath}.json" in map(
            lambda fp: fp.name, self.filepath_config.rglob("*.json")
        ):
            self.load_config(self.filepath_config.joinpath(f"{self.filepath}.json"))

        if not self.directory.is_dir():
            self.directory.mkdir(parents=True)

        self.create_readme()
        self.create_exercises()

    def create_readme(self) -> None:
        """Write README contents to README file"""
        readme_page = {
            "header": f"Python Training: {self.name}",
            "description": self.description,
            "topics": "\n".join(map(lambda x: f"- {x}", self.topics)),
            "exercises": "\n".join(
                map(lambda x: f"- {x}", self.contents.get("exercises"))
            ),
            "resources": "\n".join(
                map(lambda x: f"- {x}", self.contents.get("resources"))
            ),
        }

        readme_filepath = self.directory.joinpath("README.md")
        readme_filepath.write_text("\n".join(readme_page.values()))

    def create_exercises(self) -> None:
        """Iteratively pouplate Exercises folder with exercises"""
        exercises_filepath = self.directory.joinpath(self.filepath_exercises)
        if not exercises_filepath.is_dir():
            exercises_filepath.mkdir()
        for exercise in self.contents.get("exercises"):
            # files must begin with test; requirement for pytest
            fp_exercise = exercises_filepath.joinpath(f"test_{exercise}.py")
            if not fp_exercise.is_file():
                fp_exercise.touch()
