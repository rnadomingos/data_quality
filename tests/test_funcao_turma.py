from app.funcao import funcao_ola_turma


def test_funcao_ola_turma():
    saida = funcao_ola_turma()
    gabarito = 'Olá Turma'
    assert saida == gabarito
