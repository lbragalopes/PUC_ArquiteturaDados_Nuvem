![image](https://user-images.githubusercontent.com/83672645/224572661-cebd62a3-3d7e-4195-80f0-3f97db0c7499.png)


# Etapa 5 - Análise dos Resultados

Na Etapa anterior, apresentamos o treinamento de máquina de três modelos de regressão (Random Forest, Regressão Linear e Gradient Boosted Trees), bem como avaliamos o desempenho utilizando as métricas MSE e RMSE. 

Nesta etapa, continuaremos utilizando a ferramenta Databricks para analisar os resultados. 

Para interpretar os resultados de cada algoritmo de regressão, comparamos as métricas de desempenho (MSE e RMSE) dos diferentes modelos. Essas métricas nos ajudam a avaliar quanto cada modelo está ajustando os dados e a fazer uma comparação objetiva entre eles. Utilizamos o seguinte código para calcular e visualizar as métricas MSE e RMSE em gráficos de barras:

![image](https://github.com/lbragalopes/PUC_ArquiteturaDados_Nuvem/assets/83672645/e88bd594-1d8f-4404-abb8-cc261f4c8a75)


Observando os gráficos é possível concluir que os modelos de regressão tiveram um desempenho semelhante em termos de erro quadrático médio. Isso indica que os modelos não apresentaram diferenças significativas na capacidade de fazer previsões precisas com base nos dados fornecidos. Ou seja, não há um modelo claramente superior em termos de desempenho de acordo com essa métrica específica.

Para explorar os dados e os resultados do modelos, comparamos as previsões feitas pelos modelos de regressão linear com os valores reais, plotando um gráfico de dispersão. Utilizamos o código. 

![image](https://github.com/lbragalopes/PUC_ArquiteturaDados_Nuvem/assets/83672645/1b6745bb-8eee-42c8-888e-cdd64d3fcc67)


O gráfico acima permite visualizar como as previsões do modelo estão se aproximando ou afastando dos valores reais. No caso, é possível identificar que as previsões do modelo estão tendendo a ser consistentemente próximas, independentemente dos valores reais. Esse alinhamento horizontal indica que o modelo está realizando previsões com um certo grau de precisão, embora possa não estar capturando todas as nuances dos valores reais.

Com base na análise dos resultados dos modelos de regressão, concluímos que os três algoritmos - Random Forest, Regressão Linear e Gradient Boosted Trees - tiveram um desempenho semelhante em relação às métricas MSE e RMSE. Isso indica que eles foram capazes de ajustar os dados e fazer previsões com níveis comparáveis de precisão.
Ao explorar os dados e os resultados dos modelos, observamos que as previsões do modelo de regressão linear apresentaram uma tendência de se aproximar dos valores reais de forma consistente, independentemente dos valores reais. 

**Segue o notebook completo 'Analise_resultados' na pasta: [Analise_resultado]
