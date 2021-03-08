
## Asetto Corsa

Most AC mods use the game directory as their root. If not, create the parent folders yourself and move the directory in there during mod installation.
Instead of using the official Assetto Corsa executable consider using the Content Manager which can be downloaded / bought at: https://assettocorsa.club/content-manager.html
The Content Manager (which is then to be started via MO2) + the Custom Shader Patch will change Asetto Corsa in a modern and in my opinion one of the best racing games. The Content Manager does not have a good mod manager yet (Ilya is working on one), but meanwhile this will help you to install Assetto Corsa mods in a non-destructive way and keep track of versioning and add notes (download location etc.).
When using the Content Manager do not forget to install the track, car updates once in a while from inside the Custom Shader Patch and opening the '...' context menus. This will improve the tracks & cars by making them use the new features added by the Custom Shader Patch.

## Beam.NG Drive

Many Beam.NG mods are to be installed inside the `<Documents>/BeamNG.drive/mods` folder. This will use Beam.NG's own mod system. Very often the official mod system is not good enough and other files outside of the `mods` folder require to be changes. MO2 will enable us to do this in a non-destructive way. If you want to install a mod that has to be installed inside the `mods` folder you can just create an new mod inside MO2, add a `mods` folder and move the zip file in there. MO2's overwrite feature will take care of any files generated by Beam.NG while keeping the original folders clean.

## Beat Saber (Still have to test this one, let me know if it works)

Most Beat Saber mods are to be installed relative to the game's root directory. There is also an semi-official mod manager called Mod Assistant, but I prefer to use MO2 and enjoy its benefits. You may want to run the IPA (injector) outside of MO2, but it should work from inside MO2 as well with the benefit that it will add all modified files to the overwrite folder, not touching the original folder.

## Microsoft Flight Simulator 2020

Microsoft Flight Simulator uses a `Packages` folder where all extra content of the game is installed. This custom game support plugin assumes that the packages are installed in `%USERPROFILE%\AppData\Roaming\Microsoft Flight Simulator\Packages`, which is the default location. If you chose a different location you can achieve the same effect by letting MSFS2020 use the default location again and then move the `Official` folder to its own mod by creating an new mod inside MO2 that you could call `Official Packages`. When you install a community package you will have to make sure they are placed relative to the `Community` folder, for example:

The official packages:
`<Mod Organizer Folder>\mods\Official Packages\Official\*`

An example community package:
`<Mod Organizer Folder>\mods\FlybyWireSim A32NX\Community\A32NX\*`

When MSFS2020 updates their official packages you may want to move the updated files from the `overwrite` folder to the `Official Packages` mod.

## X-Plane 11

Many X-Plane 11 modifications are to be installed relative to the game's root directory. By using MO2 we can install many of the mods that tend to overwite official files in an non-destructive way. Of course do not forget to update the official files once in a while by using the official launcher.