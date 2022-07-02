# smoking-korea

Classification of smokers, former smokers and non-smokers based on a public health dataset from South Korea.

Dataset: https://www.data.go.kr/data/15007122/fileData.do#tab-layer-file


---
## Aprendizado de Dados de Sa�de P�blica da Cor�ia do Sul

O trabalho a seguir foi desenvolvido para tarefas de aprendizado de m�quinas em uma base de dados de sa�de p�blica da Cor�ia.

A base � denominada **[National Health Insurance Corporation_Health Checkup Information](https://www.data.go.kr/data/15007122/fileData.do#/layer_data_infomation)** (tradu��o autom�tica de coreano para ingl�s) e est� dispon�vel no [portal p�blico de dados do governo da Cor�ia](https://www.data.go.kr/data/15007122/fileData.do#/layer_data_infomation).

A base de dados foi obtida � partir da base **[Body signal of smoking](https://www.kaggle.com/datasets/kukuroo3/body-signal-of-smoking)**, dispon�vel no [Kaglle](https://www.kaggle.com/). Essa �ltima base corresponde a uma vers�o simplificada da base original.

A base [National Health Insurance Corporation_Health Checkup Information](https://www.data.go.kr/data/15007122/fileData.do#/layer_data_infomation) cont�m 1.000.000 de registros de check-up de sa�de e seus dependentes com mais de 40 anos, membros locais que s�o chefes de fam�lia e membros locais com mais de 40 anos e aqueles que atingiram a idade de 40 e 66 entre os sujeitos a check-up geral de sa�de.

S�o dados abertos que consistem em informa��es b�sicas (sexo, idade, c�digo do teste, etc.) e detalhes do exame (altura, peso, colesterol total, hemoglobina, etc.).

As informa��es de uso de cigarros n�o englobam cigarros eletr�nicos.


### Dicion�rio de Dados

Uma vez que a base de dados est� dispon�vel apenas em coreano, foi utilizado o Google Tradutor para auxiliar na tarefa de entendimento dos r�tulos de dados e c�digos dispon�veis.

A base de dados foi rotulada com aux�lio do dicion�rio de dados, dispon�vel no arquivo "National Health Information Data Health Checkup Information User Manual_20171027" (dentro do menu "Periodic historical data (20 cases"), na p�gina da [base de dados](https://www.data.go.kr/data/15007122/fileData.do#/layer_data_infomation).

O arquivo est� dispon�vel em formato hwp (equivalente ao Word, para arquivos em coreano) e foi aberto com aux�lio de um [visualizador online](https://appzend.herokuapp.com/hwpviewer/).

Abaixo est�o descritas algumas informa��es importantes acerca dos dados dispon�veis na base.

#### C�digo da Localidade (Try Code)

* 11 Seul
* 26 Busan
* 27 Cidade Metropolitana de Daegu
* 28 Incheon Cidade Metropolitana
* 29 Gwangju
* 30 Daejeon
* 31 Cidade Metropolitana de Ulsan
* 36 Cidade Aut�noma Especial de Sejong
* 41 Gyeonggi-do
* 42 Gangwon-do
* 43 Chungcheongbuk-do
* 44 Chungcheongnam-do
* 45 Jeollabuk-do
* 46 Jeollanam-do
* 47 Gyeongsangbuk-do
* 48 Gyeongsangnam-do
* 49 Prov�ncia Aut�noma Especial de Jeju

#### G�nero 

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

Altura e pesos s�o arredondados para baixo, em intervalos de 5-5cm (ex.: 100~104cm -> 100cm)

#### Vis�o (Olhos Esquerdos e Direitos)

� expresso como um valor entre 0,1 e 2,5. 
A acuidade visual inferior a 0,1 � indicada como 0,1 e a cegueira como 9,9.

#### Audi��o (Ouvidos Esquerdos e Direitos)

S�o usados os seguintes c�digos:

* 1 = normal
* 2 = anormal

#### Colester�is Totais

O valor normal � de 150~250mg/dL, cerca de 1/3 � colesterol do tipo HDL, e o resto � LDL.

#### Ast Sgot (Aspartate aminotransferase (AST) / Serum Glutamic-Oxaloacetic Transaminase (SGOT))

Valores de exames de sangue que indicam fun��o hep�tica, exceto hepat�citos
� uma enzima que tamb�m est� presente no intestino, rim, c�rebro e m�sculo.
A concentra��o aumenta quando danificado.

Valor normal 0-40IU/L

#### Alt Sgpt (Alanine Aminotransferase (ALT) / Serum Glutamic Pyruvic Transaminase (SGPT))

Valores de exames de sangue que indicam fun��o hep�tica, exceto hepat�citos
� uma enzima que tamb�m est� presente no intestino, rim, c�rebro e m�sculo.
A concentra��o aumenta quando danificado.

Valor normal 0-40IU/L

#### Gama GPT

Valores de exames de sangue indicando fun��o hep�tica, trato biliar no f�gado
� uma enzima presente no tubo) que converte o �cido glut�mico em pept�deos ou amino�cidos.
Atua como um transportador de �cido, excre��o biliar prejudicada (bile), hepat�citos
Aumento no sangue quando ocorre um dist�rbio.

Normal: Masculino 11-63IU/L, Feminino 8-35IU/L

#### Fumantes

* 1 = I don't smoke
* 2 = I smoked before, but I quit
* 3 = I still smoke


