from pathlib import Path
import json, csv

DATA_DIR = Path(__file__).resolve().parent / 'data'
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / 'leads.json'

# CRUD ---> Create, Read, Update, Delete. Sigla principal de um banco de dados

#READ
def read_leads():
    if not DB_PATH.exists():
        return []

    try:
        return json.loads(DB_PATH.read_text(encoding='utf-8'))
    except json.JSONDecodeError:
        return []

#Create
def create_lead(lead_dict):
    leads = read_leads() #Lista de dicionários de leads
    leads.append(lead_dict)
    DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding='utf-8')

#Export leads como CSV
def export_csv(): #Exporta os leads para CSV e Retorna o caminho do arquivo criado
    path_csv = DATA_DIR / 'leads.cvs'

    leads = read_leads() #lista - array

    try:
        with path_csv.open('w', newline='',encoding='utf-8') as file_csv:
            write = csv.DictWriter(file_csv, fieldnames=leads[0].keys())
            write.writeheader()
            for row in leads:
                write.writerow(row)
        return path_csv
    except PermissionError:
        return None


#Read leads from query/search
def read_leads_search(query):
    leads = read_leads()
    results = []

    for i, lead in enumerate(leads):
        txt_lead = f'{lead['name']} {lead['email']} {lead['company']}'.lower()

        if query.lower() in txt_lead:
            results.append((i, lead))

    return results