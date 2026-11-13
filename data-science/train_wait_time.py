from pathlib import Path
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
import joblib

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT/'datasets/processed/atendimentos_processed.csv')
features = ['hospital','especialidade','canal','hora_entrada','pessoas_na_fila','profissionais_ativos','tempo_medio_historico','prioridades_na_fila']
X, y = df[features], df['tempo_espera_min']
cat = ['hospital','especialidade','canal']
num = [c for c in features if c not in cat]
prep = ColumnTransformer([('cat', OneHotEncoder(handle_unknown='ignore'), cat), ('num','passthrough',num)])
model = Pipeline([('prep',prep),('model',RandomForestRegressor(n_estimators=90,random_state=42,min_samples_leaf=2))])
Xtr,Xte,ytr,yte = train_test_split(X,y,test_size=.2,random_state=42)
model.fit(Xtr,ytr)
pred = model.predict(Xte)
print('MAE:', round(mean_absolute_error(yte,pred),2),'min')
print('R2:', round(r2_score(yte,pred),3))
out = ROOT/'data-science/wait_time_model.joblib'
joblib.dump(model,out)
print('Modelo salvo em:',out)
