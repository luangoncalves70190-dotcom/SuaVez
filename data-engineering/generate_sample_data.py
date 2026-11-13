from pathlib import Path
import csv, random
from datetime import datetime, timedelta

random.seed(42)
ROOT = Path(__file__).resolve().parents[1]
out = ROOT / 'datasets' / 'raw' / 'atendimentos_raw.csv'
out.parent.mkdir(parents=True, exist_ok=True)

hospitals = ['Pronto Socorro e Maternidade Antena','Hospital Family','Hospital Geral de Pirajussara','UPA Dr. Akira Tada','Pronto Atendimento Infantil Taboão da Serra','AME Taboão da Serra']
specialties = ['Clínica Geral','Pediatria','Cardiologia','Ortopedia']
channels = ['WEB','RECEPCAO']
start = datetime(2026,1,1,7,0)

with out.open('w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['id_entrada','hospital','especialidade','canal','data_entrada','hora_entrada','pessoas_na_fila','profissionais_ativos','tempo_medio_historico','prioridades_na_fila','tempo_espera_min','tempo_atendimento_min','abandonou','usou_ia'])
    for i in range(5000):
        dt = start + timedelta(minutes=random.randint(0, 250000))
        fila = random.randint(1,45)
        profissionais = random.randint(2,9)
        historico = random.randint(8,38)
        prioridades = random.randint(0,min(8,fila))
        wait = max(4, int((fila/profissionais)*4.5 + prioridades*2.7 + historico*.35 + random.gauss(0,5)))
        atendimento = max(4, int(random.gauss(16,5)))
        p_abandono = 0.02 if wait <= 30 else (0.18 if wait <= 45 else (0.48 if wait <= 60 else 0.72))
        abandonou = 1 if random.random() < p_abandono else 0
        w.writerow([f'ENT-{i+1:06d}', random.choice(hospitals), random.choice(specialties), random.choice(channels), dt.date().isoformat(), dt.hour, fila, profissionais, historico, prioridades, wait, atendimento, abandonou, 1 if random.random() < .31 else 0])
print(out)
