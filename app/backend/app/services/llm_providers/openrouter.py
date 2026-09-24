import httpx

from .base import LLMProvider, LLMProviderError

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


class OpenRouterProvider(LLMProvider):
    def __init__(self, api_key: str, model: str, timeout_seconds: float = 60.0):
        self._api_key = api_key
        self._model = model
        self._timeout_seconds = timeout_seconds

    @property
    def model_id(self) -> str:
        return self._model

    async def complete(self, system_prompt: str, user_prompt: str) -> str:
        headers = {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json",
        }
        body = {
            "model": self._model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        }
        try:
            async with httpx.AsyncClient(timeout=self._timeout_seconds) as client:
                response = await client.post(OPENROUTER_URL, headers=headers, json=body)
        except httpx.HTTPError as exc:
            raise LLMProviderError(f"Couldn't reach OpenRouter: {exc}") from exc

        if response.status_code >= 400:
            # OpenRouter puts the real reason (rate limit detail, invalid model, etc.) in the
            # body — the bare status code alone ("429 Too Many Requests") doesn't say why.
            raise LLMProviderError(f"OpenRouter {response.status_code}: {response.text}")

        try:
            data = response.json()
            return data["choices"][0]["message"]["content"]
        except (KeyError, IndexError, ValueError) as exc:
            raise LLMProviderError(f"OpenRouter returned an unexpected response: {exc}") from exc
