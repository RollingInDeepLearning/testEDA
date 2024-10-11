import joblib
import pandas as pd
import sys

THRESHOLD = 0.4

def main(features_file):

    model = joblib.load('trained_catboost.joblib')

    # upload test file
    features = pd.read_csv(features_file)


    probabilities = model.predict_proba(features)[:, 1]

    predictions = (probabilities > THRESHOLD).astype(int)

    results = pd.DataFrame({'Predicted': predictions})
    print()

    results.to_csv('predictions.csv', index=False)

if __name__ == "__main__":
    if len(sys.argv) != 2:  
        print("Usage: python load_and_predict.py <features_file> ")
        sys.exit(1)

    features_file = sys.argv[1]
    main(features_file)