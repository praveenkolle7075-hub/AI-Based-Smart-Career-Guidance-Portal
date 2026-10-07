import pandas as pd
import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# -----------------------------------------
# LOAD DATASET
# -----------------------------------------

data = pd.read_csv("career_dataset.csv")

print("Dataset loaded successfully!")
print("Total records:", len(data))


# -----------------------------------------
# FEATURES
# -----------------------------------------

features = [
    "math",
    "programming",
    "communication",
    "creativity",
    "analytical",
    "leadership"
]

X = data[features]

y = data["career"]


# -----------------------------------------
# ENCODE CAREER NAMES
# -----------------------------------------

encoder = LabelEncoder()

y_encoded = encoder.fit_transform(y)

print("\nCareer classes:")

for number, career in enumerate(encoder.classes_):
    print(number, "=", career)


# -----------------------------------------
# TRAIN / TEST SPLIT
# -----------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.30,
    random_state=42
)


# -----------------------------------------
# RANDOM FOREST MODEL
# -----------------------------------------

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

print("\nModel training completed!")


# -----------------------------------------
# TEST MODEL
# -----------------------------------------

prediction = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    prediction
)

print(
    "\nModel Accuracy: {:.2f}%".format(
        accuracy * 100
    )
)


# -----------------------------------------
# SAVE MODEL
# -----------------------------------------

model_data = {
    "model": model,
    "encoder": encoder,
    "features": features
}

with open(
    "career_model.pkl",
    "wb"
) as file:

    pickle.dump(
        model_data,
        file
    )


print("\nModel saved successfully!")

print(
    "Created: career_model.pkl"
)