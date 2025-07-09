import logging
import pandas as pd
from zenml import step
from typing_extensions import Annotated
from typing import Tuple

@step
def clean_data(df: pd.DataFrame) -> None:
# Tuple[
#     Annotated[pd.DataFrame: "X_test"],
#     Annotated[pd.DataFrame: "X_train"],
#     Annotated[pd.DataFrame: "y_test"],
#     Annotated[pd.DataFrame: "y_train"],
# ]:
    pass