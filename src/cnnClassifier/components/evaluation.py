from cnnClassifier.entity.config_entity import EvaluationConfig
import tensorflow as tf
from pathlib import Path
from cnnClassifier.constants import *
from cnnClassifier.utils.common import save_json


class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    def _valid_generator(self):
        datagenerator_kwargs = dict(
            rescale=1./255,
            validation_split=0.30
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:2],  # cần lấy cả (height, width)
            batch_size=self.config.params_batch_size,
            interpolation='bilinear',
            class_mode='categorical',
            subset='validation',
            seed=42
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            **dataflow_kwargs
        )

        return valid_generator

    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)

    def evaluation(self):
        self.model = self.load_model(self.config.path_of_model)
        valid_generator = self._valid_generator()
        self.score = self.model.evaluate(valid_generator)

    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path=Path("scores.json"), data=scores)