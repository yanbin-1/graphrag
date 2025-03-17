# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""A module containing 'InMemoryCache' model."""

from typing import Any

from graphrag.cache.pipeline_cache import PipelineCache


class InMemoryCache(PipelineCache):
    """In memory cache class definition."""

    _cache: dict[str, Any]
    _name: str

    def __init__(self, name: str | None = None):
        """Init method definition."""
        self._cache = {}
        self._name = name or ""

    async def get(self, key: str) -> Any:
        """Get the value for the given key.

        Args:
            key (str): The key to get the value for.

        Returns
        -------
            Any: The value for the given key or None if the key does not exist.
        """
        key = self._create_cache_key(key)
        return self._cache.get(key)

    async def set(self, key: str, value: Any, debug_data: dict | None = None) -> None:
        """Set the value for the given key.

        Args:
            key (str): The key to set the value for.
            value (Any): The value to set.
            debug_data (dict | None, optional): Additional debugging information.

        Returns
        -------
            None
        """
        key = self._create_cache_key(key)
        self._cache[key] = value

    async def has(self, key: str) -> bool:
        """Return True if the given key exists in the storage.

        Args:
            key (str): The key to check for.

        Returns
        -------
            bool: True if the key exists in the storage, False otherwise.
        """
        key = self._create_cache_key(key)
        return key in self._cache

    async def delete(self, key: str) -> None:
        """Delete the given key from the storage.

        Args:
            key (str): The key to delete.

        Returns
        -------
            None
        """
        key = self._create_cache_key(key)
        del self._cache[key]

    async def clear(self) -> None:
        """Clear the storage.

        Returns
        -------
            None
        """
        self._cache.clear()

    def child(self, name: str) -> PipelineCache:
        """Create a sub cache with the given name.

        Args:
            name (str): The name of the sub cache.

        Returns
        -------
            PipelineCache: A new instance of InMemoryCache with the specified name.
        """
        return InMemoryCache(name)

    def _create_cache_key(self, key: str) -> str:
        """Create a cache key for the given key.

        Args:
            key (str): The base key to create a cache key for.

        Returns
        -------
            str: The created cache key.
        """
        return f"{self._name}{key}"