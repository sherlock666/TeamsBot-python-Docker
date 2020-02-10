# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from os import environ


class DefaultConfig:
    """ Bot Configuration """

    PORT: int = 3978
    APP_ID: str = environ.get("MicrosoftAppId", "e30b319d-8b5e-4f2b-9cf6-8078fb398310")
    APP_PASSWORD: str = environ.get("MicrosoftAppPassword", "4/-pOrU3EehecuP9mmYWd0/NmrvevWZ?")
