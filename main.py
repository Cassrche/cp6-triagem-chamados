import json

PESO = {"alto": 3, "medio": 2, "baixo": 1}


def carregar():
    with open("chamados.json", encoding="utf-8") as f:
        return json.load(f)


def pontos(c):
    return PESO[c["impacto"]] * 20 + c["usuarios_afetados"] + len(c["setores_afetados"]) * 5


def ordenar(chamados):
    return sorted(chamados, key=lambda c: (-pontos(c), c["data_abertura"], c["hora_abertura"]))


def contar(chamados, campo):
    total = {}
    for c in chamados:
        total[c[campo]] = total.get(c[campo], 0) + 1
    return total


def metricas(chamados):
    print("\n--- metricas ---")
    print("total de chamados:", len(chamados))
    print("usuarios afetados:", sum(c["usuarios_afetados"] for c in chamados))
    print("tempo medio estimado:", round(sum(c["tempo_estimado_min"] for c in chamados) / len(chamados), 1), "min")
    print("por impacto:", contar(chamados, "impacto"))
    print("por tipo:", contar(chamados, "tipo"))


def fila(chamados):
    ordem = ordenar(chamados)
    p = ordem[0]
    print("\n--- fila ---")
    print(f"PROXIMO: #{p['id']} {p['titulo']} ({p['tipo']}, {p['impacto']}, {pontos(p)} pts)")
    for i, c in enumerate(ordem[1:], 2):
        print(f"{i}. #{c['id']} {c['titulo']} ({c['tipo']}, {c['impacto']}, {pontos(c)} pts)")


chamados = carregar()
while True:
    op = input("\n1 - metricas\n2 - fila de atendimento\n0 - sair\n> ")
    if op == "1":
        metricas(chamados)
    elif op == "2":
        fila(chamados)
    elif op == "0":
        break
    else:
        print("opcao invalida")
