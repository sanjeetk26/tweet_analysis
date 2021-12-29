# Twitter Analysis


For generating data consisting of cogData and random NP data points. Make changes in data.py accordingly and run: 
``` 
python code/data.py 
```

The experimentations with RobertaForSequenceClassification can be found in Twitter_Classification.ipynb. The notebook contains code for training and data augmentation. Run the code cells as mentioned in the notebook.

'database' folder consists of the data used for training. It consists of 4 CSV files:

1. CogData_350.csv: Old Cog Data containing 350 Cog data points.
2. CogData_840.csv: New Cog Data containing 840 Cog data points.
3. Data_New.csv: Contains New Cog Data with 180,000 NP data points. Used for Data Augmentation.
4. NPData.csv: NP Data containing 180,000 NP data points.