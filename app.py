aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em watts (W): "))
horasDia = float(input("Digite o tempo médio de uso diário em horas: "))
consumo = (potencia * horasDia * 30) / 1000
print("Aparelho:" , aparelho)
print("Consumo estimado:" , consumoMensal, "kwh/mês")
