from clinica import Clinica
from paciente import Paciente
from profissional import Profissional
from tipoAtendimento import TipoAtendimento
from atendimento import Atendimento

raul=Paciente("raul","(48) 988587817", "103.829.772.79", 2008, 3, 15)
tiago=Paciente("tiago","(55) 942587217", "206.999.772.79", 2000, 9, 22)
polo_sul=Clinica("Polo Sul", "São José", "Clinica para perda de cabelo", 12, 30, 18, 30)
dr_raimundo=Profissional("Raimundo Teixeira", "(99) 01823901", "327.191.182.32", "Socorrista",
                         'sou legalmente registrado')
cabelo=TipoAtendimento("Remoto",  2000)
ligando=Atendimento(2026,6,1,14,24,15,30,10000,polo_sul,raul,dr_raimundo,cabelo)
#ligando.adicionar_procedimento("Pegar cabelo na caixa e colar na cabeça dele", 12000.00, dr_raimundo)
#ligando.adicionar_procedimento("Pegar barba na caixa e colar no queixo dele", 7000.00, dr_raimundo)
#ligando.adicionar_procedimento("Pegar bigode na caixa e colar no buço dele", 5000.00, dr_raimundo)
ligando.adicionar_pagamento(5000.00,"0","28999999999","Visa")
ligando.adicionar_pagamento(3000.00,"0","28999999999","Visa")
#ligando.adicionar_pagamento(2000.00,"0","28999999999","Visa")
ligando.remover_pagamento()
a=ligando.valor_restante()
print(a)
b=ligando.data
print(b)
ligando.verificar_idade()