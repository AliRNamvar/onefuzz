#!/usr/bin/env python
#
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import logging

import azure.functions as func
from onefuzztypes.enums import VmState

from ..onefuzzlib.proxy import Proxy


def main(mytimer: func.TimerRequest) -> None:  # noqa: F841
    for proxy in Proxy.search():
        if not proxy.is_used():
            logging.info("stopping proxy")
            proxy.state = VmState.stopping
            proxy.save()
