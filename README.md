# EcoAI

# 🐾 Relatório de Espécies com Gemini AI
Projeto desenvolvido para gerar relatórios automatizados sobre espécies da biodiversidade brasileira, integrando a API do Gemini AI com Python. O sistema analisa informações biológicas e ecológicas e gera relatórios em Markdown para facilitar a divulgação científica e educação ambiental.

# 🌿 Sobre o Projeto
Este projeto utiliza Inteligência Artificial Generativa para criar relatórios descritivos de espécies a partir de seus nomes científicos e do bioma onde ocorrem. É ideal para estudantes, pesquisadores e educadores que desejam automatizar a produção de conteúdo biológico.

# 🚀 Funcionalidades
✅ Análise automatizada de espécies (nome científico + bioma).
✅ Geração de relatórios em formato .md (Markdown).
✅ Fácil integração com Google Colab.
✅ Possibilidade de expansão para outros biomas e grupos de organismos.
✅ Código limpo e comentado, pronto para reuso.

# 🛠️ Tecnologias Utilizadas
Python 3.x

Google Generative AI (Gemini 1.5 ou 2.0)

Biblioteca google-generativeai

Google Colab (execução recomendada)

# 📦 Como Executar no Google Colab
Clone ou copie o código deste projeto para seu Google Colab.

Instale as dependências:

python
Copiar
Editar
!pip install google-generativeai
Configure sua API KEY do Gemini:

python
Copiar
Editar
import os
import google.generativeai as genai

os.environ["GOOGLE_API_KEY"] = "SUA-API-KEY-AQUI"  # coloque sua API Key aqui
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
Rode a função de análise:

python
Copiar
Editar
def analisar_especie(nome_cientifico, bioma):
    prompt = f"Crie um relatório detalhado sobre a espécie '{nome_cientifico}' que ocorre no bioma '{bioma}', incluindo aspectos ecológicos, comportamento e conservação."
    modelo = genai.GenerativeModel("gemini-1.5-flash")  # ou gemini-2.0-flash se preferir
    resposta = modelo.generate_content(prompt)
    return resposta.text
Gere seu relatório:

python
Copiar
Editar
nome_cientifico = "Panthera onca"
nome_comum = "Onça-pintada"
bioma = "Mata Atlântica"

relatorio = analisar_especie(nome_cientifico, bioma)
print(relatorio)
Salve o relatório como Markdown (.md):

python
Copiar
Editar
with open("relatorio_onca_pintada.md", "w", encoding="utf-8") as file:
    file.write(f"# Relatório: {nome_comum} ({nome_cientifico})\n\n")
    file.write(relatorio)
 # 📊 Exemplo de Resultado
nginx
Copiar
Editar
# Relatório: Onça-pintada (Panthera onca)

A onça-pintada é o maior felino das Américas e um predador de topo nos ecossistemas onde ocorre. Na Mata Atlântica, desempenha papel crucial no equilíbrio ecológico (...relatório completo gerado pela IA...)
