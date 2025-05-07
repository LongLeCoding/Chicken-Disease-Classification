from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.evaluation import Evaluation
from cnnClassifier import logger
import tensorflow as tf
STAGE_NAME = "Evaluation"


tf.config.run_functions_eagerly(False)#True in debug phase and False in Training Phase
class EvaluationPipeline:
    def __init__(self):
        pass
        
    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()


if __name__ == '__main__':
    try:
        logger.info(f"****************")
        logger.info(f">>>>>>>>stage {STAGE_NAME} started<<<<<<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<< \n\n x================x")
    except Exception as e:
        logger.exception(e)
        raise e