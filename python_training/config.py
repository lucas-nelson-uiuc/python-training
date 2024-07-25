import re
import string
from pathlib import Path

from pydantic import BaseModel
from attrs import define

from jinja2 import Environment, FileSystemLoader


FILEPATH_CONFIG = Path("python_training/config")
FILEPATH_SETUP = FILEPATH_CONFIG.joinpath("config.json")

FILEPATH_TOPICS = Path("python_training/topics")
FILEPATH_EVALUATE = Path("python_training/evaluate")
FILEPATH_SOLUTIONS = Path("python_training/solutions")
FILEPATH_EXERCISES = Path("exercises")

FILEPATH_BASE_SCRIPT = FILEPATH_CONFIG.joinpath("base_script.py")
FILEPATH_README = FILEPATH_CONFIG.joinpath("README.md")


class TrainingModel(BaseModel):
    """Pydantic model representation of Training instance"""

    name: str
    description: str
    order: int
    topics: list[str]
    contents: dict[str, list[str]]


@define(slots=False)
class TrainingConfig:
    """Base training module.

    Training modules provide methods for detailing specific configurations
    for each topic as well as populating them in the Topics folder.

    TODO: include validations; ensure up to date so modules can be compiled
    """

    training_model: dict

    def normalize_filepath(self, filepath: str, str_case: str = "lower") -> str:
        """Construct compliant filepath (default: lower snakecase)"""
        invalid_chars = re.compile(f"[\s{string.punctuation}]+")
        return invalid_chars.sub("_", getattr(str, str_case)(filepath.strip()))

    def generate_filename(
        self, prefix: str, index: int, name: str, sep: str = "_", suffix: str = ".py"
    ) -> str:
        """Construct filename with specific pattern given parameters"""
        filename = sep.join([prefix, str(index).zfill(2), name])
        return f"{filename}{suffix}"

    def create_training(self) -> None:
        """Create default training folder"""
        self.directory_name = self.normalize_filepath(self.training_model.name)
        self.directory_path = FILEPATH_TOPICS.joinpath(self.directory_name)
        self.solutions_path = FILEPATH_SOLUTIONS.joinpath(self.directory_name)

        if not self.directory_path.is_dir():
            self.directory_path.mkdir(parents=True)

        self.create_readme()
        self.create_exercises(
            exercises_filepath=self.directory_path.joinpath(FILEPATH_EXERCISES)
        )
        self.create_exercises(exercises_filepath=self.solutions_path)
        self.create_solutions()

    def create_readme(self) -> None:
        """Write README contents to README file"""
        readme_page = {
            "header": self.training_model.name,
            "description": self.training_model.description,
            "topics": self.training_model.topics,
            "resources": self.training_model.contents.get("resources"),
        }
        jinja_env = Environment(loader=FileSystemLoader("python_training/config"))
        readme_template = jinja_env.get_template("README.md")
        readme_rendered = readme_template.render(readme_page)
        readme_filepath = self.directory_path.joinpath("README.md")
        readme_filepath.write_text(readme_rendered)

    def create_exercises(self, exercises_filepath: Path) -> None:
        """Iteratively pouplate Exercises folder with template exercise files"""

        if not exercises_filepath.is_dir():
            exercises_filepath.mkdir()

        base_exercise = FILEPATH_BASE_SCRIPT.read_text()
        for i, topic in enumerate(self.training_model.topics):
            topic_name = self.normalize_filepath(topic)
            fp_exercise = exercises_filepath.joinpath(
                self.generate_filename("topic", i, topic_name, suffix=".py")
            )
            if not fp_exercise.is_file():
                fp_exercise.touch()
                fp_exercise.write_text(base_exercise)

    def create_solutions(self) -> None:
        """Iteratively populate Solutions folder with template solution files"""
        solutions_filepath = FILEPATH_EVALUATE.joinpath(self.directory_name)
        topic_import_path = ".".join(
            map(
                str,
                [
                    "python_training",
                    FILEPATH_TOPICS.stem,
                    self.directory_path.stem,
                    FILEPATH_EXERCISES,
                ],
            )
        )

        if not solutions_filepath.is_dir():
            solutions_filepath.mkdir()

        jinja_env = Environment(loader=FileSystemLoader("python_training/config"))
        solution_template = jinja_env.get_template("base_solution.py")
        for i, topic in enumerate(self.training_model.topics):
            topic_name = self.normalize_filepath(topic)
            solution_rendered = solution_template.render(
                {
                    "topic_import_path": topic_import_path,
                    "topic_name": self.generate_filename(
                        "topic", i, topic_name, suffix=""
                    ),
                    # "topic_name": f"topic_{str(i).zfill(2)}_{topic_name}",
                }
            )
            fp_solution = solutions_filepath.joinpath(
                f"test_{str(i).zfill(2)}_{topic_name}.py"  # files must begin with test; requirement for pytest
            )
            if not fp_solution.is_file():
                fp_solution.write_text(solution_rendered)
