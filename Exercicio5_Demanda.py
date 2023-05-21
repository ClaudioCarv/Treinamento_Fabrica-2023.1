def voto(ano_nascimento):
    from datetime import date
    idade = date.today().year - ano_nascimento

    if idade < 16:
        return "VOTO NEGADO"
    elif 16 <= idade < 18 or idade >= 65:
        return "VOTO OPCIONAL"
    else:
        return "VOTO OBRIGATÓRIO"

ano = int(input("Digite o ano de nascimento: "))
resultado = voto(ano)
print(resultado)
