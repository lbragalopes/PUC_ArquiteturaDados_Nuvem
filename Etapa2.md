## 2- Coleta de Dados
	
A Política de Dados Abertos do poder executivo federal, instituída pelo Decreto nº 8.777, de 11 de maio de 2016, tem por objetivo promover a publicação e disseminação de dados contidos em bases de órgãos e entidades da administração pública federal direta, autárquica e fundacional. Desta maneira, as informações de interesse coletivo, que antes ficavam restritas ao âmbito da administração pública, passam a ser acessíveis a toda a sociedade no formato de dados abertos, visando o aprimoramento da cultura da transparência, do controle social e da inovação. 

No presente caso, realizamos a coleta dos dados históricos da plataforma Consumidor.gov, por meio dos arquivos disponibilizados no website governamental do Ministério da Justiça e Segurança Pública (Dados.MJ) . 

Governança de Dados, segundo consta no Inciso VI do Art. 2º da Portaria STI/MP nº 58, de 23 de dezembro de 2016, é o conjunto de políticas, processos, pessoas e tecnologias que visam a estruturar e administrar os ativos de informação, com o objetivo de aprimorar a eficiência dos processos de gestão e da qualidade dos dados, a fim de promover eficiência operacional, bem como garantir a confiabilidade das informações que suportam a tomada de decisão.

É possível verificar que o website governamental do Ministério da Justiça e Segurança Pública estabelece padrões de qualidade de dados, garantindo a segurança e privacidade dos dados, disponibilizando arquivos no formato CSV acessíveis e compreensíveis, além de monitorar a qualidade dos dados e disponibilizar atualizações mensais. 

Com o objetivo de garantir a gestão adequada dos dados e, consequentemente, a conformidade com as políticas e regulamentação de governança de dados, realizamos a coleta de dados de forma automatizada, utilizando a linguagem Python. 

A coleta de dados automatizada permite que os dados sejam armazenados de forma consistente e padronizada, minimizando a possibilidade do armazenamento de dados incorretos ou duplicados. Realizamos o armazenamento dos dados no serviço em nuvem S3 da Amazon, seguindo os seguintes passos:

1º) Criação de um arquivo Excel (caminho-dados-hisoricos.xlsx) contendo os endereços dos dados disponibilizados no website Dados.MJ, com o objetivo de ser lido para ser lido por um script Python.  
![image](https://user-images.githubusercontent.com/83672645/224571606-c5d738c9-3e4f-4e4a-a514-8f05b431c5b4.png)

2º) Criação do bucket “projeto-puc” no serviço S3 da AWS e da pasta “raw_db” para armazenar os dados brutos. 
![image](https://user-images.githubusercontent.com/83672645/224571623-202b6f51-adda-4a22-b752-87f8d8855a75.png)

3º) Desenvolvimento de um script Python chamado “coletadados.py” com o objetivo de coletar os dados e armazená-los na pasta raw_db do serviço S3. Para isso, o script realiza a leitura dos caminhos URL contidos no arquivo ‘caminho-dados-historicos.xlsx’.
![image](https://user-images.githubusercontent.com/83672645/224571648-9e139e14-76d2-480d-bb28-537a4d9e0219.png)

Para realizar a coleta dos dados históricos disponíveis no website governamental do Ministério da Justiça e Segurança Pública, utilizamos o módulo concurrent.futures do Python para executar as requisições de forma assíncrona. Essa técnica foi adotada com o objetivo de reduzir o tempo de espera para cada requisição, considerando que a carga histórica consta de arquivos desde o ano de 2014 até fevereiro de 2023.

Adicionamos no script a variável "status" para confirmar a coleta e o armazenamento dos arquivos no bucket. Essa variável imprime em tela o HTTPStatusCode de cada URL e atualiza o arquivo "caminho-dados-historicos.xlsx" com o código da resposta da requisição na coluna "Status".

Após a execução bem-sucedida do script "coletadados.py", todos os arquivos referentes aos dados abertos da plataforma Consumidor.gov disponibilizados no website Dados.MJ foram armazenados na pasta "raw_db" do bucket "projeto-puc" do serviço S3 da Amazon, conforme pode ser verificado abaixo:
![image](https://user-images.githubusercontent.com/83672645/224571666-29974a37-5e6e-4e51-8115-31285dbcff1b.png)

Dessa forma, adotamos práticas e políticas que asseguram a qualidade e confiabilidade no armazenamento dos dados no AWS S3, garantindo a conformidade com as regulamentações e políticas de governança de dados.

#### Referências:
Amazon Web Services Documentation. Disponível em: https://docs.aws.amazon.com/. Acesso em: 27 fev. 2023.

Lei nº 13709, de 14 de agosto de 2018, Lei Geral de Proteção de Dados.

Luiz Barbosa, Wellington, Shayer Lyra, Roberto - Governança de Dados. Enad. Módulo 1. Disponível em: https://repositorio.enap.gov.br/handle/1/5008.  Acesso em: 09 mar. 2023.

Ministério da Justiça – Plano de dados abertos. Disponível em: https://www.gov.br/mj/pt-br/acesso-a-informacao/dados-abertos/pda-mjsp-2022.pdf. Acesso em: 03 mar. 2023.

Python documentation. Disponível em: https://docs.python.org/3/library/functions.html. Acesso em: 12 mar. 2023.

