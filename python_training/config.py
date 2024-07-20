import re
from pathlib import Path

from pydantic import BaseModel
from attrs import define

from jinja2 import Environment, FileSystemLoader


FILEPATH_EXERCISES = Path("exercises")
FILEPATH_SOLUTIONS = Path("solutions")
FILEPATH_TOPICS = Path("topics")
FILEPATH_CONFIG = Path("config")
FILEPATH_BASE_SCRIPT = Path("config/base_script.py")
FILEPATH_README = Path("config/README.md")


class TrainingModel(BaseModel):
    """Pydantic model representation of Training instance"""

    name: str
    description: str
    order: int
    topics: list[str]
    contents: dict[str, list[str]]


from attrs import define
import re


@define(slots=False)
class Training:
    """Base training module.

    Training modules provide methods for detailing specific configurations
    for each topic as well as populating them in the Topics folder.

    TODO: include validations; ensure up to date so modules can be compiled
    """

    training_model: dict

    def create_training(self) -> None:
        """Create default training folder"""

        self.directory_name = re.sub(
            "\s+", "_", self.training_model.name.strip().lower()
        )
        # directory_index = str(self.training_model.order - 1).zfill(2)
        self.directory_path = FILEPATH_TOPICS.joinpath(self.directory_name)

        if not self.directory_path.is_dir():
            self.directory_path.mkdir(parents=True)

        self.create_readme()
        self.create_exercises()
        self.create_solutions()

    def create_readme(self) -> None:
        """Write README contents to README file"""
        readme_page = {
            "header": self.training_model.name,
            "description": self.training_model.description,
            "topics": self.training_model.topics,
            "resources": self.training_model.contents.get("resources"),
        }

        jinja_env = Environment(loader=FileSystemLoader("config"))
        readme_template = jinja_env.get_template("README.md")
        readme_rendered = readme_template.render(readme_page)

        readme_filepath = self.directory_path.joinpath("README.md")
        readme_filepath.write_text(readme_rendered)

    def create_solutions(self) -> None:
        solutions_filepath = FILEPATH_SOLUTIONS.joinpath(self.directory_name)
        # python_training.topics.automation_projects.exercises.topic_00_files
        topic_import_path = ".".join(
            map(
                str,
                [
                    "python_training",
                    FILEPATH_TOPICS,
                    self.directory_path.stem,
                    FILEPATH_EXERCISES,
                ],
            )
        )

        if not solutions_filepath.is_dir():
            solutions_filepath.mkdir()

        jinja_env = Environment(loader=FileSystemLoader("config"))
        solution_template = jinja_env.get_template("base_solution.py")
        for i, topic in enumerate(self.training_model.topics):
            import string
            topic_name = re.sub(f"[\s{string.punctuation}]+", "_", topic.strip().lower())
            solution_rendered = solution_template.render(
                {
                    "topic_import_path": topic_import_path,
                    "topic_name": f"topic_{str(i).zfill(2)}_{topic_name}",
                }
            )
            fp_solution = solutions_filepath.joinpath(
                f"test_{str(i).zfill(2)}_{topic_name}.py"  # files must begin with test; requirement for pytest
            )
            if not fp_solution.is_file():
                fp_solution.write_text(solution_rendered)

    def create_exercises(self) -> None:
        """Iteratively pouplate Exercises folder with exercises"""
        exercises_filepath = self.directory_path.joinpath(FILEPATH_EXERCISES)

        if not exercises_filepath.is_dir():
            exercises_filepath.mkdir()

        base_exercise = FILEPATH_BASE_SCRIPT.read_text()
        for i, topic in enumerate(self.training_model.topics):
            import string
            topic_name = re.sub(f"[\s{string.punctuation}]+", "_", topic.strip().lower())
            fp_exercise = exercises_filepath.joinpath(
                f"topic_{str(i).zfill(2)}_{topic_name}.py"
            )
            if not fp_exercise.is_file():
                fp_exercise.touch()
                fp_exercise.write_text(base_exercise)
