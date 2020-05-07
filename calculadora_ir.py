from CalculadoraIRRF import CalculadoraIRRF
from DeducaoDependente import DeducaoDependente
from calculadora import enquadramento_aliquota

def calcula_inss(salario):
    """
    Calcula valor a ser pago de INSS com base no salário
    """
    valor_a_ser_pago = salario * 0.11
    return valor_a_ser_pago

def calcula_final_depende(salario, dependentes):
    salario_base = salario - calcula_inss(salario)
    salario_base = salario_base - DeducaoDependente().deducao_dependente(dependentes)
    aliquota = 0 if type(enquadramento_aliquota(salario_base)) == str else enquadramento_aliquota(salario_base)
    calculo_irrf = CalculadoraIRRF().subtrair_base_irrf(salario_base)
    valor_imposto = (calculo_irrf * aliquota) / 100
    valor_imposto = float('%.2f' % valor_imposto)

    return valor_imposto
