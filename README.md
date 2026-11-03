# CP6 - triagem de chamados de TI

## integrantes

- Cassiano Rocha Assumpção - RM 568632

## solução

programa em python que lê o chamados.json e tem 2 menus:

1. métricas: total de chamados, usuários afetados, tempo médio estimado, chamados por impacto e por tipo
2. fila de atendimento: os chamados em ordem de prioridade, com o próximo em destaque

## estratégia

cada chamado ganha pontos e a fila vai do maior pro menor:

```
pontos = peso do impacto x 20 + usuarios afetados + setores afetados x 5
```

peso do impacto: alto 3, medio 2, baixo 1

o impacto pesa mais porque é a gravidade do problema, então um chamado alto sai 20 pontos na frente de um medio. depois conta quantas pessoas ficaram paradas (1 ponto cada) e quantos setores foram afetados (5 cada), porque problema que pega vários setores atrapalha mais a empresa.

se der empate vai primeiro quem abriu antes, que tá esperando há mais tempo.

não usei o tipo nem o tempo estimado. o impacto já diz a gravidade, e se priorizasse pelo tempo os problemas grandes e demorados iam ficar pro final.

## como rodar

```
python3 main.py
```

o chamados.json tem que estar na mesma pasta.
