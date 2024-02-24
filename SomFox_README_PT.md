# Projeto SomFox: Visualizador de Som Dinâmico {style="display: block; margin: 0 auto;"}

![SomFox](https://raw.githubusercontent.com/FoxPopBR/SomFox/main/asset/SomFox.jpg){width=500px height=500px style="display: block; margin: 0 auto;"}

## &nbsp; O SomFox é um aplicativo projetado para transformar áudio captado em tempo real pelo microfone em uma experiência visual interativa e envolvente

## &nbsp; Este visualizador de som se destaca por criar uma faixa de fileiras de blocos personalizável que se iluminam e se movem em harmonia com as ondas sonoras captadas, funcionando como um equalizador visual do som ambiente

### Características Principais

**Menu Superior de Ajustes:** Localizado no canto superior esquerdo, podemos encontrar um conjunto de input que permite ao usuário modificar configurações básicas para personalizar a experiência visual.

**Visualizador Sonoro:** No centro da janela encontramos o visualizador de som. Composto por pequenos blocos quadrados em uma grade separando os blocos.

- A quantidade de blocos que contem em uma fileira vertical pode ser personalizado.
- A quantidade de fileiras de blocos pode ser personalizada.

Configurações de Visualização:

- Tamanho dos Blocos: Ajusta as dimensões dos blocos para uma visualização mais detalhada ou mais ampla.
- Quantidade de Fileiras: Permite alterar a altura e a quantidade de fileiras verticais, ajustando a densidade da visualização.
- Ajustes de Grid: Configurações de espessura e cor do grid, oferecendo mais opções de personalização visual.
- FPS (Frames Por Segundo): Ajuste da taxa de atualização da animação, permitindo uma visualização fluida e sincronizada com o áudio.
- Futuras Expansões
- Variações de Animação: Introdução de novos modos de visualização para representar o som captado, enriquecendo a experiência do usuário.
- Personalização Avançada: Inclusão de opções detalhadas de personalização, como escolha de cores e padrões de animação para o equalizador visual.
- Estilos pré configurados de visualização para escolher ou salvar.

**Objetivo**
O objetivo do SomFox é oferecer uma nova maneira de interagir com o som, transformando áudio em arte visual. Busca-se proporcionar não apenas entretenimento, mas também uma ferramenta útil para análise e apreciação de áudio em diferentes contextos.

## &nbsp; Organização do Projeto SomFox

- repositório: <https://github.com/FoxPopBR/SomFox>
- Criado um Ambiente Virtual Conda: Jarvis_Alfa_1.0.0
- conda --version conda 23.7.4
- python --version Python 3.10.13

<details>
  <summary>Clique para Lista Dependências </summary>
<pre>
pyaudio==0.2.14
json==2.16.2
ast==0.7.12
pygame_gui==0.6.9
pathlib==1.0.1
numpy==1.26.2
pygame==2.5.2
os==1.2.0
re==2.7.0
</pre>
</details>

<details>
  <summary>Clique aqui para Arvore de arquivos do código</summary>
<pre>
🗃️ SomFox/
├── 🌐 index.html
├── ☕ audio-visualizer.js
├── 📄 dados.json
├── 📝 SomFox_README_PT.md
├── 📝 project_structure.md
├── 📝 showtree.md
├── 🎵 respect.mp3
├── 🐍 main.py
├── 🐍 project_directory.py
├── 🐍 teste.py
├── 🐍 tree.py
├── 📝 bibliotecas_utilizadas.txt
├── 📝 conda_list.txt
├── 📝 list.txt
├── 📝 pip_list.txt
├── 📝 requirements.txt
├── 🗺️ asset/
│   ├── 🖼️ SomFox.jpg
│   └── Standard DALL·E.webp
└── 🛠️ modules/
    ├── 🐍 __init__.py
    ├── 🐍 config.py
    └── 🐍 treemaker.py
</pre>
</details>