from datetime import date, time
from clinica import Clinica
from paciente import Paciente
from profissional import Profissional
from tipoAtendimento import TipoAtendimento
from procedimento import Procedimento
from pagamento import PagamentoCartao, PagamentoDinheiro, PagamentoPix


class Atendimento:
    def __init__(self,ano:int,mes:int,dia:int, hora_inicio:int,minuto_inicio:int, hora_fim:int,minuto_fim:int,
                valor:float, clinica:Clinica, paciente:Paciente, profissional:Profissional, tipo_atend:TipoAtendimento):
        self.__data = date(ano,mes,dia)
        self.__horario_inicio = time(hora_inicio,minuto_inicio)
        self.__horario_fim = time(hora_fim,minuto_fim)
        self.__valor = valor
        if isinstance(clinica,Clinica):
            self.__clinica = clinica
        if isinstance(paciente,Paciente):
            self.__paciente = paciente
        if isinstance(profissional,Profissional):
            self.__profissional_responsavel = profissional
        if isinstance(tipo_atend,TipoAtendimento):
            self.__tipo_atendimento = tipo_atend
        self.__pagamentos = []
        self.__procedimentos = []
       
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self,ano,mes,dia):
        self.__data=date(ano,mes,dia)
    
    @property
    def horario_inicio(self):
        return self.__horario_inicio
    @horario_inicio.setter
    def horario_inicio(self, hora, minuto):
        self.__horario_inicio=time(hora,minuto)
    
    @property
    def horario_fim(self):
        return self.__horario_fim
    @horario_fim.setter
    def horario_fim(self, hora, minuto):
        self.__horario_fim=time(hora,minuto)

    @property
    def valor(self):
        return self.__valor
    @valor.setter
    def valor(self, valor:float):
        self.__valor = valor
    
    @property
    def clinica(self):
        return self.__clinica
    @clinica.setter
    def clinica(self, clinica:Clinica):
        if isinstance(clinica,Clinica):
            self.__clinica = clinica
    
    @property
    def paciente(self):
        return self.__paciente
    @paciente.setter
    def paciente(self, paciente:Paciente):
        if isinstance(paciente,Paciente):
            self.__paciente = paciente

    @property
    def profissional_responsavel(self):
        return self.__profissional_responsavel
    @profissional_responsavel.setter
    def profissional_responsavel(self, profissional_responsavel:Profissional):
        if isinstance(profissional_responsavel,Profissional):
            self.__profissional_responsavel = profissional_responsavel
    
    @property
    def tipo_atendimento(self):
        return self.__tipo_atendimento
    @tipo_atendimento.setter
    def tipo_atendimento(self, tipo_atendimento:TipoAtendimento):
        if isinstance(tipo_atendimento,TipoAtendimento):
            self.__tipo_atendimento = tipo_atendimento
    
    @property
    def pagamentos(self):
        return self.__pagamentos
    def adicionar_pagamento(self, valor_pag_pix:float, cpf_pag_pix:str,
                            numero_cartao:str, bandeira:str):
        cntrl=0
        while cntrl==0:
            opcao_usuario=input('digitar opção de pagamento: 1=Pix, 2=Dinheiro, 3=Cartão. Digitar:')
            match opcao_usuario:
                case "1":
                    pagamento = PagamentoPix(self.__data, self.__paciente, valor_pag_pix, cpf_pag_pix)
                    cntrl+=1
                case '2':
                    pagamento = PagamentoDinheiro(self.__data, self.__paciente, valor_pag_pix)
                    cntrl+=1
                case "3":
                    pagamento = PagamentoCartao(self.__data, self.__paciente, valor_pag_pix,numero_cartao,bandeira)
                    cntrl+=1
                case _:
                    print('Opção inválida')
        self.__pagamentos.append(pagamento)
    def remover_pagamento(self):
        ultimo=len(self.pagamentos)
        self.__pagamentos.pop(ultimo-1)

    @property
    def procedimentos(self):
        return self.__procedimentos
    def adicionar_procedimento(self, descricao:str, custo:float, profissional:Profissional):
        if isinstance(profissional,Profissional):
            self.__procedimentos.append(Procedimento(descricao,custo,profissional))
    def remover_procedimento(self):
        ultimo=len(self.procedimentos)
        self.__procedimentos.pop(ultimo-1)

    def valor_de_atendimento(self):
        total=0
        total+=self.__tipo_atendimento.valor_base
        return total

    def total_de_procedimentos(self):
        total=0
        for x in range(len(self.__procedimentos)):
            total+=self.__procedimentos[x].custo
        return total
    
    def valor_restante(self):
        valor_restante=self.__valor
        valor_restante+=self.total_de_procedimentos()
        valor_restante+=self.valor_de_atendimento()
        for x in range(len(self.__pagamentos)):
            valor_restante-=self.__pagamentos[x].valor
        return valor_restante

    #controlador
    def verificar_idade(self):
        dezoito=self.data.year-18
        data_permitida=date(dezoito,self.data.month,self.data.day)
        if self.paciente.nascimento>data_permitida:
            print('block')