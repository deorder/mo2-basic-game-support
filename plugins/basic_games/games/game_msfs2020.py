from ..basic_game import BasicGame

from PyQt5.QtCore import QDir

import mobase
import os
import re


class MSFS2020Game(BasicGame):

    Name = "Microsoft Flight Simulator 2020 Support Plugin"
    Author = "Deorder"
    Version = "0.0.1"

    GameName = "Microsoft Flight Simulator 2020"
    GameShortName = "msfs2020"
    GameBinary = r"FlightSimulator.exe"
    GameDataPath = r"%USERPROFILE%\AppData\Roaming\Microsoft Flight Simulator\Packages\Community"
    GameSteamId = [1250410]

    def dataDirectory(self) -> QDir:
        # Find and use package path specified in Asobo engine options        
        AppDataPath = os.path.expandvars(r"%APPDATA%\Microsoft Flight Simulator")
        UserCfgPath = os.path.join(AppDataPath, "UserCfg.opt")
        InstalledPackagesPathPattern = re.compile("InstalledPackagesPath\s*=\s*\"(.*)\"", re.IGNORECASE)
        with open(UserCfgPath, newline='') as f:
            for _, line in enumerate(f):
                for match in re.finditer(InstalledPackagesPathPattern, line):
                    return QDir(os.path.join(match.group(), "Community"))
        return QDir(os.path.join(AppDataPath, "Packages", "Community"))
