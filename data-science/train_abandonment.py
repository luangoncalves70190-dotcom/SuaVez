from pathlib import Path
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT/'datasets/processed/atendimentos_processed.csv')
features = ['hospital','especialidade','canal','hora_entrada','pessoas_na_fila','profissionais_ativos','tempo_medio_historico','prioridades_na_fila']
X, y = df[features], df['abandonou']
cat = ['hospital','especialidade','canal']
num = [c for c in features if c not in cat]
prep = ColumnTransformer([('cat',OneHotEncoder(handle_unknown='ignore'),cat),('num','passthrough',num)])
model = Pipeline([('prep',prep),('model',RandomForestClassifier(n_estimators=180,random_state=42,class_weight='balanced'))])
Xtr,Xte,ytr,yte = train_test_split(X,y,test_size=.2,random_state=42,stratify=y)
model.fit(Xtr,ytr)
proba = model.predict_proba(Xte)[:,1]
pred = (proba >= 0.35).astype(int)
print('Limiar de decisão: 0.35')
print(classification_report(yte,pred,digits=3))
