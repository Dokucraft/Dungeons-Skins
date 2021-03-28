@echo off
::Cape Automation
::python "Scripts/Main.py" '' 2 Test '' ''
::Skin Automation
::python "Scripts/Main.py" 1 1 Test Steve 2
::Normal Run
python "Scripts/Main.py" '' '' '' '' ''
::Argument 1: Skin Format (1 = JavaSteve, 2 = JavaAlex)
::Argument 2: Skin or Cape (1 = Skin, 2 = Cape)
::Argument 3: Requester Name (String)
::Argument 4: Skin Name (String)
::Argument 5: Include Eyes? (1 = Yes, 2 = No)
pause