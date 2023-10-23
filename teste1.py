from chempy import Substance

def calcular_massa_molar(formula):

    substancia = Substance.from_formula(formula)

    massa_molar = substancia.mass

    return massa_molar

while True:
    print("Calculadora de Massa Molar")
    formula = input("Digite a fórmula química (ou 'sair' para encerrar): ")

    if formula.lower() == 'sair':
        break

    try:
        massa_molar = calcular_massa_molar(formula)
        print(f"A massa molar de {formula} é {massa_molar:.2f} g/mol")
    except ValueError:
        print("Fórmula química inválida. Tente novamente.")
