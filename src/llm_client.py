"""
LLM API client configuration for chat completions.
Supports DeepSeek API and Microsoft Azure OpenAI.
Use environment variables to choose provider and credentials.
"""

import os


def get_llm_config():
    """
    Return (api_url, headers, model_for_payload) for the configured LLM provider.

    - Azure OpenAI: set AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_KEY, AZURE_OPENAI_DEPLOYMENT.
      Optional: AZURE_OPENAI_API_VERSION (default 2024-02-15-preview).
      For Azure, model_for_payload is None (deployment is in URL); do not add "model" to request body.
    - DeepSeek (default): set DEEPSEEK_API_KEY. api_url and model "deepseek-chat" are used.
    """
    endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT", "").strip()
    api_key_azure = os.environ.get("AZURE_OPENAI_API_KEY", "").strip()
    deployment = os.environ.get("AZURE_OPENAI_DEPLOYMENT", "").strip()

    if endpoint and api_key_azure and deployment:
        # Azure OpenAI
        base = endpoint.rstrip("/")
        api_version = os.environ.get("AZURE_OPENAI_API_VERSION", "2024-02-15-preview").strip()
        api_url = f"{base}/openai/deployments/{deployment}/chat/completions?api-version={api_version}"
        headers = {
            "api-key": api_key_azure,
            "Content-Type": "application/json",
        }
        # Azure uses deployment in URL; omit "model" in body or some services accept it
        model_for_payload = None
        return api_url, headers, model_for_payload

    # DeepSeek (default)
    api_key = os.environ.get("DEEPSEEK_API_KEY", "").strip()
    if not api_key:
        raise ValueError(
            "Set DEEPSEEK_API_KEY for DeepSeek, or AZURE_OPENAI_ENDPOINT + AZURE_OPENAI_API_KEY + AZURE_OPENAI_DEPLOYMENT for Azure OpenAI."
        )
    api_url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    model_for_payload = "deepseek-chat"
    return api_url, headers, model_for_payload


def build_chat_payload(messages, temperature=0.0, model_for_payload=None, **extra):
    """
    Build request body for chat completions.
    If model_for_payload is None (Azure), "model" is not included.
    """
    payload = {
        "temperature": temperature,
        "messages": messages,
    }
    if model_for_payload is not None:
        payload["model"] = model_for_payload
    payload.update(extra)
    return payload
