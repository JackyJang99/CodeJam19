import pandas as pd
import numpy as np
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle
import os.path
from os import path
import time

# constants
filename = 'finalized_rf.sav'

# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))

while not (path.exists("user_apps_statistics.csv") and path.exists("user_table.csv")):
    time.sleep(5)

apps = pd.read_csv('user_apps_statistics.csv', index_col = 'user_id')
try: purch = pd.read_csv('user_purchase_events.csv', index_col = 'user_id')
except: pass
user = pd.read_csv('user_table.csv', index_col = 'user_id')

try:
    apps.drop('Unnamed: 0', axis=1, inplace=True)
    print(apps.columns.values)
except: pass
try:
    purch.drop('Unnamed: 0', axis=1, inplace=True)
except: pass
try:
    user.drop('Unnamed: 0', axis=1, inplace=True)
except: pass

# modified purch table
try :
    # purch.amount_spend.replace({'casual': 3, 'rookie': 1, 'player': 5, 'whale': 10}, inplace=True)
    purch.amount_spend.replace({'casual': 1, 'rookie': 1, 'player': 1, 'whale': 1}, inplace=True)
    purch.drop('date', axis=1, inplace=True)
    # purch = pd.DataFrame(purch.groupby('user_id')['amount_spend'].sum())
    purch = pd.DataFrame(purch.groupby('user_id')['amount_spend'].count()).assign(amount_spend=1)
except: pass

try:
    mer = apps.loc[:,['n_topGrossingApps', 'nTotal_Apps', 'n_shoppingApps','user_id']].join(purch.loc[:,['amount_spend','user_id']],on = 'user_id')
except:
    mer = apps.loc[:,['n_topGrossingApps', 'nTotal_Apps', 'n_shoppingApps','user_id']]

df = user.join(mer,on='user_id')
df.drop('ref',axis=1, inplace=True)

# filling empty slots
try :df.amount_spend.fillna(0, inplace=True)
except: pass
df.bin_age.fillna(4, inplace=True)
df.gender.fillna(0.5, inplace=True)
df.source_id.fillna('_0.5', inplace=True)
df.country_id.fillna('_0.5', inplace=True)
df.os_version.fillna('8.', inplace=True)
df.n_topGrossingApps.fillna('4.55',inplace=True)
df.nTotal_Apps.fillna('95.14',inplace=True)
df.n_shoppingApps.fillna('5.05',inplace=True)

df.bin_age.replace({'(13.0, 18.0]': 1, '(18.0, 22.0]': 2, '(22.0, 25.0]': 3,\
                    '(25.0, 30.0]': 4,'(30.0, 35.0]':5,'(35.0, 40.0]':6,\
                        '(40.0, 45.0]':7,'(45.0, 55.0]':8,'(55.0, 65.0]':9,'(65.0, 200.0]':10}, inplace=True)


# parsing string
df['c_id'] = df['country_id'].apply(lambda x: x.split('_')[1])
df['os_v'] = df['os_version'].apply(lambda x: x.split('.')[0])
df['s_id'] = df['source_id'].apply(lambda x: x.split('_')[1])

cols = ['n_topGrossingApps', 'nTotal_Apps', 'n_shoppingApps','bin_age','c_id','os_v','gender']
df_X = df[cols]
try: df_Y = df['amount_spend']
except: pass
    
X = df_X.reset_index(drop=True).to_numpy()
try: Y = df_Y.reset_index(drop=True).to_numpy()
except: pass


pred=loaded_model.predict(X)
binary = np.round(pred)

try:
    Y_Valid = [float(i) for i in Y]

    from sklearn.metrics import confusion_matrix,classification_report, f1_score
    report = classification_report(Y_Valid, binary, output_dict=True)
    pd.DataFrame(binary).to_csv('test_res')
    pd.DataFrame(confusion_matrix(Y_Valid,binary)).to_csv('confusion_matrix.csv')
    pd.DataFrame(report).T.to_csv('classfication_report.csv')
except: pass

output = pd.DataFrame()
output['predicted'] = binary
output.to_csv('predicted.csv')
print("\n\ntask complete\n\n")