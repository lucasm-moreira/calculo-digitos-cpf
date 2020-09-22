# Método responsável por preencher o cpf até ter 11 dígitos
def completaCpf(cpf):
    if (len(cpf) > 9):
        print("Você deve digitar um cpf com no máximo 9 dígitos!")
        exit()

    if (len(cpf) < 9):
        cpf = cpf.zfill(11)
        return cpf

    return cpf

#Método para validar primeiro dígito verificador
def validaPrimeiroDigito(cpf):
    soma = 0
    modulo = 0
    fator_soma = 10
    iterador = 0
    primeiro_digito_verificador = 0
    resultado_subtracao = 0
    cpf_list = list(cpf)

    for i in range(10, 1, -1):
        soma += (int(str(cpf_list[iterador])) * fator_soma)
        iterador = iterador + 1
        fator_soma = fator_soma - 1

    modulo = soma % 11

    resultado_subtracao = 11 - modulo

    if(resultado_subtracao >= 10):
        primeiro_digito_verificador = 0

    else:
        primeiro_digito_verificador = resultado_subtracao

    cpf_list.append(str(primeiro_digito_verificador))

    cpf = ''.join(cpf_list)

    return cpf

#Método para validar segundo dígito verificador
def validaSegundoDigito(cpf):
    soma = 0
    modulo = 0
    fator_soma = 11
    iterador = 0
    segundo_digito_verificador = 0
    resultado_subtracao = 0
    cpf_list = list(cpf)

    for i in range(11, 1, -1):
        soma += (int(str(cpf_list[iterador])) * fator_soma)
        iterador = iterador + 1
        fator_soma = fator_soma - 1

    modulo = soma % 11

    resultado_subtracao = 11 - modulo

    if(resultado_subtracao >= 10):
        segundo_digito_verificador = 0

    else:
        segundo_digito_verificador = resultado_subtracao

    cpf_list.append(str(segundo_digito_verificador))

    cpf = ''.join(cpf_list)

    return cpf

#Método para inserir máscara no CPF
def inserirMascara(cpf) :
    cpf = '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
    return cpf

# Input para receber o valor do CPF
cpf = str(input("Digite o CPF (sem pontos ou hífens): "))

cpf = completaCpf(cpf)
cpf_primeiro_digito = validaPrimeiroDigito(cpf)
cpf_segundo_digito = validaSegundoDigito(cpf_primeiro_digito)
cpf_formatado = inserirMascara(cpf_segundo_digito)

print("O CPF com os dígitos verificadores é: {}".format(cpf_formatado))