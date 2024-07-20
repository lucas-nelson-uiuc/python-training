import json
from pathlib import Path

from python_training.config import TrainingModel, TrainingConfig, FILEPATH_SETUP


def main():
    with open(FILEPATH_SETUP, "r") as fp:
        topics_repository = json.load(fp)

    for topic_json in topics_repository:
        training_model = TrainingModel(**topic_json)
        TrainingConfig(training_model).create_training()


if __name__ == "__main__":
    main()
