import os
import requests
from llama_index.llms.openai import OpenAI
from ...setting import RAGSettings
from dotenv import load_dotenv

load_dotenv()


class LocalRAGModel:
    def __init__(self) -> None:
        pass

    @staticmethod
    def set(
        model_name: str | None = None,
        system_prompt: str | None = None,
        host: str = "host.docker.internal",
        setting: RAGSettings | None = None,
    ):
        setting = setting or RAGSettings()
        model_name = model_name or setting.ollama.llm
        api_base = os.getenv("OPENAI_API_BASE", setting.ollama.openai_api_base)
        api_key = os.getenv("OPENAI_API_KEY", setting.ollama.openai_api_key)

        if not model_name or model_name.startswith("gpt-") or model_name.startswith("text-") or "llama3" not in model_name:
            return OpenAI(
                model=model_name or "gpt-4o",
                api_base=api_base,
                api_key=api_key,
                temperature=setting.ollama.temperature,
                system_prompt=system_prompt,
            )
        else:
            from llama_index.llms.ollama import Ollama
            settings_kwargs = {
                "tfs_z": setting.ollama.tfs_z,
                "top_k": setting.ollama.top_k,
                "top_p": setting.ollama.top_p,
                "repeat_last_n": setting.ollama.repeat_last_n,
                "repeat_penalty": setting.ollama.repeat_penalty,
            }
            return Ollama(
                model=model_name,
                system_prompt=system_prompt,
                base_url=f"http://{host}:{setting.ollama.port}",
                temperature=setting.ollama.temperature,
                context_window=setting.ollama.context_window,
                request_timeout=setting.ollama.request_timeout,
                additional_kwargs=settings_kwargs,
            )

    @staticmethod
    def pull(host: str, model_name: str):
        setting = RAGSettings()
        payload = {"name": model_name}
        return requests.post(
            f"http://{host}:{setting.ollama.port}/api/pull", json=payload, stream=True
        )

    @staticmethod
    def check_model_exist(host: str, model_name: str) -> bool:
        setting = RAGSettings()
        data = requests.get(f"http://{host}:{setting.ollama.port}/api/tags").json()
        if data["models"] is None:
            return False
        list_model = [d["name"] for d in data["models"]]
        if model_name in list_model:
            return True
        return False
