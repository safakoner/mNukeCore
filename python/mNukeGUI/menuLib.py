#
# Copyright 2020 Safak Oner.
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------
## @file    mNukeGUI/menuLib.py @brief [ FILE ] - Operate on menus in Nuke.
## @package mNukeGUI.menuLib    @brief [ FILE ] - Operate on menus in Nuke.


#
# ----------------------------------------------------------------------------------------------------
# IMPORT
# ----------------------------------------------------------------------------------------------------
import nuke

import mApplication.applicationInfoAbs
import mApplication.parentApplicationLib


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief This function creates menus in Nuke based on the application info classes available in PYTHONPATH.
#
#  @see mApplication.applicationInfoAbs.ApplicationInfo
#
#  @exception N/A
#
#  @return None - None
def initializeMenus():

    applicationList = mApplication.applicationInfoAbs.ApplicationInfo.list()
    if not applicationList:
        return

    for app in applicationList:

        menuPath = app.fullMenuPath()
        if not menuPath:
            continue

        if not mApplication.parentApplicationLib.Application.kNuke in app.parentApplications() and not \
                mApplication.parentApplicationLib.Application.kAll in app.parentApplications():
            continue

        nuke.menu('Nuke').addCommand(menuPath, app.pythonCommand(), icon=app.getIconFileAbsolutePath())
