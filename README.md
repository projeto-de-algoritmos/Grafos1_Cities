# Turista
# Acesse a aplicação pelo badge! 
# 👇🏽
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/projeto-de-algoritmos/Grafos1_Turista/master?urlpath=%2Fvoila%2Frender%2Fapp.ipynb)

---

**Número da Lista**: 1<br>
**Conteúdo da Disciplina**: Grafos 1<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 17/0138798  |  Caio Fernandes |
| 17/0050939  |  Lucas Dutra    |

## Sobre 
Turista é uma aplicação para quem quer fazer viagens internacionais sem apreciando a paisagem de cada país! Insira o país de origem e o país de destino e descubra a melhor rota para sua viagem!  

## Screenshots
### Grafo total 🙂
![total_graph](img/all_graph.jpg)
### Sucesso na busca 🙂
Países alcançáveis
![success](img/success.jpg)
### Falha na busca ☹️
Países não alcançáveis
![fail](img/fail.jpg)

## Instalação 
**Linguagem**: Python<br>
É necessário a instalação dos seguintes pacotes: **Python**, **pip** e **virtualenv** (opcional) para instalação do projeto.
### Instalação dos recursos necessários
1. Instalação do gerenciador de pacote `python pip`<br>
    ```$ sudo apt-get install python3-pip```
2. Instalação do `python virtual environment`<br>
    ```$ sudo apt-get install python3-venv```

### Criação do virtualenv (altamente recomendado)
1. Crie seu ambiente virtual python  
    ```$ python3 -m venv venv ```  
2. Execute o ambiente virtual criado  
    ```$ source venv/bin/activate```  
3. Para desativar o ambiente virtual após execução do projeto   
    ```$ deactivate```
### Execução do projeto
1. Instale as biblioteca necessárias  
    ```$ pip3 install -r requirements.txt```
2. Execute o script de pré-processamento dos dados  
    ```$ python main.py run```
3. Habilite os widget em seu notebook  
    ```$ jupyter nbextension enable --py --user widgetsnbextension```
4. Execute o notebook juntamente com o `voila`  
   ```$ voila --enable_nbextensions=True```
5. A interface de interação com o usuário final abrirá em seu navegador padrão  
6. Acesse o arquivo `App.ipynb` para interagir com a aplicação

## Uso 

### Vídeo explicativo
[Aqui](https://github.com/projeto-de-algoritmos/Grafos1_Turista/blob/master/app.mp4)

### Para acessar o deploy da aplicação, COM TODOS OS RECURSOS clique no badge abaixo:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/projeto-de-algoritmos/Grafos1_Turista/master?urlpath=%2Fvoila%2Frender%2Fapp.ipynb)

### Caso queira consultar o código:
- Após execução do comando **3.** 
- Acessar localmente:
  - Subir o servidor do jupyter-notebook  
  `$ jupyter-notebook --NotebookApp.token=""`
  - Acessar a seguinte url:  
  `http://localhost:8888/notebooks/Grafos1_Cities.ipynb`
  - Para o script de pré-processamento:  
  `$ {editor de sua preferência} main.py`
  
- Acessar no repositório:
  - Acessar: [script de pré-processamento](https://github.com/projeto-de-algoritmos/Grafos1_Turista/blob/master/main.py) e [lógica da interface](https://github.com/projeto-de-algoritmos/Grafos1_Turista/blob/master/main.py)

## Outros 
<p>Neste projeto foram utilizadas fontes diferentes de dados, retiradas do <a href="https://www.kaggle.com/">kaggle</a>. A <a href="https://www.kaggle.com/resheto/country-borders">primeira</a>, consistia em, basicamente, a maioria dos países de todos os continentes associados às suas fronteiras. A <a href="https://www.kaggle.com/tomvebrcz/countriesandcontinents">segunda</a>, possui a lista da maioria dos países associada aos respectivos continentes.</p>

<p>Porém, ambos os dados apresentavam algumas incosistências como repetição desnecessária de variáveis e padrões nominais desatualizados. Para otimização da utilidade dessas fontes, foi necessário a aplicação de técnicas de pré-processamento, usando como suporte a biblioteca de manipulação de dados <a href="https://pandas.pydata.org/">pandas</a> e, também, a biblioteca <a href="https://metaflow.org/">Metaflow</a>, originalmente desenvolvida na Netflix para aumentar a produtividade dos cientistas de dados que trabalham em uma grande variedade de projetos, desde estatísticas clássicas até state-of-the-art deep learning.</p>

<p>Além disso, criamos um novo dataset, proveniente do cruzamento de dados de ambas a fontes citadas anteriormente.</p>
