from meu_pacote.moduloA.script_A import var_A
from meu_pacote.moduloB.script_B import var_B
from meu_pacote.moduloC.script_C import var_C

def func():
    print(var_A +  var_B + var_C)


if __name__ == '__main__':
    print('Testando: func')
    func ()