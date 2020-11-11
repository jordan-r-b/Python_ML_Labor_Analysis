import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')




hours = pd.read_csv("Data3.csv")




hours["Month"] = hours["APPLYDATE"].apply(lambda x: x[0:1])
hours["Year"] = hours["APPLYDATE"].apply(lambda x: x[-4:])
hours["MY"] = hours["Month"] + "/" + hours["Year"]




hours = hours.drop(['LOCATION'], axis=1)




hours = hours.drop(['APPLYDATE'], axis=1)




hours = hours.drop(['MY'], axis=1)




hours = hours.drop(['Month'], axis=1)




hours.groupby(["WY"])




hours.head()




sns.jointplot(x='Hours', y='WY', data=hours)




pivot_hours = pd.pivot_table(hours,index=["PAYCODENAME","Department"], values=["Hours"], 
columns = ["WY"], aggfunc=[np.sum],fill_value=0,margins=True)




pivot_hours




#kal = pivot_hours.query('LOCATION == ["US_KALAMAZOO_KAL"]')




kal = pivot_hours




kal = kal.T




kal




#kal = kal.droplevel([0,1], axis=0)
kal=kal.droplevel([0], axis=1)




kal = kal.droplevel([0,1], axis=0)




kal




sns.jointplot(x='Global-CP-Vacation', y='Global-CP-Overtime', data=kal)




kal = kal.reset_index()




y = kal['Global-CP-Overtime']
X = kal['Globa-CP-Vacation']




y = np.array(y)




y = y.reshape(-1,1)




X = np.array(X)




X = X.reshape(-1,1)




from sklearn.model_selection import train_test_split




X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)




from sklearn.linear_model import LinearRegression




lm = LinearRegression()




lm.fit(X_train,y_train)




# The coefficients
print('Coefficients: \n', lm.coef_)




predictions = lm.predict( X_test)




plt.scatter(y_test,predictions)
plt.xlabel('Y Test')
plt.ylabel('Predicted Y')




# calculate these metrics by hand!
from sklearn import metrics

print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))




coeffecients = pd.DataFrame(lm.coef_,X.columns)
coeffecients.columns = ['Coeffecient']
coeffecients






