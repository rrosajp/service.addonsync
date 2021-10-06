# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: © 2016 Rob Webset
# SPDX-FileCopyrightText:  2020-2021 Peter J. Mello <admin@petermello.net>
#
# SPDX-License-Identifier: MPL-2.0
"""Invoke AddonSync as a Kodi Program add-on."""

import xbmcaddon
import xbmcgui

# Import the common settings
from resources.lib.settings import log
from resources.lib.core import AddonSync

ADDON = xbmcaddon.Addon(id="service.addonsync")
ICON = ADDON.getAddonInfo("icon")
ADDONSYNC = AddonSync()


#########################
# Main
#########################
if __name__ == "__main__":
    log("AddonSync: Started Manually")

    # Print message that we have started
    xbmcgui.Dialog().notification(
        ADDON.getLocalizedString(32001).encode('utf-8'),
        ADDON.getLocalizedString(32019).encode('utf-8'),
        ICON,
        3000,
        False
    )

    COMPLETED = ADDONSYNC.start_sync()

    # Only show the complete message if we have not shown an error
    if COMPLETED:
        xbmcgui.Dialog().notification(
            ADDON.getLocalizedString(32001).encode('utf-8'),
            ADDON.getLocalizedString(32020).encode('utf-8'),
            ICON,
            3000,
            False,
        )

    del ADDONSYNC

    log("AddonSync: End Manual Running")
