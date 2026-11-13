from pathlib import Path
import csv, random
from datetime import datetime, timedelta

ROOT = Path(__file__).resolve().parents[1]
out = ROOT/'datasets/raw/atendimentos_1m.csv'
random.seed(2026)
hospitals=['Pronto Socorro e Maternidade Antena','Hospital Family','Hospital Geral de Pirajussara','UPA Dr. Akira Tada','Pronto Atendimento Infantil Taboão da Serra','AME Taboão da Serra']
specialties=['Clínica Geral','Pediatria','Cardiologia','Ortopedia']
start=datetime(2025,1,1)
N=1_000_000
with out.open('w',newline='',encoding='utf-8') as f:
    w=csv.writer(f)
    w.writerow(['id','hospital','especialidade','data','hora','fila','espera_min','abandonou'])
    for i in range(N):
        dt=start+timedelta(minutes=random.randint(0,900000))
        fila=random.randint(1,60)
        espera=max(3,int(fila*random.uniform(1.1,2.3)))
        w.writerow([i+1,random.choice(hospitals),random.choice(specialties),dt.date(),dt.hour,fila,espera,1 if espera>65 and random.random()<.25 else 0])
print(out)
