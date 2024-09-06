def notas(*num, sit=False):
    """
    -> Quarda notas, media e situação de um aluno em
    um dicionario
    :param num: Todas as notas do aluno
    :param sit: (OPCIONAL) Escolha do user adiconar a situação
    do aluno no dicionario (RUIM, RAZOAVEL, BOA)
    :return: Retorna o dicionario
    """
    total = 0
    for n in num:
        total += n
    media = total/len(num)
    dicio = {'total': len(num), 'maior': max(num), 'menor': min(num), 'media': media}
    if sit:
        if media <= 5:
            dicio['Situação'] = 'RUIM'
        elif media <= 7:
            dicio['Situação'] = 'RAZOAVEL'
        elif media > 7:
            dicio['Situação'] = 'BOA'
    return dicio


rps = notas(3, 10, 10, sit=True)
print(rps)
