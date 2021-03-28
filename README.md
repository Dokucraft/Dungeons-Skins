# Dungeons-Skins
Scripts to Convert a Java Skin to a Dungeons Mod using Python

## Requirements

Python 3.8+

> python -m pip install --upgrade pip

> python -m pip install --upgrade Pillow

## Setup

Set Paths in Scripts/settings

* editor_directory.txt *Path to Editor*

* game_directory.txt *Path to Mods Folder*

* skins_directory.txt *Path to local Repository*

## Instructions

Place Skin into Skin/Skin with any name, 1 Skin at a time

Skins have to be either 64x32, or 64x64

Place Cape into Skin/Cape with any name, 1 Cape at a time

Capes have to be 32x32, 64x64, 22x17, 44x34, 46x22, or 92x44

Run Package Skin.bat

### Automation Settings in Package Skin.bat

**Cape Automation**

> python "Scripts/Main.py" '' 2 Test '' ''

**Skin Automation**

> python "Scripts/Main.py" 1 1 Test Steve 2

**Manual Run**

> python "Scripts/Main.py" '' '' '' '' ''

> Argument 1: Skin Format (1 = JavaSteve, 2 = JavaAlex)
> 
> Argument 2: Skin or Cape (1 = Skin, 2 = Cape)
> 
> Argument 3: Requester Name (String)
> 
> Argument 4: Skin Name (String)
> 
> Argument 5: Include Eyes? (1 = Yes, 2 = No)
