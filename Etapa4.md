![image](https://user-images.githubusercontent.com/83672645/224572661-cebd62a3-3d7e-4195-80f0-3f97db0c7499.png)


# Etapa 4 - Aprendizagem de Máquina

Nesta Etapa, utilizamos o MLflow, plataforma desenvolvida pela Databricks, para gerenciar e acompanhar os diferentes experimentos realizados, com o objetivo de registrar as configurações dos algoritmos, hiperparâmetros, métricas, desempenho e visualização dos resultados. 

Conforme consta na documentação do MLflow, “O MLflow é uma plataforma versátil, expansível e de código aberto para gerenciar fluxos de trabalho e artefatos em todo o ciclo de vida do aprendizado de máquina. Ele possui integrações integradas com muitas bibliotecas de ML populares, mas pode ser usado com qualquer biblioteca, algoritmo ou ferramenta de implantação. Ele foi projetado para ser extensível, para que você possa escrever plug-ins para oferecer suporte a novos fluxos de trabalho, bibliotecas e ferramentas.”

Para realizar os experimentos utilizamos um Dataframe  integrado e coerente, contendo os registros pré-processados na etapa anterior, conforme segue abaixo. 
  
![image](https://github.com/lbragalopes/PUC_ArquiteturaDados_Nuvem/assets/83672645/793a590e-5e96-4f1a-807c-fb44904c28bb)

É importante destacar que, Modelos de Machine Learning podem ser afetados negativamente por dados faltantes ou desbalanceados, o que pode resultar em modelos imprecisos ou enviesados. 

Por isso, antes de iniciar os experimentos, verificamos a qualidade dos dados e a presença de anomalias nas variáveis “Tempo_Resposta” e “Nota_Cosumidor”. 
Na imagem abaixo, é possível verificar a presença de dados com baixa contagem referente a coluna “Tempo_Resposta”. 

![image](https://github.com/lbragalopes/PUC_ArquiteturaDados_Nuvem/assets/83672645/67e4f186-1d04-4633-aa77-3e3bc517a5ae)

A baixa contagem significa que essas linhas não possuem representatividade suficiente, podendo prejudicar a qualidade do modelo de aprendizado de máquina e resultar em previsões imprecisas.

Após analisar as linhas que possuem a baixa contagem, concluímos que os valores apresentados como ‘Tempo_Resposta’ contendo apenas 1 contagem, são valores “outliers”. Ou seja, são valores muitos distantes da maioria dos outros valores do conjunto de dados. Destacando que os valores fogem as regras de negócio estipulado na plataforma Consumidor.gov, não sendo viável valores negativos, como tempo de resposta. Por isso, removemos as 13 linhas que contém anomalias nos dados com relação ao tempo de resposta. 

![image](https://github.com/lbragalopes/PUC_ArquiteturaDados_Nuvem/assets/83672645/18ae833d-f42a-4ca0-b3b2-e72a0c38a1eb)

Concluindo a avaliação da qualidade dos dados, utilizamos as funções isnan, when, count e col para detectar a inexistência de valores nulos ou NaN nas colunas "Tempo_Resposta", “Nota_consumido” e "Comprou_Contratou".

![image](https://github.com/lbragalopes/PUC_ArquiteturaDados_Nuvem/assets/83672645/3485cb35-b0e5-41c8-b9a6-32a167c0ecb3)

Confirmada a qualidade dos dados, iniciamos os experimentos utilizando algoritmos distintos do tipo regressão e classificação.

Modelo de aprendizado do tipo regressão é um tipo de modelo que visa prever um valor numérico de saída a partir de um conjunto de variáveis de entrada. A regressão é usada principalmente para problemas de previsão.

No caso, utilizamos experimentos com algoritmos de regressão com o objetivo de prever a nota do consumidor com base no tempo de resposta e na forma como o serviço foi contratado ou o produto foi comprado. Visamos encontrar um padrão nas variáveis de entrada que possa explicar ou prever o valor de saída.

Para isso, definimos a coluna "Nota_Consumidor" como o valor de saída (label) e utilizamos como variáveis de entrada (features) as colunas "Tempo_Resposta" e "Comprou_Contratou".

Os modelos de regressão exigem que as variáveis de saída (label) e entrada (features) sejam numéricas, pois eles são baseados em equações matemáticas que buscam estimar a relação entre essas variáveis. Por isso, se as variáveis de saída e entrada forem categóricas, é necessário transformá-las em números para que os modelos possam operar sobre elas.

No DataFrame, a coluna "Comprou_Contratou" apresenta valores categóricos. Por isso, definimos um dicionário com as categorias existentes na coluna e seus respectivos números sequenciais. Utilizamos a função withColumn para criar novas colunas no DataFrame, com o nome "Categoria_" seguido pelo

![image](https://github.com/lbragalopes/PUC_ArquiteturaDados_Nuvem/assets/83672645/4264bbf7-2217-4602-9627-0b42242d01a8)

Já as colunas "Tempo_Resposta" e "Nota_Consumidor" possuem os dados em formato de string, sendo necessária a conversão do tipo de dados para integer. Ou seja, é necessário converter os dados para tipo numérico antes de utilizá-los no modelo de aprendizado.

![image](https://github.com/lbragalopes/PUC_ArquiteturaDados_Nuvem/assets/83672645/257ac9d9-5724-4fcd-9ac8-46097a67a685)

Para garantir a representatividade dos dados realizamos um filtro selecionando apenas as situações finalizadas. 

![image](https://github.com/lbragalopes/PUC_ArquiteturaDados_Nuvem/assets/83672645/6d55c414-ae92-4b46-a144-9d305158821d)

Após transformar o tipo dos dados para adequá-los aos modelos de aprendizado, realizamos experimentos de Machine Learning (ML) utilizando os algoritmos Random Forest, Regressão Linear e Gradient Boosting Machine (GBM), conforme descrito abaixo. 
  
&rArr; Criamos um objeto VectorAssembler para transformar as colunas do DataFrame em um único vetor de características, que é usado como entrada para o modelo de aprendizado de máquina, contendo as colunas “Tempo_Resposta” e “Categoria_”.  Lembrando que a coluna “Categoria_” representa a coluna “Comprou_Contratou” de forma numérica. 

&rArr; Experimentamos os três modelos de regressão.  Cada modelo utiliza uma classe e parâmetros específicos na sua forma de construção.  
  
>O modelo **Random Forest Regressor** é baseado em árvores de decisão que são construídas a partir de amostrar aleatórias do conjunto de treinamento.  Nesse modelo utilizamos a classe ‘RandomForestRegressor’ e os parâmetros numTrees que é o número de árvores de decisão a serem construídas,  maxDepth que é a profundidade máxima de cada árvore, e as colunas de entrada (featuresCol) e saída (labelCol).
>
>O modelo de **Regressão Linear** é um método estatístico utilizado para modelar a relação entre uma variável dependente e uma ou mais variáveis independentes. Nesse modelo utilizamos a classe ‘LinearRegression’ e os parâmetros maxIter que é o número máximo de iterações para o algoritmo de otimização, regParam que é o parâmetro de regularização, elasticNetParam que controla a proporção entre a regularização L1 e L2, e as colunas de entrada (featuresCol) e saída (labelCol).
>
>O modelo **Gradient Boosting Tree Regressor** é um algoritmo de aprendizado de máquina baseado em árvores de decisão, que são adicionadas sequencialmente para melhorar a precisão da previsão. Nesse modelo utilizamos a classe GBTRegressor, e os parâmetros maxIter que é o número máximo de iterações para o algoritmo de otimização, maxDepth que é a profundidade máxima de cada árvore e as colunas de entrada (featuresCol) e saída (labelCol).

&rArr; Criamos um pipeline para cada modelo. O Pipeline é uma sequência de estágios que podem ser executados em ordem. Assim, quando o pipeline é executado, os dados passam pelo assembler para serem transformados em um vetor de features e, em seguida, alimentam o modelo de regressão correspondente para fazer as previsões.

&rArr; Utilizamos a função randomSplit() para dividir os dados em conjuntos de treinamento (trainingData) e teste (testData), sendo 70% dos dados usados para treinamento e 30% para teste. O conjunto de treinamento será usado para treinar o modelo, enquanto o conjunto de teste será usado para avaliar o desempenho do modelo. 

&rArr; Utilizamos a função fit() para treinar os modelos seguindo a sequência das etapas do pipeline. Armazenamos o modelo treinado em variáveis de modelo, pois após treinado, ele pode ser utilizado para fazer previsões em novos dados, que não foram utilizados durante o treinamento. 

&rArr; Após treinar os modelos com os dados de treinamento, é preciso avaliar a capacidade dos modelos de fazer previsões em dados não vistos antes, os chamados dados de teste. Para isso, utilizamos a função transform() para aplicar o modelo treinado nos dados de teste para gerar previsões. 

&rArr; A avaliação de desempenho de um modelo de aprendizado de máquina é fundamental para verificar se o modelo está conseguindo fazer previsões precisas e confiáveis. Para avaliar os modelos criamos o objeto RegressionEvaluator, e utilizamos a função evaluate é chamada para calcular as métricas MSE e RMSE.

&rArr; Para finalizar, utilizamos o MLflow para registrar os parâmetros e métricas dos modelos treinados e salvar os modelos em um formato que pode ser facilmente implantado em outras aplicações.

![image](https://github.com/lbragalopes/PUC_ArquiteturaDados_Nuvem/assets/83672645/ef7ebe9e-a270-4a49-a81a-f1a2a6f7eba4)

*Segue o notebook completo 'Modelos_Regressao' na pasta: [aprendizado_maquina](https://github.com/lbragalopes/PUC_ArquiteturaDados_Nuvem/aprendizado_maquina/Modelos_Regressao.ipynb)*

Utilizando a métrica de erro médio (MSE), os experimentos apresentaram o seguinte resultado:
•	Regressão Linear: 3.090
•	Random Forest: 3.066
•	GBM: 3.045

Com relação ao MSE, podemos afirmar que o modelo GBM apresentou o menor MSE, indicando que possui a menor média de erros quadráticos em relação aos dados de teste. 

Utilizando a métrica erro médio quadrático da raiz (RMSE), os experimentos apresentaram o seguinte resultado:
• Regressão Linear: 1.758
• Random Forest: 1.751
• GBM: 1.745

Da mesma forma, o menor valor de RMSE indica um desempenho melhor do modelo em termos de minimização do erro, considerando a raiz quadrada do erro.
Comparando os resultados dos experimentos, podemos afirmar que com base nos valores de MSE e RMSE fornecidos, o modelo GBM parece ter o melhor desempenho em termos de minimização do erro em comparação com os modelos de Regressão Linear e Random Forest.

![image](https://github.com/lbragalopes/PUC_ArquiteturaDados_Nuvem/assets/83672645/da80f9d8-54ce-4f30-97dc-907b12c9227d)




***Referências:***
 - MLflow Documentation: https://www.mlflow.org/
 - Regressão Linear: https://spark.apache.org/docs/latest/ml-classification-regression.html#linear-regression
 - Random Forest: https://spark.apache.org/docs/latest/ml-classification-regression.html#random-forest-regression
 - Gradient Boosting Machine: https://spark.apache.org/docs/latest/ml-classification-regression.html#gradient-boosted-tree-regression





