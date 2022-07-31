from sklearn.metrics import mean_squared_error
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn import linear_model
import numpy as np
import pandas as pd
import sys
import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'sklearn'])
boston = load_boston()
print(boston)
df_x = pd.DataFrame(boston.data)
df_y = pd.DataFrame(boston.target)

df_x.describe()
reg = linear_model.LinearRegression()
x_train, x_test, y_train, y_test = train_test_split(
    df_x, df_y, test_size=0.33, random_state=42)
reg.fit(x_train, y_train)
print("Regular coefficient")
print(reg.coef_)
y_pred = reg.predict(x_test)
print("\n\n\nDependent values")
print(y_pred)

y_pred[2]
y_test[0]
print(np.mean((y_pred-y_test)**2))
print(mean_squared_error(y_test, y_pred))
