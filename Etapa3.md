![image](https://user-images.githubusercontent.com/83672645/224572661-cebd62a3-3d7e-4195-80f0-3f97db0c7499.png)


# Etapa 3 - Pré-processamento de dados


  Conforme apresentado na etapa anterior, os dados necessários para este projeto foram armazenados em um bucket do S3, em vários arquivos no formato .csv, segundo disponibilizado pela plataforma consumidor.gov.

  Nessa etapa utilizamos a plataforma Databricks para realizar a padronização e a particionamento dos arquivos, assim como a limpeza e a criação das relações do conjunto de dados. 

  O Databricks foi construído sob o Apache Spark, o que permite o processamento de grandes volumes de dados. Conforme consta na documentação oficial, Databricks é um conjunto unificado de ferramentas para criar, implantar, compartilhar e manter soluções de dados de nível empresarial em escala. A Plataforma Databricks Lakehouse integra-se com armazenamento em nuvem e segurança em sua conta de nuvem e implanta a infraestrutura de nuvem em seu nome. 

  Para realizar o pré-processamento utilizando o Databricks, criamos um Workspace <Projeto_puc>. Para acessar os dados armazenados na etapa anterior, utilizamos uma função do IAM do Amazon para vincular o bucket S3 ao Workspace do Databricks. Em seguida, criamos um cluster <projeto-puc> e configuramos o acesso ao S3 através do perfil de instância com permissão de leitura, gravação e atualização do bucket S3.


![image](https://user-images.githubusercontent.com/83672645/230123929-1b29d219-1175-4741-b5bc-766e622373ac.png)


  Utilizamos o notebook do Databricks para ler os arquivos históricos armazenados no diretório raw_db do bucket S3, executamos as transformações, e em seguida salvamos os dados transformados de forma particionada em um novo diretório do S3 chamado ref_db. 

  É possível identificar no notebook (script na pasta preprocessamento) que utilizamos a biblioteca PySpark para ler o conjunto de arquivos csv. Uma das principais vantagens de utilizar o PySpark é a escalabilidade horizontal e a capacidade de processamento em grande escala. Além disso, o PySpark oferece uma API em Python, que permite realizar tarefas de análise de dados, modelagem e machine learning em grande escala.
  
![image](https://user-images.githubusercontent.com/83672645/230124166-19b9de78-3d15-404a-83cf-d73b8c01a34d.png)

É possível verificar no bucket S3 a presença do diretório ref_db, após a execução do código. 

![image](https://user-images.githubusercontent.com/83672645/230124344-6505a626-0a0a-44ad-b222-f1c1688bdf40.png)

  Para melhor desempenho no processamento dos dados, os arquivos foram particionados por data de finalização, permitindo que o processamento seja distribuído entre os nós do cluster, aumentando a eficiência e reduzindo o tempo de execução. 

  Desse modo, foram realizadas todas as limpezas e transformações necessárias para prosseguir para a etapa de aprendizado de máquina. Com os dados já particionados, será possível aplicar algoritmos de classificação e explorar os insights obtidos a partir dos resultados gerados.


***Referências:***
 - Databrick Documentation – Disponível em: https://docs.databricks.com/. Acesso em: 03 de abr. 2023
