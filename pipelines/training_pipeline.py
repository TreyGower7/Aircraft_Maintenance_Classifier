from zenml import pipeline
from steps.clean import clean_data
from steps.Ingest import Ingest
from steps.evaluate import evaluate_model
from steps.model_dev import train_model
#from steps.config import ModelNameConfig


@pipeline(enable_cache=True)
def training_pipeline(data_path: str):
    """
    froms data, cleans data, trains model, evaluates model performance
    
    Args:
        data_path: a string containing data path
        model_name: a string with the model we will train
    """
    df = Ingest(data_path)
    clean_data(df)
    train_model(df)
    evaluate_model()

    
    # TODO: X_train, X_test, Y_train, Y_test = clean_data(df)
    #  model_config = ModelNameConfig(model_name=model_name)
    # model = train_model(X_train, X_test, Y_train, Y_test, model_config)
    # r2_score, rmse = evaluate_model(model, X_test, Y_test)

