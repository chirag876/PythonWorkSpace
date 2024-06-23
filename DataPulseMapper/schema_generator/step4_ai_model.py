import time
from logzero import logger

class AiModel:
    def __init__(self) -> None:
        pass

    def step4_process_ai_models(self):
      start_time = time.time()
      try:
        model_score = 0
        end_time = time.time()
        logger.info(f"Time taken for step4_process_ai_models: {end_time - start_time} seconds")
        return model_score
      except Exception as e:
          end_time = time.time()
          logger.info(f"Error in step4_process_ai_models: {e}")
          logger.info(f"Time taken for step4_process_ai_models: {end_time - start_time} seconds")
          return {}, {}