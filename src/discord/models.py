# https://discord.com/developers/docs/developer-tools/game-sdk#activitytimestamps-struct

from __future__ import annotations

from datetime import datetime  # noqa: TC003

from pydantic import BaseModel

from src.discord.enums import ActivityType  # noqa: TC001


class DiscordUser(BaseModel):
    """
    ```
    id: int
    username: str
    discriminator: str
    avatar: str
    bot: bool
    ```

    Discord Documentation
    ---
    id: the user's id
    username: their name
    discriminator: the user's unique discrim
    avatar: the hash of the user's avatar
    bot: if the user is a bot user
    """

    id: int
    username: str
    discriminator: str
    avatar: str
    bot: bool


class Activity(BaseModel):
    """
    ```
    app_id: int | None
    name: str | None
    type: ActivityType | None
    state: str | None
    details: str | None
    party: ActivityPartyData | None
    timing: ActivityTimingData | None
    large_image: ActivityAsset | None
    small_image: ActivityAsset | None
    secrets: ActivitySecrets | None
    button_primary: ActivityButtonData | None
    button_secondary: ActivityButtonData | None
    ```

    Discord Documentation
    ---
    app_id: your application id - this is a read-only field
    name: name of the application - this is a read-only field
    type: What the player is doing (e.g., "Playing", "Watching", "Listening")
    details: what the player is currently doing
    state: the player's current party status
    timestamps:
    assets:
    party:
    secrets:
    instance:

    Example Rich Presence Activity
    ---

    """

    app_id: int | None
    name: str | None
    type: ActivityType | None
    details: str | None
    state: str | None
    timestamps: ActivityTimestamps | None
    assets: ActivityAssets | None
    party: ActivityParty | None
    secrets: ActivitySecrets | None
    instance: bool | None
    buttons: list[ActivityButton | None]


# NOTE: Discord: ActivityParty Struct, PartySize Struct
class ActivityParty(BaseModel):
    """
    ```
    id: int | None
    current_size: int | None
    max_size: int | None
    ```

    Discord Documentation
    ---
    id: a unique identifier for this party
    current_size: the current size of the party
    max_size: the max possible size of the party

    Notes
    ---
    The Discord API docs define a field, ActivityParty.size, which is a PartySize struct.
    The current_size and max_size fields are fields of the PartySize struct.
    However, we directly embed those fields here for brevity.
    """

    id: int | None
    current_size: int | None
    max_size: int | None


class ActivityTimestamps(BaseModel):
    """
    ```
    start: datetime | None
    end: datetime | None
    paused_at: datetime | None
    elapsed: int | None
    ```

    paused_at: used to track when an activity is still running, but became considered idle
    elapsed: used to track the total, non-paused/idle time

    Discord Documentation
    ---
    starts: unix timestamp - send this to have an "elapsed" timer
    ends: unix timestamp - send this to have a "remaining" timer

    Notes
    ---
    The paused_at and elapsed fields are not part of the Discord API
    """

    # WARN: The start and end times must be sent to the Discord API as unix timestamps
    start: datetime | None
    end: datetime | None  # Used for a remaining timer
    # WARN: BELOW IS NOT PART OF THE DISCORD API
    paused_at: datetime | None
    elapsed: int | None  # Number of seconds, not counting paused time
    # TODO: Add a way to track subelapsed/checkpoint times
    # Eg. time working on entire project vs time editing this specific file


class ActivityAssets(BaseModel):
    """
    ```
    large_image: str | None
    large_text: str | None
    large_url: str | None
    small_image: str | None
    small_text: str | None
    small_url: str | None
    ```

    Discord Documentation
    ---
    large_image: Activity asset images are arbitrary strings which usually contain snowflake IDs or prefixed image IDs
    large_text: Text displayed when hovering over the large image of the activity
    large_url: URL that is opened when clicking on the large image
    small_image: Activity asset images are arbitrary strings which usually contain snowflake IDs or prefixed image IDs
    small_text: Text displayed when hovering over the small image of the activity
    small_url: URL that is opened when clicking on the small image
    """

    large_image: str | None  # TODO: Find correct type(s) (can be static image or gif)
    large_text: str | None
    large_url: str | None
    small_image: str | None  # TODO: Find correct type(s) (can be static image or gif)
    small_text: str | None
    small_url: str | None


class ActivitySecrets(BaseModel):
    """
    ```
    match: str | None
    join: str | None
    spectate: str | None
    ```

    Discord Documentation
    ---
    match: unique hash for the given match context
    join: unique hash for chat invites and Ask to Join
    spectate: unique hash for Spectate button
    """

    match: str | None
    join: str | None
    spectate: str | None


# NOTE: Discord: ? Struct
class ActivityButton(BaseModel):
    """
    ```
    label: str | None
    url: str | None
    ```

    label: Text shown on the button (1-32 characters)
    url: URL opened when clicking the button (1-512 characters)
    """

    label: str | None
    url: str | None  # TODO: validate url or use a URL wrapper type?
