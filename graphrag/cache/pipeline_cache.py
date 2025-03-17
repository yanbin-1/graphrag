# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""A module containing 'PipelineCache' model."""

from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import Any


class PipelineCache(metaclass=ABCMeta):
    """Provide a cache interface for the pipeline."""

    @abstractmethod
    async def get(self, key: str) -> Any:
        """Get the value for the given key.

        Args:
            key (str): The key to get the value for.

        Returns:
            Any: The value for the given key.
        """

    @abstractmethod
    async def set(self, key: str, value: Any, debug_data: dict | None = None) -> None:
        """Set the value for the given key.

        Args:
            key (str): The key to set the value for.
            value (Any): The value to set.
            debug_data (dict | None, optional): Optional debugging data.
        """

    @abstractmethod
    async def has(self, key: str) -> bool:
        """Return True if the given key exists in the cache.

        Args:
            key (str): The key to check for.

        Returns:
            bool: True if the key exists in the cache, False otherwise.
        """

    @abstractmethod
    async def delete(self, key: str) -> None:
        """Delete the given key from the cache.

        Args:
            key (str): The key to delete.
        """

    @abstractmethod
    async def clear(self) -> None:
        """Clear the cache."""

    @abstractmethod
    def child(self, name: str) -> PipelineCache:
        """Create a child cache with the given name.

        Args:
            name (str): The name to create the sub cache with.
        """