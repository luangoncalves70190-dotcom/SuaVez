# 🏥 SuaVez

**SuaVez** é uma plataforma acadêmica para gestão e acompanhamento de filas hospitalares. O sistema permite que pacientes encontrem unidades próximas, acompanhem a posição na fila, recebam estimativas de espera e alertas de aproximação, enquanto administradores visualizam indicadores operacionais em um painel de gestão.

> Projeto desenvolvido para a ExpoTech, integrando desenvolvimento web, banco de dados, Data Engineering, Data Science, Big Data e Cloud.

## Principais funcionalidades

### Paciente
- Cadastro e login unificado
- Hospitais próximos por geolocalização, em raio de até 10 km
- Especialidades e convênios
- Entrada e acompanhamento de fila
- Prioridade 60+ e sinalização de urgência
- Estimativa de espera em formato amigável
- Alertas quando faltam 5, 3 e 1 paciente, além do aviso de chegada da vez
- Ajuda SuaVez

### Administrador
- Dashboard de gestão
- Hospitais, usuários, filas e alertas
- Gráficos por hospital, especialidade e horário
- Indicadores de espera, abandono, prioridades e urgências
- Área de Dados e Inteligência

## Tecnologias

| Camada | Tecnologias |
|---|---|
| Frontend | React, TypeScript, Vite |
| Backend | NestJS, Node.js |
| Autenticação / Dados | Firebase Auth, Firestore |
| IA | Groq + LLaMA |
| Data Engineering | Python, Pandas |
| Data Science | Python, scikit-learn, Random Forest |
| Big Data | PySpark |
| Data Warehouse | MySQL, Star Schema |
| Cloud | Firebase, Google Cloud, Cloud Run, BigQuery |

## Estrutura

```text
SuaVez/
├── frontend/
├── backend/
├── data-engineering/
├── data-science/
├── big-data/
├── database/
├── warehouse/
├── cloud/
├── datasets/
├── docs/
└── .github/workflows/
```

## Execução

Frontend:

```bash
cd frontend
npm install
cp .env.example .env
npm run dev
```

Backend:

```bash
cd backend
npm install
cp .env.example .env
npm run start:dev
```

Frontend: `http://localhost:5173`  
API: `http://localhost:3001`

## Banco e Star Schema

- `database/suavez_operacional.sql`: banco relacional
- `database/suavez_star_schema.sql`: Data Warehouse em Star Schema

No MySQL Workbench, use **Database → Reverse Engineer** para gerar o diagrama EER.

## Pipeline ETL

```text
SuaVez
  ↓
Banco operacional
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

## Segurança

Não envie arquivos `.env`, chaves de API, arquivos de conta de serviço ou outras credenciais para o GitHub.

---

Projeto acadêmico — SuaVez.
