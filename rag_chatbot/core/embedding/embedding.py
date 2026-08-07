import os
import requests
from llama_index.embeddings.openai import OpenAIEmbedding
from ...setting import RAGSettings
from dotenv import load_dotenv


load_dotenv()


class LocalEmbedding:
    @staticmethod
    def set(setting: RAGSettings | None = None, model_name: str | None = None, **kwargs):
        setting = setting or RAGSettings()
        model_name = model_name or setting.ingestion.embed_llm
        api_base = os.getenv("OPENAI_API_BASE", setting.ollama.openai_api_base)
        api_key = os.getenv("OPENAI_API_KEY", setting.ollama.openai_api_key)

        if not model_name or model_name.startswith("text-embedding") or model_name.startswith("gpt-") or "openai" in model_name.lower():
            return OpenAIEmbedding(
                model=model_name or "text-embedding-3-large",
                api_base=api_base,
                api_key=api_key,
                embed_batch_size=setting.ingestion.embed_batch_size,
            )
        try:
            import torch
            from llama_index.embeddings.huggingface import HuggingFaceEmbedding
            from transformers import AutoModel, AutoTokenizer

            return HuggingFaceEmbedding(
                model=AutoModel.from_pretrained(
                    model_name, torch_dtype=torch.float16, trust_remote_code=True
                ),
                tokenizer=AutoTokenizer.from_pretrained(
                    model_name, torch_dtype=torch.float16
                ),
                cache_folder=os.path.join(os.getcwd(), setting.ingestion.cache_folder),
                trust_remote_code=True,
                embed_batch_size=setting.ingestion.embed_batch_size,
            )
        except Exception:
            return OpenAIEmbedding(
                model=model_name,
                api_base=api_base,
                api_key=api_key,
                embed_batch_size=setting.ingestion.embed_batch_size,
            )

    @staticmethod
    def pull(host: str, **kwargs):
        setting = RAGSettings()
        payload = {"name": setting.ingestion.embed_llm}
        return requests.post(f"http://{host}:11434/api/pull", json=payload, stream=True)

    @staticmethod
    def check_model_exist(host: str, **kwargs) -> bool:
        setting = RAGSettings()
        data = requests.get(f"http://{host}:11434/api/tags").json()
        list_model = [d["name"] for d in data["models"]]
        if setting.ingestion.embed_llm in list_model:
            return True
        return False
