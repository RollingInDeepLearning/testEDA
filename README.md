0. Ensure you have Python 3.x and the necessary libraries installed. You can install them using pip:
```bash
   pip install pandas numpy catboost seaborn matplotlib
```
1.  Run Jupyter Notebook stroke-eda-prediction.ipynb
 
After executing all cells in the notebook, the following files will be saved:
- predictions_notebook.csv: Predictions made by the model on test data.
- test_features.csv: Test features (original, unprocessed).
- trained_catboost.joblib: The trained CatBoost model.

2. execute the following command in your terminal to get predictions:
```bash
    python main.py test_features.csv 
```
3. To verify that the prediction results are consistent, run the following command:
```bash
    diff predictions.csv predictions_notebook.csv
```