import pytest
from scripts.data_preprocessing import prepocess

@pytest.fixture
def sample_data():
    return {
        "PolicyID": [1, 2, 3],
        "TotalPremium": [100.0, 200.0, -50.0],
        "TotalClaims": [50.0, -20.0, 30.0]
    }

def test_handle_dataset(sample_data):
    # Create a dataframe from the sample data
    import pandas as pd
    df = pd.DataFrame(sample_data)

    # Process the data
    preprocessor = prepocess()
    processed_df = preprocessor.handle_dataset(df, "dummy_output.csv")

    # Check the processed data
    assert processed_df["TotalPremium"].min() >= 0, "Negative premiums not removed"
    assert processed_df["TotalClaims"].min() >= 0, "Negative claims not removed"
    assert "PolicyID" in processed_df.columns, "Essential columns are missing"
