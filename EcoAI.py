import os
from dotenv import load_dotenv
import google.generativeai as genai

# Carregar variáveis do arquivo .env
load_dotenv()

# Pega a chave da variável de ambiente
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("A chave API_KEY não foi encontrada no arquivo .env")

# Configurar a API do Gemini com a chave
genai.configure(api_key=API_KEY)

# Listar modelos disponíveis (opcional, para saber qual usar)
print("Modelos disponíveis:")
for m in genai.list_models():
    print(f"- {m.name} (métodos: {m.supported_generation_methods})")

# Escolha do modelo que suporta generateContent (ajuste conforme o output acima)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

def analisar_especie(nome_cientifico, bioma):
    prompt = f"""
    Você é um especialista em conservação. Me forneça um relatório técnico resumido sobre:
    - Nome científico: {nome_cientifico}
    - Bioma: {bioma}
    Inclua: Status de conservação (IUCN), principais ameaças, importância ecológica e ações de preservação no Brasil.
    Responda em tópicos.
    """
    resposta = model.generate_content(prompt)
    return resposta.text

if __name__ == "__main__":
    nome_cientifico = "Panthera onca"
    bioma = "Mata Atlântica"

    relatorio = analisar_especie(nome_cientifico, bioma)

    print("\nRelatório gerado:\n")
    print(relatorio)
