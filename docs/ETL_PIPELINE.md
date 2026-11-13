# Pipeline ETL do SuaVez

```text
SuaVez
  ↓
Dados operacionais
  ↓
usuarios / hospitais / filas / entradas_fila / atendimentos
  ↓
Extração
  ↓
Python + Pandas
  ↓
Tratamento e padronização
  ↓
Data Warehouse / Star Schema
  ↓
Data Science + Big Data
  ↓
Dashboard administrativo
```

## Transformações
- padronização de datas e horários;
- tratamento de valores ausentes;
- cálculo do tempo de espera;
- organização por hospital e especialidade;
- classificação dos status;
- prioridade 60+;
- urgência sinalizada;
- indicadores de abandono e conclusão.
