import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
import joblib

df = pd.read_csv(r"C:\Users\shubh\krishi_mitra_ai\data\crop_data.csv")
df = df.dropna()

encoder = LabelEncoder()
df["crop_label"] = encoder.fit_transform(df["crop"])

features = ['N','P','K','temperature','humidity','rainfall']

X_crop = df[features]
y_crop = df['crop_label']
Xc_train, Xc_test, yc_train, yc_test = train_test_split(X_crop, y_crop, test_size=0.2, random_state=42)

crop_model = RandomForestClassifier(n_estimators=200, random_state=42)
crop_model.fit(Xc_train, yc_train)
print("Crop Model Accuracy:", accuracy_score(yc_test, crop_model.predict(Xc_test)))

joblib.dump(crop_model, r"C:\Users\shubh\krishi_mitra_ai\models\crop_recommendation_model.pkl")
joblib.dump(encoder, r"C:\Users\shubh\krishi_mitra_ai\models\crop_label_encoder.pkl")


X_yield = df[features]
y_yield = df['yield']
Xy_train, Xy_test, yy_train, yy_test = train_test_split(X_yield, y_yield, test_size=0.2, random_state=42)

yield_model = RandomForestRegressor(n_estimators=250, random_state=42)
yield_model.fit(Xy_train, yy_train)
print("Yield R2 Score:", r2_score(yy_test, yield_model.predict(Xy_test)))

joblib.dump(yield_model, r"C:\Users\shubh\krishi_mitra_ai\models\yield_prediction_model.pkl")


print("Models saved in ../models/")
