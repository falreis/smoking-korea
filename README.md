# smoking-korea

Classification of smokers, former smokers and non-smokers based on a public health dataset from South Korea.

Dataset: https://www.data.go.kr/data/15007122/fileData.do#tab-layer-file


---
## Aprendizado de Dados de Saúde Pública da Coréia do Sul

O trabalho a seguir foi desenvolvido para tarefas de aprendizado de máquinas em uma base de dados de saúde pública da Coréia.

A base é denominada **[National Health Insurance Corporation_Health Checkup Information](https://www.data.go.kr/data/15007122/fileData.do#/layer_data_infomation)** (tradução automática de coreano para inglês) e está disponível no [portal público de dados do governo da Coréia](https://www.data.go.kr/data/15007122/fileData.do#/layer_data_infomation).

A base de dados foi obtida à partir da base **[Body signal of smoking](https://www.kaggle.com/datasets/kukuroo3/body-signal-of-smoking)**, disponível no [Kaglle](https://www.kaggle.com/). Essa última base corresponde a uma versão simplificada da base original.

A base [National Health Insurance Corporation_Health Checkup Information](https://www.data.go.kr/data/15007122/fileData.do#/layer_data_infomation) contém 1.000.000 de registros de check-up de saúde e seus dependentes com mais de 40 anos, membros locais que são chefes de família e membros locais com mais de 40 anos e aqueles que atingiram a idade de 40 e 66 entre os sujeitos a check-up geral de saúde.

São dados abertos que consistem em informações básicas (sexo, idade, código do teste, etc.) e detalhes do exame (altura, peso, colesterol total, hemoglobina, etc.).

As informações de uso de cigarros não englobam cigarros eletrônicos.


### Dicionário de Dados

Uma vez que a base de dados está disponível apenas em coreano, foi utilizado o Google Tradutor para auxiliar na tarefa de entendimento dos rótulos de dados e códigos disponíveis.

A base de dados foi rotulada com auxílio do dicionário de dados, disponível no arquivo "National Health Information Data Health Checkup Information User Manual_20171027" (dentro do menu "Periodic historical data (20 cases"), na página da [base de dados](https://www.data.go.kr/data/15007122/fileData.do#/layer_data_infomation).

O arquivo está disponível em formato hwp (equivalente ao Word, para arquivos em coreano) e foi aberto com auxílio de um [visualizador online](https://appzend.herokuapp.com/hwpviewer/).

Abaixo estão descritas algumas informações importantes acerca dos dados disponíveis na base.

#### Código da Localidade (Try Code)

* 11 Seul
* 26 Busan
* 27 Cidade Metropolitana de Daegu
* 28 Incheon Cidade Metropolitana
* 29 Gwangju
* 30 Daejeon
* 31 Cidade Metropolitana de Ulsan
* 36 Cidade Autônoma Especial de Sejong
* 41 Gyeonggi-do
* 42 Gangwon-do
* 43 Chungcheongbuk-do
* 44 Chungcheongnam-do
* 45 Jeollabuk-do
* 46 Jeollanam-do
* 47 Gyeongsangbuk-do
* 48 Gyeongsangnam-do
* 49 Província Autônoma Especial de Jeju

#### Gênero 

* 1 = masculino
* 2 = feminino

#### Idade

*  1 = 0-4
*  2 = 5-9
*  3 = 10-14
*  4 = 15-19
*  5 = 20-24
*  6 = 25-29
*  7 = 30-34
*  8 = 35-39
*  9 = 40-44
* 10 = 45-49
* 11 = 50-54
* 12 = 55-59
* 13 = 60-64
* 14 = 65-69
* 15 = 70-74
* 16 = 75-79
* 17 = 80-84
* 18 = 85+

#### Altura e Peso

Altura e pesos são arredondados para baixo, em intervalos de 5-5cm (ex.: 100~104cm -> 100cm)

#### Visão (Olhos Esquerdos e Direitos)

É expresso como um valor entre 0,1 e 2,5. 
A acuidade visual inferior a 0,1 é indicada como 0,1 e a cegueira como 9,9.

#### Audição (Ouvidos Esquerdos e Direitos)

São usados os seguintes códigos:

* 1 = normal
* 2 = anormal

#### Colesteróis Totais

O valor normal é de 150~250mg/dL, cerca de 1/3 é colesterol do tipo HDL, e o resto é LDL.

#### Ast Sgot (Aspartate aminotransferase (AST) / Serum Glutamic-Oxaloacetic Transaminase (SGOT))

Valores de exames de sangue que indicam função hepática, exceto hepatócitos
É uma enzima que também está presente no intestino, rim, cérebro e músculo.
A concentração aumenta quando danificado.

Valor normal 0-40IU/L

#### Alt Sgpt (Alanine Aminotransferase (ALT) / Serum Glutamic Pyruvic Transaminase (SGPT))

Valores de exames de sangue que indicam função hepática, exceto hepatócitos
É uma enzima que também está presente no intestino, rim, cérebro e músculo.
A concentração aumenta quando danificado.

Valor normal 0-40IU/L

#### Gama GPT

Valores de exames de sangue indicando função hepática, trato biliar no fígado
É uma enzima presente no tubo) que converte o ácido glutâmico em peptídeos ou aminoácidos.
Atua como um transportador de ácido, excreção biliar prejudicada (bile), hepatócitos
Aumento no sangue quando ocorre um distúrbio.

Normal: Masculino 11-63IU/L, Feminino 8-35IU/L

#### Fumantes

* 1 = I don't smoke
* 2 = I smoked before, but I quit
* 3 = I still smoke


