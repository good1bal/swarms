"""Swarms - A framework for orchestrating multi-agent AI systems.

This package provides tools and abstractions for building, managing,
and deploying swarms of AI agents that can collaborate to solve
complex tasks.

Example:
    >>> from swarms import Agent, SwarmRouter
    >>> agent = Agent(agent_name="MyAgent", model_name="gpt-4o")
    >>> router = SwarmRouter(agents=[agent])
"""

from swarms.agents.agent import Agent
from swarms.structs.swarm_router import SwarmRouter
from swarms.structs.sequential_workflow import SequentialWorkflow
from swarms.structs.concurrent_workflow import ConcurrentWorkflow
from swarms.structs.mixture_of_agents import MixtureOfAgents
from swarms.utils.loguru_logger import initialize_logger

__version__ = "7.0.0"
__author__ = "Kye Gomez"
__license__ = "MIT"

logger = initialize_logger(log_folder="swarms")

__all__ = [
    # Core agent
    "Agent",
    # Swarm structures
    "SwarmRouter",
    "SequentialWorkflow",
    "ConcurrentWorkflow",
    "MixtureOfAgents",
    # Utilities
    "logger",
    # Metadata
    "__version__",
    "__author__",
    "__license__",
]
