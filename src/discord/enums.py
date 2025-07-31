from __future__ import annotations

from enum import Enum


class ActivityType(Enum):
    """
    ```
    PLAYING = 0
    STREAMING = 1
    LISTENING = 2
    WATCHING = 3
    CUSTOM = 4
    COMPETING = 5
    ```
    """

    PLAYING = 0
    STREAMING = 1
    LISTENING = 2
    WATCHING = 3
    CUSTOM = 4
    COMPETING = 5


class ActivityJoinRequestReply(Enum):
    """
    ```
    NO = 0
    YES = 1
    IGNORE = 2
    ```
    """

    NO = 0
    YES = 1
    IGNORE = 2


class ActivityActionType(Enum):
    """
    ```
    JOIN = 0
    SPECTATE = 1
    ```
    """

    JOIN = 0
    SPECTATE = 1
