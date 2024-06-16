## PegaPlantão

**PegaPlantão** é um projeto desenvolvido para automatizar uma rotina de escritório atribuída a mim em 2022 na empresa CMA Anestesia. O objetivo era gerenciar o controle interno de entradas e saídas, horas extras e deslocamento de plantões dos médicos sócios da empresa. Este sistema atende cerca de 250 médicos, distribuídos para cumprir turnos em 12 unidades hospitalares.

### Problema Antes da Automação

Antes da automação, os registros eram feitos manualmente, resultando em um trabalho repetitivo e mentalmente cansativo. Com uma média de 150 registros por dia, cada um levando aproximadamente 1 minuto para ser processado, o processo ocupava cerca de 2 horas e 30 minutos do responsável (no caso, eu).

### Solução com Automação

Com a automação, foi possível robotizar esse processo, economizando tempo e reduzindo erros humanos. A automatização é dividida em cinco Jupyter Notebooks, conforme descrito a seguir:

### 1. Tratamento dos Dados -> `1 - Tratamento de Dados.ipynb`
Neste notebook, os dados em texto são capturados e transformados em tabelas. A seguir, alguns dos parâmetros capturados nos textos:
- Dia do plantão a ser registrado
- Horário de início ou fim do plantão, caso o indivíduo tenha entrado ou saído mais tarde ou mais cedo
- Unidade em que o indivíduo estava
- Tipo de registro (entrada, saída, extra, deslocamento de unidade, distância)

Nesta parte do projeto, exercitei o aprendizado de manipulação e manuseio de strings usando métodos built-ins, expressões regulares (regex) e funções facilitadoras contidas nos pacotes `unidecode`, `time` (para cálculos de horas) e `pandas` (para manuseio de dataframes).

### 2. Execução -> `2 - Criação de Plantões.ipynb`
Neste notebook, a automatização é realizada utilizando os pacotes `selenium`, `BeautifulSoup`, `pyautogui` e `time`. Criei um pipeline de automações de cliques e preenchimento de textos no site "Pega Plantão", onde finalmente eram utilizados os dados tratados pelo primeiro notebook.

### 3. Correções de Possíveis Erros -> `3 - Procura e Correção de Erros.ipynb`
Semelhante ao segundo notebook, porém com o objetivo e pipeline focados em procurar qualquer espaço vazio ou plantão repetido no quadro de plantões dos indivíduos (sócios médicos), garantindo assim que o mês seja encerrado sem erros que poderiam afetar o cálculo correto do pro labore.

### Benefícios

- **Eficiência:** Redução significativa do tempo gasto no registro de plantões.
- **Precisão:** Minimização de erros humanos no processo de registro.
- **Escalabilidade:** Capacidade de gerenciar um grande número de registros com facilidade.

### Conclusão

O projeto PegaPlantão demonstrou como a automação de processos repetitivos pode transformar uma tarefa tediosa e demorada em uma operação eficiente e precisa. A aplicação prática de diversas tecnologias e pacotes Python não apenas facilitou a rotina de escritório, mas também proporcionou um aprendizado valioso em automação e manipulação de dados.
