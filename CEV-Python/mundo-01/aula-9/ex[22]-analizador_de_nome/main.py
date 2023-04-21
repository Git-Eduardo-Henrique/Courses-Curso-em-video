# =======================================================================
# coleta o nome
print(60 * "\033[31m=", "\033[m")
nome = str(input('Digite seu \033[31mnome\033[m: '))
print(60 * "\033[31m=", "\033[m",
      '\nAnalizando seu \033[31mnome...\033[m')
print(60 * "\033[31m=", "\033[m")
# =======================================================================
# mostra o nome formatado de varias formas
print(f'Seu nome em \033[31mMAIUSCULAS\033[m: {nome.upper()}\n'
      f'Seu nome em \033[31mminusculas\033[m: {nome.lower()}\n'
      f'Seu nome tem: \033[31m{len(nome) - nome.count(" ")} letras\033[m\n'
      f'Seu primeiro nome é: \033[31m{nome.split()[0]}\033[m e tem \033[31m{len(nome.split()[0])} letras\033[m')
print(60 * "\033[31m=", "\033[m")
# =======================================================================
