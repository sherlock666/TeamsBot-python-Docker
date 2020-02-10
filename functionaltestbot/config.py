#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os


class DefaultConfig:
    """ Bot Configuration """

    PORT = 443
    APP_ID = os.environ.get("MicrosoftAppId", "e30b319d-8b5e-4f2b-9cf6-8078fb398310")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "4/-pOrU3EehecuP9mmYWd0/NmrvevWZ?")
