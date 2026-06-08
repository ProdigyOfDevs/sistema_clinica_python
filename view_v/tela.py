class TelaApp:
    def __init__(self):
        self.__nada = None

    def inicializacao(self) -> int:
        print("\n" + "="*45)
        print("      SISTEMA DE GERENCIAMENTO CLÍNICO")
        print("="*45)
        print("1) Gerenciar Pacientes")
        print("2) Gerenciar Clínicas")
        print("3) Gerenciar Profissionais")
        print("4) Gerenciar Tipos de Atendimento")
        print("5) Gerenciar Atendimentos e Relatórios")
        print("0) Sair do Sistema")
        print("="*45)
        try:
            opcao = int(input("Escolha uma opção: "))
            return opcao
        except ValueError:
            return -1

    def entrando_clinica(self) -> int:
        print("\n" + "-"*40)
        print("         MENU DE CLÍNICAS")
        print("-"*40)
        print("1) Cadastrar nova clínica")
        print("2) Listar clínicas cadastradas")
        print("3) Alterar clínica cadastrada")
        print("4) Remover clínica cadastrada")
        print("5) Retornar ao menu anterior")
        print("-"*40)
        try:
            opcao = int(input("Escolha uma opção: "))
            return opcao
        except ValueError:
            return -1

    def entrando_paciente(self) -> int:
        print("\n" + "-"*40)
        print("         MENU DE PACIENTES")
        print("-"*40)
        print("1) Cadastrar novo paciente")
        print("2) Listar pacientes cadastrados")
        print("3) Alterar paciente cadastrado")
        print("4) Remover paciente cadastrado")
        print("5) Retornar ao menu anterior")
        print("-"*40)
        try:
            opcao = int(input("Escolha uma opção: "))
            return opcao
        except ValueError:
            return -1

    def entrando_profissional(self) -> int:
        print("\n" + "-"*40)
        print("         MENU DE PROFISSIONAIS")
        print("-"*40)
        print("1) Cadastrar novo profissional")
        print("2) Listar profissionais cadastrados")
        print("3) Alterar profissional cadastrado")
        print("4) Remover profissional cadastrado")
        print("5) Retornar ao menu anterior")
        print("-"*40)
        try:
            opcao = int(input("Escolha uma opção: "))
            return opcao
        except ValueError:
            return -1

    def entrando_tipo_atendimento(self) -> int:
        print("\n" + "-"*40)
        print("     MENU DE TIPOS DE ATENDIMENTO")
        print("-"*40)
        print("1) Cadastrar novo tipo de atendimento")
        print("2) Listar tipos de atendimento")
        print("3) Alterar tipo de atendimento")
        print("4) Remover tipo de atendimento")
        print("5) Retornar ao menu anterior")
        print("-"*40)
        try:
            opcao = int(input("Escolha uma opção: "))
            return opcao
        except ValueError:
            return -1

    def entrando_atendimento(self) -> int:
        print("\n" + "-"*40)
        print("         MENU DE ATENDIMENTOS")
        print("-"*40)
        print("1) Agendar novo atendimento")
        print("2) Listar atendimentos agendados")
        print("3) Adicionar procedimento a um atendimento")
        print("4) Registrar pagamento de um atendimento")
        print("5) Cancelar/Excluir um atendimento")
        print("6) Emitir relatórios consolidados")
        print("7) Retornar ao menu anterior")
        print("-"*40)
        try:
            opcao = int(input("Escolha uma opção: "))
            return opcao
        except ValueError:
            return -1

    def mostra_mensagem(self, mensagem: str):
        print(f"\n[INFO] {mensagem}")

    def pegar_dados_clinica(self, alteracao=False) -> dict:
        if alteracao:
            print("\n--- Alterando Clínica ---")
        else:
            print("\n--- Cadastro de Nova Clínica ---")
        
        try:
            nome = input("Nome da Clínica: ").strip()
            if not nome:
                raise ValueError("O nome não pode ser vazio.")
            
            cidade = input("Cidade: ").strip()
            if not cidade:
                raise ValueError("A cidade não pode ser vazia.")
                
            descricao = input("Descrição/Especialidade: ").strip()
            if not descricao:
                raise ValueError("A descrição não pode ser vazia.")
            
            print("\nHorário de Funcionamento:")
            hora_abertura = int(input("Hora de abertura (0-23): "))
            if not (0 <= hora_abertura <= 23):
                raise ValueError("Hora de abertura deve ser entre 0 e 23.")
                
            minuto_abertura = int(input("Minuto de abertura (0-59): "))
            if not (0 <= minuto_abertura <= 59):
                raise ValueError("Minuto de abertura deve ser entre 0 e 59.")
                
            hora_fechamento = int(input("Hora de fechamento (0-23): "))
            if not (0 <= hora_fechamento <= 23):
                raise ValueError("Hora de fechamento deve ser entre 0 e 23.")
                
            minuto_fechamento = int(input("Minuto de fechamento (0-59): "))
            if not (0 <= minuto_fechamento <= 59):
                raise ValueError("Minuto de fechamento deve ser entre 0 e 59.")
            
            return {
                "nome": nome,
                "cidade": cidade,
                "descricao": descricao,
                "hora_abertura": hora_abertura,
                "minuto_abertura": minuto_abertura,
                "hora_fechamento": hora_fechamento,
                "minuto_fechamento": minuto_fechamento
            }
        except ValueError as e:
            self.mostra_mensagem(f"Entrada inválida: {e}")
            return None

    def pegar_dados_paciente(self, alteracao=False) -> dict:
        if alteracao:
            print("\n--- Alterando Paciente ---")
        else:
            print("\n--- Cadastro de Novo Paciente ---")
        
        try:
            nome = input("Nome do Paciente: ").strip()
            if not nome:
                raise ValueError("O nome não pode ser vazio.")
            
            celular = input("Celular: ").strip()
            if not celular:
                raise ValueError("O celular não pode ser vazio.")
            
            cpf = ""
            if not alteracao:
                cpf = input("CPF: ").strip()
                if not cpf:
                    raise ValueError("O CPF não pode ser vazio.")
            
            print("\nData de Nascimento:")
            ano = int(input("Ano (ex: 1995): "))
            if ano < 1900 or ano > 2026:
                raise ValueError("Ano de nascimento inválido.")
                
            mes = int(input("Mês (1-12): "))
            if not (1 <= mes <= 12):
                raise ValueError("Mês de nascimento deve ser entre 1 e 12.")
                
            dia = int(input("Dia (1-31): "))
            if not (1 <= dia <= 31):
                raise ValueError("Dia de nascimento deve ser entre 1 e 31.")
            
            return {
                "nome": nome,
                "celular": celular,
                "cpf": cpf,
                "ano_nascimento": ano,
                "mes_nascimento": mes,
                "dia_nascimento": dia
            }
        except ValueError as e:
            self.mostra_mensagem(f"Entrada inválida: {e}")
            return None

    def pegar_dados_profissional(self, alteracao=False) -> dict:
        if alteracao:
            print("\n--- Alterando Profissional ---")
        else:
            print("\n--- Cadastro de Novo Profissional ---")
        
        try:
            nome = input("Nome do Profissional: ").strip()
            if not nome:
                raise ValueError("O nome não pode ser vazio.")
            
            celular = input("Celular: ").strip()
            if not celular:
                raise ValueError("O celular não pode ser vazio.")
            
            cpf = ""
            if not alteracao:
                cpf = input("CPF: ").strip()
                if not cpf:
                    raise ValueError("O CPF não pode ser vazio.")
            
            especialidade = input("Especialidade: ").strip()
            if not especialidade:
                raise ValueError("A especialidade não pode ser vazia.")
            
            registro = input("Registro Profissional (ex: CRM, CREFITO): ").strip()
            if not registro:
                raise ValueError("O registro profissional não pode ser vazio.")
            
            return {
                "nome": nome,
                "celular": celular,
                "cpf": cpf,
                "especialidade": especialidade,
                "registro_profissional": registro
            }
        except ValueError as e:
            self.mostra_mensagem(f"Entrada inválida: {e}")
            return None

    def pegar_dados_tipo_atendimento(self, alteracao=False) -> dict:
        if alteracao:
            print("\n--- Alterando Tipo de Atendimento ---")
        else:
            print("\n--- Cadastro de Novo Tipo de Atendimento ---")
        
        try:
            descricao = input("Descrição (ex: Consulta, Exame, Retorno): ").strip()
            if not descricao:
                raise ValueError("A descrição não pode ser vazia.")
            
            valor_base = float(input("Valor Base (R$): "))
            if valor_base < 0:
                raise ValueError("O valor base não pode ser negativo.")
                
            return {
                "descricao": descricao,
                "valor_base": valor_base
            }
        except ValueError as e:
            self.mostra_mensagem(f"Entrada inválida: {e}")
            return None

    def pegar_dados_atendimento(self) -> dict:
        print("\n--- Cadastro de Agendamento ---")
        try:
            print("\nData do Atendimento:")
            ano = int(input("Ano (ex: 2026): "))
            if ano < 2020:
                raise ValueError("Ano inválido.")
            mes = int(input("Mês (1-12): "))
            if not (1 <= mes <= 12):
                raise ValueError("Mês inválido.")
            dia = int(input("Dia (1-31): "))
            if not (1 <= dia <= 31):
                raise ValueError("Dia inválido.")

            print("\nHorário de Início:")
            hora_inicio = int(input("Hora de início (0-23): "))
            if not (0 <= hora_inicio <= 23):
                raise ValueError("Hora de início inválida.")
            minuto_inicio = int(input("Minuto de início (0-59): "))
            if not (0 <= minuto_inicio <= 59):
                raise ValueError("Minuto de início inválido.")

            print("\nHorário de Término:")
            hora_fim = int(input("Hora de término (0-23): "))
            if not (0 <= hora_fim <= 23):
                raise ValueError("Hora de término inválida.")
            minuto_fim = int(input("Minuto de término (0-59): "))
            if not (0 <= minuto_fim <= 59):
                raise ValueError("Minuto de término inválido.")

            valor = float(input("\nValor do Atendimento (R$): "))
            if valor < 0:
                raise ValueError("O valor não pode ser negativo.")

            return {
                "ano": ano,
                "mes": mes,
                "dia": dia,
                "hora_inicio": hora_inicio,
                "minuto_inicio": minuto_inicio,
                "hora_fim": hora_fim,
                "minuto_fim": minuto_fim,
                "valor": valor
            }
        except ValueError as e:
            self.mostra_mensagem(f"Entrada inválida: {e}")
            return None

    def pegar_dados_procedimento(self) -> dict:
        print("\n--- Adicionar Procedimento ---")
        try:
            descricao = input("Descrição do procedimento: ").strip()
            if not descricao:
                raise ValueError("A descrição não pode ser vazia.")
            custo = float(input("Custo do procedimento (R$): "))
            if custo < 0:
                raise ValueError("O custo não pode ser negativo.")
            return {
                "descricao": descricao,
                "custo": custo
            }
        except ValueError as e:
            self.mostra_mensagem(f"Entrada inválida: {e}")
            return None

    def pegar_dados_pagamento(self) -> dict:
        print("\n--- Registrar Pagamento ---")
        try:
            print("\nData do Pagamento:")
            ano = int(input("Ano (ex: 2026): "))
            mes = int(input("Mês (1-12): "))
            dia = int(input("Dia (1-31): "))

            valor = float(input("Valor Pago (R$): "))
            if valor <= 0:
                raise ValueError("O valor pago deve ser maior que zero.")

            print("\nModalidade de Pagamento:")
            print("1) PIX")
            print("2) Dinheiro")
            print("3) Cartão de Crédito")
            tipo = int(input("Escolha a modalidade: "))

            if tipo not in [1, 2, 3]:
                raise ValueError("Modalidade inválida.")

            cpf_pagador = ""
            numero_cartao = ""
            bandeira = ""

            if tipo == 1:
                cpf_pagador = input("CPF do Pagador: ").strip()
                if not cpf_pagador:
                    raise ValueError("O CPF do pagador é obrigatório para PIX.")
            elif tipo == 3:
                numero_cartao = input("Número do Cartão: ").strip()
                if not numero_cartao:
                    raise ValueError("O número do cartão é obrigatório.")
                bandeira = input("Bandeira do Cartão (ex: Visa, Master): ").strip()
                if not bandeira:
                    raise ValueError("A bandeira do cartão é obrigatória.")

            return {
                "ano": ano,
                "mes": mes,
                "dia": dia,
                "valor": valor,
                "tipo": tipo,
                "cpf_pagador": cpf_pagador,
                "numero_cartao": numero_cartao,
                "bandeira": bandeira
            }
        except ValueError as e:
            self.mostra_mensagem(f"Entrada inválida: {e}")
            return None

    def mostrar_clinicas(self, clinicas: list):
        print("\n" + "="*60)
        print(f"{'NOME':<20} | {'CIDADE':<15} | {'FUNCIONAMENTO':<12}")
        print("="*60)
        for clinica in clinicas:
            horario = f"{clinica.horario_inicial.strftime('%H:%M')} - {clinica.horario_fim.strftime('%H:%M')}"
            print(f"{clinica.nome:<20} | {clinica.cidade:<15} | {horario:<12}")
            print(f"Descrição: {clinica.descricao}")
            print("-"*60)

    def mostrar_pacientes(self, pacientes: list):
        print("\n" + "="*70)
        print(f"{'NOME':<25} | {'CPF':<15} | {'CELULAR':<15} | {'NASCIMENTO':<10}")
        print("="*70)
        for pac in pacientes:
            nascimento_str = pac.nascimento.strftime("%d/%m/%Y")
            print(f"{pac.nome:<25} | {pac.cpf:<15} | {pac.celular:<15} | {nascimento_str:<10}")
        print("="*70)

    def mostrar_profissionais(self, profissionais: list):
        print("\n" + "="*80)
        print(f"{'NOME':<25} | {'CPF':<15} | {'CELULAR':<15} | {'ESPECIALIDADE':<15} | {'REGISTRO':<10}")
        print("="*80)
        for prof in profissionais:
            print(f"{prof.nome:<25} | {prof.cpf:<15} | {prof.celular:<15} | {prof.especialidade:<15} | {prof.registro_profissional:<10}")
        print("="*80)

    def mostrar_tipos_atendimento(self, tipos: list):
        print("\n" + "="*50)
        print(f"{'DESCRIÇÃO':<30} | {'VALOR BASE':<15}")
        print("="*50)
        for t in tipos:
            print(f"{t.descricao:<30} | R$ {t.valor_base:<13.2f}")
        print("="*50)

    def mostrar_atendimentos(self, atendimentos: list):
        print("\n" + "="*80)
        print(f"{'IND':<4} | {'DATA':<10} | {'HORÁRIO':<13} | {'CLÍNICA':<15} | {'PACIENTE':<15} | {'RESTANTE':<12}")
        print("="*80)
        for idx, a in enumerate(atendimentos):
            horario = f"{a.horario_inicio.strftime('%H:%M')}-{a.horario_fim.strftime('%H:%M')}"
            data_str = a.data.strftime("%d/%m/%Y")
            print(f"{idx:<4} | {data_str:<10} | {horario:<13} | {a.clinica.nome:<15} | {a.paciente.nome:<15} | R$ {a.valor_restante():<9.2f}")
        print("="*80)

    def mostrar_relatorios(self, rel_clinicas, custo_barato, atend_barato, custo_caro, atend_caro, rel_procedimentos, proc_barato, proc_caro):
        print("\n" + "============================================================")
        print("                 RELATÓRIOS CONSOLIDADOS")
        print("============================================================")

        # 1. Clínicas com maior número de atendimentos
        print("\n1. clínicas com maior número de atendimentos:")
        print(f"   {'CLÍNICA':<30} | {'AGENDAMENTOS':<15}")
        print("   " + "-"*48)
        for clinica, qtd in rel_clinicas:
            print(f"   {clinica:<30} | {qtd:<15}")

        # 2. Atendimentos mais caros e mais baratos
        print("\n2. atendimentos mais caros e mais baratos:")
        print(f"   * Mais Barato (Total R$ {custo_barato:.2f}):")
        print(f"     Clínica: {atend_barato.clinica.nome} | Paciente: {atend_barato.paciente.nome} | Data: {atend_barato.data.strftime('%d/%m/%Y')}")
        print(f"   * Mais Caro (Total R$ {custo_caro:.2f}):")
        print(f"     Clínica: {atend_caro.clinica.nome} | Paciente: {atend_caro.paciente.nome} | Data: {atend_caro.data.strftime('%d/%m/%Y')}")

        # 3. Procedimentos mais realizados (populares)
        print("\n3. procedimentos mais realizados (populares):")
        if rel_procedimentos:
            print(f"   {'PROCEDIMENTO':<30} | {'FREQUÊNCIA':<15}")
            print("   " + "-"*48)
            for proc, qtd in rel_procedimentos:
                print(f"   {proc:<30} | {qtd:<15}")
        else:
            print("   Nenhum procedimento registrado no sistema.")

        # 4. Procedimentos mais caros e mais baratos
        print("\n4. procedimentos mais caros e mais baratos:")
        if proc_barato and proc_caro:
            print(f"   * Mais Barato: {proc_barato.descricao} (Custo: R$ {proc_barato.custo:.2f}) | Resp: {proc_barato.profissional_responsavel.nome}")
            print(f"   * Mais Caro: {proc_caro.descricao} (Custo: R$ {proc_caro.custo:.2f}) | Resp: {proc_caro.profissional_responsavel.nome}")
        else:
            print("   Nenhum procedimento registrado no sistema.")
        print("\n" + "============================================================")

    def selecionar_clinica(self) -> str:
        return input("\nDigite o nome da clínica: ").strip()

    def selecionar_paciente(self) -> str:
        return input("\nDigite o CPF do paciente: ").strip()

    def selecionar_profissional(self) -> str:
        return input("\nDigite o CPF do profissional: ").strip()

    def selecionar_tipo_atendimento(self) -> str:
        return input("\nDigite a descrição do tipo de atendimento: ").strip()

    def selecionar_atendimento(self) -> int:
        try:
            return int(input("\nDigite o número (IND) do atendimento selecionado: "))
        except ValueError:
            return -1