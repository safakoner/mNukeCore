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
## @file    mNukeCore/packageEnvLib.py @brief [ FILE   ] - Package environment module.
## @package mNukeCore.packageEnvLib    @brief [ MODULE ] - Package environment module.


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from    os.path import join

from    json import loads


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief Set environment.
#
#  @param allLib            [ mMeco.libs.allLib.All                 | None | in  ] - All libraries.
#  @param envEntryContainer [ mMeco.libs.entryLib.EnvEntryContainer | None | in  ] - Env entry lib container.
#
#  @exception N/A
#
#  @return True  - If this package should be initialized.
#  @return False - If this package shouldn't be initialized.
def setEnvironment(allLib, envEntryContainer):

    if allLib.settingsOperator().appFilePath():
        _appFile = open(allLib.settingsOperator().appFilePath(), 'r')
        appData  = loads(_appFile.read())
        _appFile.close()

        if appData['application'] == 'nuke':

            envEntryContainer.addMulti('NUKE_PATH', join(envEntryContainer.getPackageRootPath(), 'python'))
            return True
    
    return False