import pandas as pd
import random

cogDf = pd.read_csv("C:/Users/gaura/Documents/Submission/database/CogData_350.csv") #Change the path accordingly
cogList = list(cogDf['Text'])
NPDf = pd.read_csv("C:/Users/gaura/Documents/Submission/database/NPData.csv") #Change the path accordingly
NPList = list(NPDf['Text'])

NPListRand = random.sample(NPList, 500) #Change the number accordingly

df = pd.DataFrame(list(zip(NPListRand, ['No' for _ in range(len(NPListRand))])), columns =['Text', 'CogData'])
df2 = pd.DataFrame(list(zip(cogList, ['Yes' for _ in range(len(cogList))])), columns =['Text', 'CogData'])
df = df.append(df2, ignore_index=True)
df.to_csv("C:/Users/gaura/Documents/Submission/database/Test.csv", index=False)