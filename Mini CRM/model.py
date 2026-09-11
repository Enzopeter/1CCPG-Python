from datetime import date

def model_lead(name, email, company, step="novo"): #estrutura um lead como um dicionário
    step = step or 'novo'

    return {
    "name": name,
    "email": email,
    "company": company,
    "step": step,
    "created": date.today().isoformat()
    }