"""Registers the internal gym envs then loads the env plugins for module using the entry point."""

from typing import Any

from gymnasium.envs.registration import make, pprint_registry, register, registry, spec