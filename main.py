from redwine_ml import logger
from redwine_ml.pipeline.stage_01_pipeline import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

if __name__ == "__main__":
    try:
        logger.info(f"stage----{STAGE_NAME}-----started")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f"stage-------{STAGE_NAME}------completed")
    except Exception as e:
        logger.exception(e)
        raise e
