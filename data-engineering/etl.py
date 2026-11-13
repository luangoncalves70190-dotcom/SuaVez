from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'datasets' / 'raw' / 'atendimentos_raw.csv'
target = ROOT / 'datasets' / 'processed' / 'atendimentos_processed.csv'

df = pd.read_csv(source)
print('Registros recebidos:', len(df))
print('Duplicados:', df.duplicated().sum())
print('Nulos:', int(df.isna().sum().sum()))

df = df.drop_duplicates().copy()
df['data_entrada'] = pd.to_datetime(df['data_entrada'], errors='coerce')
df = df.dropna(subset=['data_entrada','hospital','especialidade'])
df['dia_semana'] = df['data_entrada'].dt.day_name()
df['mes'] = df['data_entrada'].dt.month
df['tempo_total_min'] = df['tempo_espera_min'] + df['tempo_atendimento_min']
df['faixa_espera'] = pd.cut(df['tempo_espera_min'], bins=[-1,20,40,60,9999], labels=['Baixa','Moderada','Alta','Crítica'])
target.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(target, index=False)
print('Registros processados:', len(df))
print('Arquivo:', target)
