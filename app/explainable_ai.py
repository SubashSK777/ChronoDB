import shap
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import pandas as pd

def train_explainer(df, target_col):
    # Separate features and target variable
    X = df.drop(target_col, axis=1)
    y = df[target_col]
    
    # Encode categorical columns in X (features) to numeric using Label Encoding
    categorical_cols = X.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        encoder = LabelEncoder()
        X[col] = encoder.fit_transform(X[col].astype(str))  # Convert categorical strings to numeric
    
    # If the target column (y) is categorical, encode it as well
    if y.dtype == 'object':
        encoder = LabelEncoder()
        y = encoder.fit_transform(y.astype(str))  # Convert categorical target to numeric
    
    # Fit a RandomForest model on the encoded data
    model = RandomForestRegressor()
    model.fit(X, y)
    
    # Create a SHAP explainer and calculate SHAP values
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X)
    
    return shap_values, model
