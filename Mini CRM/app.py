from model import model_lead
import control

def add_lead():
    name = input("Nome: ")
    email = input('E-mail: ')
    company = input('Empresa: ')
    step = input('Etapa de vendas: ')

    if not name or not email or not company or '@' not in email:
        print('Nome ou e-mail inválido')
        return

    # validar as entradas do usuário
    # depois de validar vamos modelar os dados

    print(model_lead(name, email, company, step))

    # depois de modelado... vamos enviar esse dict (leads) para o leads.json
    # para salvar, vamos uasr o módulo control

    control.create_lead(model_lead(name, email, company, step))

    print('lead adicionado (func)')

def list_leads():
    leads = control.read_leads()
    if not leads:
        print("Nenhum lead ainda")
        return

    print("## | {:<15} | {:<20} | Empresa".format("nome", "E-mail"))
    for i, lead in enumerate(leads):
        print(f'{i:02d} | {lead["name"]:<15} | {lead["email"]:<20} | {lead["company"]}')

def search_leads():
    query = input('Buscar por: ').strip().lower()
    if not query:
        print('Consulta vazia')
        return

    #Envia a query para o control realizar a busca no leads.json
    leads_finded = control.read_leads_search(query)

    print("## | {:<15} | {:<20} | Empresa".format("nome", "E-mail"))
    for i, lead in leads_finded:
        print(f'{i:02d} | {lead["name"]:<15} | {lead["email"]:<20} | {lead["company"]}')

def export_leads():
    path_csv = control.export_csv()

    if path_csv is None:
        print("Não foi possivel exporta os leads")
    else:
        print(f'Exportado para {path_csv}')

def atualizar_lead():
    list_leads()

    indice = input("Digite o número do lead que deseja atualizar: ")

    if not indice.isdigit():
        print("Número inválido")
        return

    indice = int(indice)

    if control.update_lead(indice):
        print("Lead atualizado com sucesso!")
    else:
        print("Lead não encontrado")

def excluir_lead():
    list_leads()

    indice = input("Digite o número do lead que deseja excluir: ")

    if not indice.isdigit():
        print("Número inválido")
        return

    indice = int(indice) - 1

    leads = control.read_leads()

    lead = leads[indice]

    confirmacao = input(f"Tem certeza que deseja excluir {lead['name']}? (s/n): ").lower()

    if confirmacao != "s":
        print("Exclusão cancelada")
        return

    if control.delete_lead(indice):
        print("Lead excluído com sucesso!")
    else:
        print("Lead não encontrado")

def main():
    while True:
        print('\nMini CRM de leads')
        print('[1] Adicionar lead')
        print('[2] Listar leads')
        print('[3] Buscar (nome/e-mail/empresa)')
        print('[4] Exporta CSV')
        print('[5] Atualizar um lead')
        print('[6] Excluir lead')
        print('[0] Sair do programa')

        opt = input('Escolha uma opção: ')

        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "3":
            search_leads()
        elif opt == "4":
            export_leads()
        elif opt == '5':
            atualizar_lead()
        elif opt == '6':
            excluir_lead()
        elif opt == "0":
            print('Até mais...')
            break
        else:
            print('Opcao inválida')

if __name__ == '__main__':
    main()