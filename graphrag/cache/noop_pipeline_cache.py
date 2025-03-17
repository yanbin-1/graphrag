# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""Module containing the NoopPipelineCache implementation."""

from typing import Any

from graphrag.cache.pipeline_cache import PipelineCache


class NoopPipelineCache(PipelineCache):
    """A no-op implementation of the pipeline cache, usually useful for testing."""

    async def get(self, key: str) -> Any:
        """Get the value for the given key.

        Args:
            key: The key to get the value for.

        Returns
        -------
            The value for the given key.
        """
        return None

    async def set(
        self, key: str, value: str | bytes | None, debug_data: dict | None = None
    ) -> None:
        """Set the value for the given key.

        Args:
            key: The key to set the value for.
            value: The value to set.
            debug_data: Optional debug data to be associated with the value.
        """

    async def has(self, key: str) -> bool:
        """Return True if the given key exists in the cache.

        Args:
            key: The key to check for.

        Returns
        -------
            True if the key exists in the cache, False otherwise.
        """
        return False

    async def delete(self, key: str) -> None:
        """Delete the given key from the cache.

        Args:
            key: The key to delete.
        """

    async def clear(self) -> None:
        """Clear the cache."""

    def child(self, name: str) -> PipelineCache:
        """Create a child cache with the given name.

        Args:
            name: The name to create the sub cache with.

        Returns
        -------
            A child instance of the PipelineCache.
        """
        return self
