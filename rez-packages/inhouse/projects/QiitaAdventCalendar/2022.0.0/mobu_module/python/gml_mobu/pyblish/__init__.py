"""Public API

Anything that isn't defined here is INTERNAL and unreliable for external use.

"""

from .pipeline import (
    install,
    uninstall,
)


__all__ = [
    "install",
    "uninstall",
]
