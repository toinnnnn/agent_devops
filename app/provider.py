import os
import asyncio
from dotenv import load_dotenv
from openai import OpenAI

# Carrega variáveis do arquivo .env
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

if not OPENAI_API_KEY:
    raise RuntimeError("Set OPENAI_API_KEY in environment (.env)")

# Cria o cliente da nova API
client = OpenAI(api_key=OPENAI_API_KEY)

# Função assíncrona para chamar o modelo
async def call_ai(prompt: str, system: str | None = None, max_completion_tokens: int = 1000):
    def sync_call():
         # Concatena system + user manualmente
        if system:
            full_input = f"SYSTEM:\n{system}\n\nUSER:\n{prompt}"
        else:
            full_input = prompt

        resp = client.responses.create(
            model=MODEL,
            input=full_input,
        )
        
        if hasattr(resp, "output_text") and resp.output_text:
            return resp.output_text.strip()

        # Nova estrutura: resp.output[0].content[0].text
        if hasattr(resp, "output"):
            try:
                return resp.output[0].content[0].text.strip()
            except:
                pass

        return ""

    # Executa em thread separada para não travar o event loop
    return await asyncio.to_thread(sync_call)
