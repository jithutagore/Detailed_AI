from abc import ABC, abstractmethod


class LLMProviderError(Exception):
    """Raised when the provider can't produce a completion (network, auth, rate limit, bad response)."""


class LLMProvider(ABC):
    @abstractmethod
    async def complete(self, system_prompt: str, user_prompt: str) -> str:
        """Returns the model's raw text response, or raises LLMProviderError."""

    @property
    @abstractmethod
    def model_id(self) -> str:
        """Identifier stored in generated_notes.model_used (e.g. the provider's model slug)."""
