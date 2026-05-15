# mineracao-de-dados

![GitHub branch](https://img.shields.io/badge/Branch-exercicio--24--04--sed--awk-green)

## Exercício 24-04: Manipulação de Dados com Sed e Awk

Tema: Manipulação de Dados com Sed e Awk

### Sobre o arquivo
Os comandos foram validados utilizando o arquivo real de telemetria local:
- **Arquivo:** `sensores_lab.csv`
- **Estrutura:** `id_sensor,data_coleta,temperatura,umidade,status`

### Campos do arquivo:
    - `$1` - Identificação única do sensor
    - `$2` - Data e hora da coleta
    - `$3` - Temperatura medida
    - `$4` - Umidade medida
    - `$5` - Status do sensor

---

### Exercício 1

*Imprimir apenas o ID do Sensor e a Data.*

```bash
awk -F, '{print $1, $2}' sensores_lab.csv

```

### Exercício 2

*Excluir a primeira linha do arquivo (cabeçalho) antes de exibir.*

```bash
sed '1d' sensores_lab.csv

```

### Exercício 3

*Imprimir as linhas onde a Temperatura (coluna 3) seja maior que 25.0 (ignorando o cabeçalho).*

```bash
awk -F, 'NR > 1 && $3 > 25.0' sensores_lab.csv

```

### Exercício 4

*Substituir a ocorrência de uma string via sed (mantendo a lógica do exercício para o arquivo atual).*

```bash
sed 's/DataCenter/Servidores/g' sensores_lab.csv

```

### Exercício 5

*Filtrar os registros com status OK (coluna 5) e contar o total.*

```bash
awk -F, '$5 == "OK" {count++} END {print count}' sensores_lab.csv

```

### Exercício 6

*Remover todas as linhas que contenham a palavra "ERRO" (vai limpar certinho a linha problemática do seu arquivo).*

```bash
sed '/ERRO/d' sensores_lab.csv

```

### Exercício 7

*Calcular a média de todas as temperaturas (coluna 3), desconsiderando o cabeçalho e a linha com "ERRO".*

```bash
awk -F, 'NR > 1 && $3 != "ERRO" {soma += $3; count++} END {if(count > 0) print soma/count}' sensores_lab.csv

```

### Exercício 8

*Substituir os hifens (-) das datas (coluna 2) por barras (/).*

```bash
sed 's/-/\//g' sensores_lab.csv

```

### Exercício 9

*Contar quantas vezes cada sensor (coluna 1) enviou dados usando array associativo (pulando o cabeçalho).*

```bash
awk -F, 'NR > 1 {sensores[$1]++} END {for (s in sensores) print s, sensores[s]}' sensores_lab.csv

```

### Exercício 10

*Encontrar um status específico e substituir por EMERGENCIA, imprimindo apenas a linha alterada (ajustado para buscar o status `ALERTA` que existe no seu arquivo).*

```bash
sed -n 's/ALERTA/EMERGENCIA/p' sensores_lab.csv

```

### Exercício 11

*Pipeline: sed substitui vírgulas por espaços e awk imprime a Data (coluna 2) e a Temperatura (coluna 3).*

```bash
sed 's/,/ /g' sensores_lab.csv | awk '{print $2, $3}'

```

### Exercício 12

*Encontrar o valor da temperatura mais alta (coluna 3), ignorando o cabeçalho e textos de "ERRO".*

```bash
awk -F, 'NR > 1 && $3 != "ERRO" {if ($3 > max || max == "") max=$3} END {print max}' sensores_lab.csv

```

### Exercício 13

*Adicionar a string [INSPECIONADO] no final de todas as linhas que contêm o sensor especificado (ajustado para `SENS_01`).*

```bash
sed '/SENS_01/s/$/ [INSPECIONADO]/' sensores_lab.csv

```

### Exercício 14

*Exibir o ID do Sensor (coluna 1) alinhado à esquerda com 15 caracteres seguido pela Umidade (coluna 4).*

```bash
awk -F, 'NR > 1 {printf "%-15s %s\n", $1, $4}' sensores_lab.csv

```

### Exercício 15

*Pipeline: Filtrar estritamente as leituras do `SENS_01` (já que não há "Armazém") e calcular a soma total das umidades (coluna 4).*

```bash
grep "SENS_01" sensores_lab.csv | awk -F, '{soma += $4} END {print soma}'

```