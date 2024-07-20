import json
from pathlib import Path

from python_training.config import Training, TrainingModel


def main():
    with open(Path("python_training/config/topics.json"), "r") as fp:
        topics_repository = json.load(fp)

    for topic_json in topics_repository:
        training_model = TrainingModel(**topic_json)
        Training(training_model).create_training()


if __name__ == "__main__":
    main()
