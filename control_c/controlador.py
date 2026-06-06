from model_m.clinica import Clinica
from model_m.paciente import Paciente
from model_m.profissional import Profissional
from model_m.tipoAtendimento import TipoAtendimento
from model_m.atendimento import Atendimento
from view_v.tela import TelaApp

class ControladorAbas:
    def __init__(self):
        self.__paginas=['Menu Inicial']
    
    @property
    def paginas(self):
        return self.__paginas
    def nova_aba(self,nova_aba:str):
        self.__paginas.append(nova_aba)
    def voltar_aba(self):
        if len(self.__abas>1):
            self.__abas.pop(len(self.__paginas)-1)
        else:
            print('Você já esta no Menu Inicial.')

class ControlarGeral:
    def __init__(self,abas:ControladorAbas):
        if isinstance(abas,ControladorAbas):
            self.__abas=abas
    def todas_abas(self, aba:str):
        while self.__abas.paginas[-1]=="Menu Inicial":
            match aba:
                case 1:
                    self.__abas.nova_aba("Entrando como Clinica")
        while self.__abas.paginas[-1]=="Entrando como Clinica":
            match aba:
                case 1:
                    self.__abas.nova_aba("Entrando como Clinica")
