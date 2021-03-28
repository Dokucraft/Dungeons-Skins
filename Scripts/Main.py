from displace import displace
from shutil import copyfile
from PIL import Image
from os import path
import subprocess
import pathlib
import os.path
import shutil
import sys
import os
fileDir = os.getcwd()
fileDir = fileDir.replace('\\', '/')
fileDir = fileDir + '/'
editorSettings = fileDir + 'Scripts/settings/editor_directory.txt'
gameSettings = fileDir + 'Scripts/settings/game_directory.txt'
print(editorSettings)
print(gameSettings)
f = open(editorSettings, 'r')
editorDir = f.read()
f.close()
editorDir = editorDir + '/'
f = open(gameSettings, 'r')
gameDir = f.read()
f.close()
gameDir = gameDir + '/'
skinFolderFile = os.listdir(fileDir + 'Skin/Skin/')
skinNameDir = fileDir + 'Skin/Skin/' + skinFolderFile[0]
capeFolderFile = os.listdir(fileDir + 'Skin/Cape/')
capeNameDir = fileDir + 'Skin/Cape/' + capeFolderFile[0]
NameList = ["Hedwig", "Hex", "Valorie", "Hal", "Elaine", "Baako", "Annika", "Bediako", "Darian", "Eshe", "Esperanza", "Fuego", "Greta", "Igor", "Jade", "Mayeso", "Morris", "Neo", "Nuru", "Qamar", "Sam", "Sergey", "Shikoba", "Sven", "Violet", "Zola", "Alex", "Steve", "Wargen", "Pake", "Explorer", "Archeologist", "Winter_Warrior", "Frosty"]
def processCapeImage():
    print('Processing Normal Cape')
    capeFolderFile = os.listdir(fileDir + 'Skin/Cape/')
    capeNameDirImage = fileDir + 'Skin/Cape/' + capeFolderFile[0]
    capeImage = Image.open(capeNameDirImage).convert("RGBA")
    capeImage = capeImage.crop((0, 0, 32, 32))
    for y in range(11, 22):
        capeImage.putpixel((22, y), (255, 255, 255, 0))
    
    capeImageFull = capeImage.crop((0, 0, 32, 32))
    capeImageFull.save(capeNameDirImage)

def processOFCapeImage():
    print('Processing OptiFine Cape')
    capeFolderFile = os.listdir(fileDir + 'Skin/Cape/')
    capeNameDirImage = fileDir + 'Skin/Cape/' + capeFolderFile[0]
    capeImage = Image.open(capeNameDirImage).convert("RGBA")
    capeImage = capeImage.crop((0, 0, 64, 64))
    
    capeImage.putpixel((62, 0), (255, 255, 255, 0))
    capeImage.putpixel((63, 0), (255, 255, 255, 0))
    capeImage.putpixel((62, 1), (255, 255, 255, 0))
    capeImage.putpixel((63, 1), (255, 255, 255, 0))
    
    for x in range(44, 46):
        for y in range(22, 44):
            capeImage.putpixel((x, y), (255, 255, 255, 0))
    
    capeImageFull = capeImage.crop((0, 0, 64, 64))
    capeImageFull.save(capeNameDirImage)
    
def processSmallOFCapeImage():
    print('Processing Small OptiFine Cape')
    capeFolderFile = os.listdir(fileDir + 'Skin/Cape/')
    capeNameDirImage = fileDir + 'Skin/Cape/' + capeFolderFile[0]
    capeImage = Image.open(capeNameDirImage).convert("RGBA")
    capeImage = capeImage.crop((0, 0, 32, 32))
    
    capeImage.putpixel((31, 0), (255, 255, 255, 0))
    
    for x in range(22, 23):
        for y in range(11, 22):
            capeImage.putpixel((x, y), (255, 255, 255, 0))
    
    capeImageFull = capeImage.crop((0, 0, 32, 32))
    capeImageFull.save(capeNameDirImage)

def manageCapeFolders():
    CapeName = 'T_SinisterBlueCape'
    CapeFileName = CapeName + '.png'
    CapeSFileName = CapeName + '_S.png'
    CapeDir01 = fileDir + 'DungeonsSkins/Content/Dungeons/Content/Actors/Characters/Player/Capes/Skins/SinisterBlueCape'
    CapeDir02 = fileDir + 'DungeonsSkins/Content/Dungeons/Content/Actors/Characters/Player/Capes/Skins'
    CapeDir03 = fileDir + 'DungeonsSkins/Content/Dungeons/Content/Actors/Characters/Player/Capes'
    if path.exists(CapeDir03) == 0:
        os.mkdir(CapeDir03)
        print('Created: ' + CapeDir03)
    if path.exists(CapeDir02) == 0:
        os.mkdir(CapeDir02)
        print('Created: ' + CapeDir02)
    if path.exists(CapeDir01) == 0:
        os.mkdir(CapeDir01)
        print('Created: ' + CapeDir01)
    CapeDir11 = fileDir + 'Dungeons/Content/Actors/Characters/Player/Capes/Skins/SinisterBlueCape'
    CapeDir12 = fileDir + 'Dungeons/Content/Actors/Characters/Player/Capes/Skins'
    CapeDir13 = fileDir + 'Dungeons/Content/Actors/Characters/Player/Capes'
    if path.exists(CapeDir13) == 0:
        os.mkdir(CapeDir13)
        print('Created: ' + CapeDir13)
    if path.exists(CapeDir12) == 0:
        os.mkdir(CapeDir12)
        print('Created: ' + CapeDir12)
    if path.exists(CapeDir11) == 0:
        os.mkdir(CapeDir11)
        print('Created: ' + CapeDir11)
    CapeDir0 = fileDir + 'DungeonsSkins/Content/Dungeons/Content/Actors/Characters/Player/Capes/Skins/SinisterBlueCape/'
    
    CapeFile1 = CapeDir0 + 'T_SinisterBlueCape.png'
    CapeFile2 = CapeDir0 + 'T_SinisterBlueCape.uasset'
    CapeFile3 = CapeDir0 + 'T_SinisterBlueCape_S.png'
    CapeFile4 = CapeDir0 + 'T_SinisterBlueCape_S.uasset'
    
    CapeFile0_1 = pathlib.Path(CapeFile1)
    CapeFile0_2 = pathlib.Path(CapeFile2)
    CapeFile0_3 = pathlib.Path(CapeFile3)
    CapeFile0_4 = pathlib.Path(CapeFile4)
    
    if CapeFile0_1.exists ():
        os.remove(CapeFile1)
        print('Removed: ' + CapeFile1)
    if CapeFile0_2.exists ():
        os.remove(CapeFile2)
        print('Removed: ' + CapeFile2)
    if CapeFile0_3.exists ():
        os.remove(CapeFile3)
        print('Removed: ' + CapeFile3)
    if CapeFile0_4.exists ():
        os.remove(CapeFile4)
        print('Removed: ' + CapeFile4)
    
    copyfile(capeNameDir, CapeDir0 + CapeFileName)
    print('Copied: ' + CapeFileName + ' to ' + CapeDir0)
    
    copyfile(fileDir + 'Skin/Cape_S.png', CapeDir0 + CapeSFileName)
    print('Copied: ' + 'Cape_S.png to ' + CapeDir0)
    
    CapeDir1 = fileDir + 'Dungeons/Content/Actors/Characters/Player/Capes/Skins/SinisterBlueCape/'
    
    CapeFile5 = CapeDir1 + 'T_SinisterBlueCape.uasset'
    CapeFile6 = CapeDir1 + 'T_SinisterBlueCape.uexp'
    CapeFile7 = CapeDir1 + 'T_SinisterBlueCape_S.uasset'
    CapeFile8 = CapeDir1 + 'T_SinisterBlueCape_S.uexp'
    CapeFile1_1 = pathlib.Path(CapeFile5)
    CapeFile1_2 = pathlib.Path(CapeFile6)
    CapeFile1_3 = pathlib.Path(CapeFile7)
    CapeFile1_4 = pathlib.Path(CapeFile8)
    
    if CapeFile1_1.exists ():
        os.remove(CapeFile5)
        print('Removed: ' + CapeFile5)
    if CapeFile1_2.exists ():
        os.remove(CapeFile6)
        print('Removed: ' + CapeFile6)
    if CapeFile1_3.exists ():
        os.remove(CapeFile7)
        print('Removed: ' + CapeFile7)
    if CapeFile1_4.exists ():
        os.remove(CapeFile8)
        print('Removed: ' + CapeFile8)
        
def delCapeFolders():
    CapeDir0_1 = fileDir + 'DungeonsSkins/Content/Dungeons/Content/Actors/Characters/Player/Capes/Skins/SinisterBlueCape'
    CapeDir0_2 = fileDir + 'DungeonsSkins/Content/Dungeons/Content/Actors/Characters/Player/Capes/Skins'
    CapeDir0_3 = fileDir + 'DungeonsSkins/Content/Dungeons/Content/Actors/Characters/Player/Capes'
    
    if path.exists(CapeDir0_1) == 1:
        shutil.rmtree(CapeDir0_1)
        print('Removed: ' + CapeDir0_1)
    if path.exists(CapeDir0_2) == 1:
        shutil.rmtree(CapeDir0_2)
        print('Removed: ' + CapeDir0_2)
    if path.exists(CapeDir0_3) == 1:
        shutil.rmtree(CapeDir0_3)
        print('Removed: ' + CapeDir0_3)
    
    CapeDir1_1 = fileDir + 'Dungeons/Content/Actors/Characters/Player/Capes/Skins/SinisterBlueCape'
    CapeDir1_2 = fileDir + 'Dungeons/Content/Actors/Characters/Player/Capes/Skins'
    CapeDir1_3 = fileDir + 'Dungeons/Content/Actors/Characters/Player/Capes'
    
    if path.exists(CapeDir1_1) == 1:
        shutil.rmtree(CapeDir1_1)
        print('Removed: ' + CapeDir1_1)
    if path.exists(CapeDir1_2) == 1:
        shutil.rmtree(CapeDir1_2)
        print('Removed: ' + CapeDir1_2)
    if path.exists(CapeDir1_3) == 1:
        shutil.rmtree(CapeDir1_3)
        print('Removed: ' + CapeDir1_3)
        
def manageFolders():
    SkinName = 'T_'+ Name
    SkinShortFileName = SkinName + '.png'
    SkinFileName = SkinName + '_Skin.png'
    OldSkinDir0 = fileDir + 'DungeonsSkins/Content/Dungeons/Content/Actors/Characters/Player/Master/Skins/'
    OldSkinDir0Folder0 = os.listdir(OldSkinDir0)
    OldSkinDir0Folder1 = ''.join(OldSkinDir0Folder0)
    if OldSkinDir0Folder1 in NameList:
        SkinDir0 = OldSkinDir0 + OldSkinDir0Folder1 + '/'
        if path.exists(SkinDir0) == 1:
            shutil.rmtree(SkinDir0)
            print('Removed: ' + SkinDir0)
    OldSkinDir1 = fileDir + 'Dungeons/Content/Actors/Characters/Player/Master/Skins/'
    OldSkinDir1Folder0 = os.listdir(OldSkinDir1)
    OldSkinDir1Folder1 = ''.join(OldSkinDir1Folder0)
    if OldSkinDir1Folder1 in NameList:
        SkinDir1 = OldSkinDir1 + OldSkinDir1Folder1 + '/'
        if path.exists(SkinDir1) == 1:
            shutil.rmtree(SkinDir1)
            print('Removed: ' + SkinDir1)
    NewSkinDir0 = fileDir + 'DungeonsSkins/Content/Dungeons/Content/Actors/Characters/Player/Master/Skins/' + Name
    NewSkinDir1 = fileDir + 'Dungeons/Content/Actors/Characters/Player/Master/Skins/' + Name
    os.mkdir(NewSkinDir0)
    print('Created: ' + NewSkinDir0)
    os.mkdir(NewSkinDir1)
    print('Created: ' + NewSkinDir1)
    
    if Name == 'Winter_Warrior' or Name == 'Hex' or Name == 'Hal' or Name == 'Frosty' or Name == 'Explorer' or Name == 'Archeologist':
        print('Copied: ' + SkinShortFileName + ' to ' + NewSkinDir0)
        copyfile(skinNameDir, NewSkinDir0 + '/' + SkinShortFileName)
        print('Copied: T_' + Name + '_S.png to ' + NewSkinDir0)
        copyfile(fileDir + 'Skin/Skin_S.png', NewSkinDir0 + '/T_' + Name + '_S.png')
    elif Name == 'Steve':
        print('Copied: ' + SkinShortFileName + ' to ' + NewSkinDir0)
        copyfile(skinNameDir, fileDir + 'DungeonsSkins/Content/Dungeons/Content/Actors/Characters/Player/Master/Skins/Steve/T_Steve_Skin.png')
        print('Copied: ' + 'T_Steve_S.png to ' + NewSkinDir0)
        copyfile(fileDir + 'Skin/T_Steve_S.png', fileDir + 'DungeonsSkins/Content/Dungeons/Content/Actors/Characters/Player/Master/Skins/Steve/T_Steve_S.png')
    else:
        print('Copied: ' + SkinFileName + ' to ' + NewSkinDir0)
        copyfile(skinNameDir, NewSkinDir0 + '/' + SkinFileName)
        print('Copied: T_' + Name + '_Skin_S.png to ' + NewSkinDir0)
        copyfile(fileDir + 'Skin/Skin_S.png', NewSkinDir0 + '/T_' + Name + '_Skin_S.png')
        
def delSkinFolders():
    OldSkinDir0 = fileDir + 'DungeonsSkins/Content/Dungeons/Content/Actors/Characters/Player/Master/Skins/'
    OldSkinDir0Folder0 = os.listdir(OldSkinDir0)
    OldSkinDir0Folder1 = ''.join(OldSkinDir0Folder0)
    if OldSkinDir0Folder1 in NameList:
        SkinDir0 = OldSkinDir0 + OldSkinDir0Folder1 + '/'
        if path.exists(SkinDir0) == 1:
            shutil.rmtree(SkinDir0)
            print('Removed: ' + SkinDir0)
    OldSkinDir1 = fileDir + 'Dungeons/Content/Actors/Characters/Player/Master/Skins/'
    OldSkinDir1Folder0 = os.listdir(OldSkinDir1)
    OldSkinDir1Folder1 = ''.join(OldSkinDir1Folder0)
    if OldSkinDir1Folder1 in NameList:
        SkinDir1 = OldSkinDir1 + OldSkinDir1Folder1 + '/'
        if path.exists(SkinDir1) == 1:
            shutil.rmtree(SkinDir1)
            print('Removed: ' + SkinDir1)

def writeJson():
    fileDirDouble = fileDir.replace('/', '//')
    if SkinOrCape == '2':
        print('Writing JSON Files...')
        if Name == 'Winter_Warrior' or Name == 'Hex' or Name == 'Hal' or Name == 'Frosty' or Name == 'Explorer' or Name == 'Archeologist':
            skinDirDouble = '"' + fileDirDouble + 'DungeonsSkins//Content//Dungeons//Content//Actors//Characters//Player//Master//Skins//' + Name + '//T_' + Name + '.png",'
            skinSDirDouble = '"' + fileDirDouble + 'DungeonsSkins//Content//Dungeons//Content//Actors//Characters//Player//Master//Skins//' + Name + '//T_' + Name + '_S.png"'
            f = open("Scripts/importSettings.json", "w")
            f.write('{')
            f.write("\n")
            f.write('   "ImportGroups":[')
            f.write("\n")
            f.write('      {')
            f.write("\n")
            f.write('          "GroupName":"Textures",')
            f.write("\n")
            f.write('          "Filenames":[')
            f.write("\n")
            f.write('           ' + skinDirDouble)
            f.write("\n")
            f.write('           ' + skinSDirDouble)
            f.write("\n")
            f.write('          ],')
            f.write("\n")
            f.write('          "DestinationPath":"/Game/Dungeons/Content/Actors/Characters/Player/Master/Skins/' + Name + '/",')
            f.write("\n")
            f.write('          "bReplaceExisting":"true",')
            f.write("\n")
            f.write('          "bSkipReadOnly":"false",')
            f.write("\n")
            f.write('         "FactoryName": "TextureFactory",')
            f.write("\n")
            f.write('          "ImportSettings":{')
            f.write("\n")
            f.write('              "CompressionSettings": "TC_BC7",')
            f.write("\n")
            f.write('             "LODGroup": "TEXTUREGROUP_Pixels2D"')
            f.write("\n")
            f.write('          }')
            f.write("\n")
            f.write('      }')
            f.write("\n")
            f.write('   ]')
            f.write("\n")
            f.write('}')
            f.close()
        elif Name == 'Steve':
            steveDir = '"' + fileDirDouble + 'DungeonsSkins//Content//Dungeons//Content//Actors//Characters//Player//Master//Skins//Steve//T_Steve_Skin.png",'
            steveSDir = '"' + fileDirDouble + 'DungeonsSkins//Content//Dungeons//Content//Actors//Characters//Player//Master//Skins//Steve//T_Steve_S.png"'
            f = open("Scripts/importSettingsSteve.json", "w")
            f.write('{')
            f.write("\n")
            f.write('   "ImportGroups":[')
            f.write("\n")
            f.write('      {')
            f.write("\n")
            f.write('          "GroupName":"Textures",')
            f.write("\n")
            f.write('          "Filenames":[')
            f.write("\n")
            f.write('           ' + steveDir)
            f.write("\n")
            f.write('           ' + steveSDir)
            f.write("\n")
            f.write('          ],')
            f.write("\n")
            f.write('          "DestinationPath":"/Game/Dungeons/Content/Actors/Characters/Player/Master/Skins/Steve/",')
            f.write("\n")
            f.write('          "bReplaceExisting":"true",')
            f.write("\n")
            f.write('          "bSkipReadOnly":"false",')
            f.write("\n")
            f.write('         "FactoryName": "TextureFactory",')
            f.write("\n")
            f.write('          "ImportSettings":{')
            f.write("\n")
            f.write('              "CompressionSettings": "TC_BC7",')
            f.write("\n")
            f.write('             "LODGroup": "TEXTUREGROUP_Pixels2D"')
            f.write("\n")
            f.write('          }')
            f.write("\n")
            f.write('      }')
            f.write("\n")
            f.write('   ]')
            f.write("\n")
            f.write('}')
            f.close()
        else:
            skinDirDouble = '"' + fileDirDouble + 'DungeonsSkins//Content//Dungeons//Content//Actors//Characters//Player//Master//Skins//' + Name + '//T_' + Name + '_Skin.png",'
            skinSDirDouble = '"' + fileDirDouble + 'DungeonsSkins//Content//Dungeons//Content//Actors//Characters//Player//Master//Skins//' + Name + '//T_' + Name + '_Skin_S.png"'
            f = open("Scripts/importSettings.json", "w")
            f.write('{')
            f.write("\n")
            f.write('   "ImportGroups":[')
            f.write("\n")
            f.write('      {')
            f.write("\n")
            f.write('          "GroupName":"Textures",')
            f.write("\n")
            f.write('          "Filenames":[')
            f.write("\n")
            f.write('           ' + skinDirDouble)
            f.write("\n")
            f.write('           ' + skinSDirDouble)
            f.write("\n")
            f.write('          ],')
            f.write("\n")
            f.write('          "DestinationPath":"/Game/Dungeons/Content/Actors/Characters/Player/Master/Skins/' + Name + '/",')
            f.write("\n")
            f.write('          "bReplaceExisting":"true",')
            f.write("\n")
            f.write('          "bSkipReadOnly":"false",')
            f.write("\n")
            f.write('         "FactoryName": "TextureFactory",')
            f.write("\n")
            f.write('          "ImportSettings":{')
            f.write("\n")
            f.write('              "CompressionSettings": "TC_BC7",')
            f.write("\n")
            f.write('             "LODGroup": "TEXTUREGROUP_Pixels2D"')
            f.write("\n")
            f.write('          }')
            f.write("\n")
            f.write('      }')
            f.write("\n")
            f.write('   ]')
            f.write("\n")
            f.write('}')
            f.close()
        capeDirDouble = '"' + fileDirDouble + 'DungeonsSkins//Content//Dungeons//Content//Actors//Characters//Player//Capes//Skins//MonstrosityGoldenCape//T_SinisterBlueCape.png",'
        capeSDirDouble = '"' + fileDirDouble + 'DungeonsSkins//Content//Dungeons//Content//Actors//Characters//Player//Capes//Skins//MonstrosityGoldenCape//T_SinisterBlueCape_S.png"'
        f = open("Scripts/importSettingsCape.json", "w")
        f.write('{')
        f.write("\n")
        f.write('   "ImportGroups":[')
        f.write("\n")
        f.write('      {')
        f.write("\n")
        f.write('          "GroupName":"Textures",')
        f.write("\n")
        f.write('          "Filenames":[')
        f.write("\n")
        f.write('           ' + capeDirDouble)
        f.write("\n")
        f.write('           ' + capeSDirDouble)
        f.write("\n")
        f.write('          ],')
        f.write("\n")
        f.write('          "DestinationPath":"/Game/Dungeons/Content/Actors/Characters/Player/Capes/Skins/SinisterBlueCape/",')
        f.write("\n")
        f.write('          "bReplaceExisting":"true",')
        f.write("\n")
        f.write('          "bSkipReadOnly":"false",')
        f.write("\n")
        f.write('         "FactoryName": "TextureFactory",')
        f.write("\n")
        f.write('          "ImportSettings":{')
        f.write("\n")
        f.write('              "CompressionSettings": "TC_BC7",')
        f.write("\n")
        f.write('             "LODGroup": "TEXTUREGROUP_Pixels2D"')
        f.write("\n")
        f.write('          }')
        f.write("\n")
        f.write('      }')
        f.write("\n")
        f.write('   ]')
        f.write("\n")
        f.write('}')
        f.close()
        print('JSON Files Created')
    elif SkinOrCape == '1':
        if Name == 'Winter_Warrior' or Name == 'Hex' or Name == 'Hal' or Name == 'Frosty' or Name == 'Explorer' or Name == 'Archeologist':
            skinDirDouble = '"' + fileDirDouble + 'DungeonsSkins//Content//Dungeons//Content//Actors//Characters//Player//Master//Skins//' + Name + '//T_' + Name + '.png",'
            skinSDirDouble = '"' + fileDirDouble + 'DungeonsSkins//Content//Dungeons//Content//Actors//Characters//Player//Master//Skins//' + Name + '//T_' + Name + '_S.png"'
            f = open("Scripts/importSettings.json", "w")
            f.write('{')
            f.write("\n")
            f.write('   "ImportGroups":[')
            f.write("\n")
            f.write('      {')
            f.write("\n")
            f.write('          "GroupName":"Textures",')
            f.write("\n")
            f.write('          "Filenames":[')
            f.write("\n")
            f.write('           ' + skinDirDouble)
            f.write("\n")
            f.write('           ' + skinSDirDouble)
            f.write("\n")
            f.write('          ],')
            f.write("\n")
            f.write('          "DestinationPath":"/Game/Dungeons/Content/Actors/Characters/Player/Master/Skins/' + Name + '/",')
            f.write("\n")
            f.write('          "bReplaceExisting":"true",')
            f.write("\n")
            f.write('          "bSkipReadOnly":"false",')
            f.write("\n")
            f.write('         "FactoryName": "TextureFactory",')
            f.write("\n")
            f.write('          "ImportSettings":{')
            f.write("\n")
            f.write('              "CompressionSettings": "TC_BC7",')
            f.write("\n")
            f.write('             "LODGroup": "TEXTUREGROUP_Pixels2D"')
            f.write("\n")
            f.write('          }')
            f.write("\n")
            f.write('      }')
            f.write("\n")
            f.write('   ]')
            f.write("\n")
            f.write('}')
            f.close()
        elif Name == 'Steve':
            steveDir = '"' + fileDirDouble + 'DungeonsSkins//Content//Dungeons//Content//Actors//Characters//Player//Master//Skins//Steve//T_Steve_Skin.png",'
            steveSDir = '"' + fileDirDouble + 'DungeonsSkins//Content//Dungeons//Content//Actors//Characters//Player//Master//Skins//Steve//T_Steve_S.png"'
            f = open("Scripts/importSettingsSteve.json", "w")
            f.write('{')
            f.write("\n")
            f.write('   "ImportGroups":[')
            f.write("\n")
            f.write('      {')
            f.write("\n")
            f.write('          "GroupName":"Textures",')
            f.write("\n")
            f.write('          "Filenames":[')
            f.write("\n")
            f.write('           ' + steveDir)
            f.write("\n")
            f.write('           ' + steveSDir)
            f.write("\n")
            f.write('          ],')
            f.write("\n")
            f.write('          "DestinationPath":"/Game/Dungeons/Content/Actors/Characters/Player/Master/Skins/Steve/",')
            f.write("\n")
            f.write('          "bReplaceExisting":"true",')
            f.write("\n")
            f.write('          "bSkipReadOnly":"false",')
            f.write("\n")
            f.write('         "FactoryName": "TextureFactory",')
            f.write("\n")
            f.write('          "ImportSettings":{')
            f.write("\n")
            f.write('              "CompressionSettings": "TC_BC7",')
            f.write("\n")
            f.write('             "LODGroup": "TEXTUREGROUP_Pixels2D"')
            f.write("\n")
            f.write('          }')
            f.write("\n")
            f.write('      }')
            f.write("\n")
            f.write('   ]')
            f.write("\n")
            f.write('}')
            f.close()
        else:
            skinDirDouble = '"' + fileDirDouble + 'DungeonsSkins//Content//Dungeons//Content//Actors//Characters//Player//Master//Skins//' + Name + '//T_' + Name + '_Skin.png",'
            skinSDirDouble = '"' + fileDirDouble + 'DungeonsSkins//Content//Dungeons//Content//Actors//Characters//Player//Master//Skins//' + Name + '//T_' + Name + '_Skin_S.png"'
            f = open("Scripts/importSettings.json", "w")
            f.write('{')
            f.write("\n")
            f.write('   "ImportGroups":[')
            f.write("\n")
            f.write('      {')
            f.write("\n")
            f.write('          "GroupName":"Textures",')
            f.write("\n")
            f.write('          "Filenames":[')
            f.write("\n")
            f.write('           ' + skinDirDouble)
            f.write("\n")
            f.write('           ' + skinSDirDouble)
            f.write("\n")
            f.write('          ],')
            f.write("\n")
            f.write('          "DestinationPath":"/Game/Dungeons/Content/Actors/Characters/Player/Master/Skins/' + Name + '/",')
            f.write("\n")
            f.write('          "bReplaceExisting":"true",')
            f.write("\n")
            f.write('          "bSkipReadOnly":"false",')
            f.write("\n")
            f.write('         "FactoryName": "TextureFactory",')
            f.write("\n")
            f.write('          "ImportSettings":{')
            f.write("\n")
            f.write('              "CompressionSettings": "TC_BC7",')
            f.write("\n")
            f.write('             "LODGroup": "TEXTUREGROUP_Pixels2D"')
            f.write("\n")
            f.write('          }')
            f.write("\n")
            f.write('      }')
            f.write("\n")
            f.write('   ]')
            f.write("\n")
            f.write('}')
            f.close()
        print('JSON Files Created')
        
def writeCapeJson():
    fileDirDouble = fileDir.replace('/', '//')
    capeDirDouble = '"' + fileDirDouble + 'DungeonsSkins//Content//Dungeons//Content//Actors//Characters//Player//Capes//Skins//MonstrosityGoldenCape//T_SinisterBlueCape.png",'
    capeSDirDouble = '"' + fileDirDouble + 'DungeonsSkins//Content//Dungeons//Content//Actors//Characters//Player//Capes//Skins//MonstrosityGoldenCape//T_SinisterBlueCape_S.png"'
    f = open("Scripts/importSettingsCape.json", "w")
    f.write('{')
    f.write("\n")
    f.write('   "ImportGroups":[')
    f.write("\n")
    f.write('      {')
    f.write("\n")
    f.write('          "GroupName":"Textures",')
    f.write("\n")
    f.write('          "Filenames":[')
    f.write("\n")
    f.write('           ' + capeDirDouble)
    f.write("\n")
    f.write('           ' + capeSDirDouble)
    f.write("\n")
    f.write('          ],')
    f.write("\n")
    f.write('          "DestinationPath":"/Game/Dungeons/Content/Actors/Characters/Player/Capes/Skins/SinisterBlueCape/",')
    f.write("\n")
    f.write('          "bReplaceExisting":"true",')
    f.write("\n")
    f.write('          "bSkipReadOnly":"false",')
    f.write("\n")
    f.write('         "FactoryName": "TextureFactory",')
    f.write("\n")
    f.write('          "ImportSettings":{')
    f.write("\n")
    f.write('              "CompressionSettings": "TC_BC7",')
    f.write("\n")
    f.write('             "LODGroup": "TEXTUREGROUP_Pixels2D"')
    f.write("\n")
    f.write('          }')
    f.write("\n")
    f.write('      }')
    f.write("\n")
    f.write('   ]')
    f.write("\n")
    f.write('}')
    f.close()
    print('JSON Files Created')
    
def openUnreal():
    if SkinOrCape == '2':
        Editor = editorDir + 'UE4Editor-Cmd.exe'
        ImportAssets = '-importsettings=' + fileDir + 'Scripts\importSettingsCape.json'
        subprocess.call([Editor, fileDir + 'DungeonsSkins/DungeonsSkins.uproject', '-run=ImportAssets', ImportAssets, '-nosourcecontrol'])
    elif SkinOrCape == '1':
        if SkinOrCape == '2':
            print('Importing Textures into Unreal Editor...')
            ImportAssets = '-importsettings=' + fileDir + 'Scripts\importSettingsCape.json'
            subprocess.call([Editor, fileDir + 'DungeonsSkins/DungeonsSkins.uproject', '-run=ImportAssets', ImportAssets, '-nosourcecontrol'])
        elif SkinOrCape == '1':
            print('Importing Textures into Unreal Editor...')
            if Name == 'Steve':
                Editor = editorDir + 'UE4Editor-Cmd.exe'
                ImportAssets = '-importsettings=' + fileDir + 'Scripts\importSettingsSteve.json'
                subprocess.call([Editor, fileDir + 'DungeonsSkins/DungeonsSkins.uproject', '-run=ImportAssets', ImportAssets, '-nosourcecontrol'])
            else:
                Editor = editorDir + 'UE4Editor-Cmd.exe'
                ImportAssets = '-importsettings=' + fileDir + 'Scripts\importSettings.json'
                subprocess.call([Editor, fileDir + 'DungeonsSkins/DungeonsSkins.uproject', '-run=ImportAssets', ImportAssets, '-nosourcecontrol'])
    else:
        print('Error while Opening Unreal')

def cookAssets():
    Editor = editorDir + 'UE4Editor-Cmd.exe'
    Project = fileDir + 'DungeonsSkins/DungeonsSkins.uproject'
    subprocess.call([Editor, Project, '-run=cook', '-targetplatform=WindowsNoEditor'])
    
def copyCookedFiles():
    cookedFilesDir = 'DungeonsSkins/Saved/Cooked/WindowsNoEditor/DungeonsSkins/Content/Dungeons/Content/Actors/Characters/Player/'
    cookedFileDir = 'Dungeons/Content/Actors/Characters/Player/'
    cookedFile1 = 'T_' + Name + '_Skin.uasset'
    cookedFile2 = 'T_' + Name + '_Skin.uexp'
    cookedFile7 = 'T_' + Name + '_Skin_S.uasset'
    cookedFile8 = 'T_' + Name + '_Skin_S.uexp'
    
    cookedFile9 = 'T_' + Name + '.uasset'
    cookedFile10 = 'T_' + Name + '.uexp'
    cookedFile11 = 'T_' + Name + '_S.uasset'
    cookedFile12 = 'T_' + Name + '_S.uexp'
    
    if SkinOrCape == '2':
        cookedFile3 = 'T_SinisterBlueCape.uasset'
        cookedFile4 = 'T_SinisterBlueCape.uexp'
        cookedFile5 = 'T_SinisterBlueCape_S.uasset'
        cookedFile6 = 'T_SinisterBlueCape_S.uexp'
    
    if Name == 'Winter_Warrior' or Name == 'Hex' or Name == 'Hal' or Name == 'Frosty' or Name == 'Explorer' or Name == 'Archeologist':
        copyfile(fileDir + cookedFilesDir + 'Master/Skins/' + Name + '/' + cookedFile9, fileDir + cookedFileDir + 'Master/Skins/' + Name + '/' + cookedFile9)
        print('Copied: ' + cookedFile9 + ' to ' + fileDir + cookedFileDir)
        copyfile(fileDir + cookedFilesDir + 'Master/Skins/' + Name + '/' + cookedFile10, fileDir + cookedFileDir + 'Master/Skins/' + Name + '/' + cookedFile10)
        print('Copied: ' + cookedFile10 + ' to ' + fileDir + cookedFileDir)
        copyfile(fileDir + cookedFilesDir + 'Master/Skins/' + Name + '/' + cookedFile11, fileDir + cookedFileDir + 'Master/Skins/' + Name + '/' + cookedFile11)
        print('Copied: ' + cookedFile11 + ' to ' + fileDir + cookedFileDir)
        copyfile(fileDir + cookedFilesDir + 'Master/Skins/' + Name + '/' + cookedFile12, fileDir + cookedFileDir + 'Master/Skins/' + Name + '/' + cookedFile12)
        print('Copied: ' + cookedFile12 + ' to ' + fileDir + cookedFileDir)
    elif Name == 'Steve':
        copyfile(fileDir + cookedFilesDir + 'Master/Skins/' + Name + '/' + 'T_Steve_Skin.uasset', fileDir + cookedFileDir + 'Master/Skins/' + Name + '/' + 'T_Steve_Skin.uasset')
        print('Copied: ' + 'T_Steve_Skin.uasset to ' + fileDir + cookedFileDir)
        copyfile(fileDir + cookedFilesDir + 'Master/Skins/' + Name + '/' + 'T_Steve_Skin.uexp', fileDir + cookedFileDir + 'Master/Skins/' + Name + '/' + 'T_Steve_Skin.uexp')
        print('Copied: ' + 'T_Steve_Skin.uexp to ' + fileDir + cookedFileDir)
        copyfile(fileDir + cookedFilesDir + 'Master/Skins/Steve/T_Steve_S.uasset', fileDir + cookedFileDir + 'Master/Skins/Steve/T_Steve_S.uasset')
        print('Copied: ' + 'T_Steve_S.uasset to ' + fileDir + cookedFileDir)
        copyfile(fileDir + cookedFilesDir + 'Master/Skins/Steve/T_Steve_S.uexp', fileDir + cookedFileDir + 'Master/Skins/Steve/T_Steve_S.uexp')
        print('Copied: ' + 'T_Steve_S.uexp to ' + fileDir + cookedFileDir)
    else:
        copyfile(fileDir + cookedFilesDir + 'Master/Skins/' + Name + '/' + cookedFile1, fileDir + cookedFileDir + 'Master/Skins/' + Name + '/' + cookedFile1)
        print('Copied: ' + cookedFile1 + ' to ' + fileDir + cookedFileDir)
        copyfile(fileDir + cookedFilesDir + 'Master/Skins/' + Name + '/' + cookedFile2, fileDir + cookedFileDir + 'Master/Skins/' + Name + '/' + cookedFile2)
        print('Copied: ' + cookedFile2 + ' to ' + fileDir + cookedFileDir)
        copyfile(fileDir + cookedFilesDir + 'Master/Skins/' + Name + '/' + cookedFile7, fileDir + cookedFileDir + 'Master/Skins/' + Name + '/' + cookedFile7)
        print('Copied: ' + cookedFile7 + ' to ' + fileDir + cookedFileDir)
        copyfile(fileDir + cookedFilesDir + 'Master/Skins/' + Name + '/' + cookedFile8, fileDir + cookedFileDir + 'Master/Skins/' + Name + '/' + cookedFile8)
        print('Copied: ' + cookedFile8 + ' to ' + fileDir + cookedFileDir)
    
    if SkinOrCape == '2':
        copyfile(fileDir + cookedFilesDir + 'Capes/Skins/SinisterBlueCape/' + cookedFile3, fileDir + cookedFileDir + 'Capes/Skins/SinisterBlueCape/' + cookedFile3)
        print('Copied: ' + cookedFile3 + ' to ' + fileDir + cookedFileDir)
        copyfile(fileDir + cookedFilesDir + 'Capes/Skins/SinisterBlueCape/' + cookedFile4, fileDir + cookedFileDir + 'Capes/Skins/SinisterBlueCape/' + cookedFile4)
        print('Copied: ' + cookedFile4 + ' to ' + fileDir + cookedFileDir)
        copyfile(fileDir + cookedFilesDir + 'Capes/Skins/SinisterBlueCape/' + cookedFile5, fileDir + cookedFileDir + 'Capes/Skins/SinisterBlueCape/' + cookedFile5)
        print('Copied: ' + cookedFile5 + ' to ' + fileDir + cookedFileDir)
        copyfile(fileDir + cookedFilesDir + 'Capes/Skins/SinisterBlueCape/' + cookedFile6, fileDir + cookedFileDir + 'Capes/Skins/SinisterBlueCape/' + cookedFile6)
        print('Copied: ' + cookedFile6 + ' to ' + fileDir + cookedFileDir)

def copyCookedCapeFiles():
    cookedFilesDir = 'DungeonsSkins/Saved/Cooked/WindowsNoEditor/DungeonsSkins/Content/Dungeons/Content/Actors/Characters/Player/'
    cookedFileDir = 'Dungeons/Content/Actors/Characters/Player/'
    cookedFile3 = 'T_SinisterBlueCape.uasset'
    cookedFile4 = 'T_SinisterBlueCape.uexp'
    cookedFile5 = 'T_SinisterBlueCape_S.uasset'
    cookedFile6 = 'T_SinisterBlueCape_S.uexp'
    copyfile(fileDir + cookedFilesDir + 'Capes/Skins/SinisterBlueCape/' + cookedFile3, fileDir + cookedFileDir + 'Capes/Skins/SinisterBlueCape/' + cookedFile3)
    print('Copied: ' + cookedFile3 + ' to ' + fileDir + cookedFileDir)
    copyfile(fileDir + cookedFilesDir + 'Capes/Skins/SinisterBlueCape/' + cookedFile4, fileDir + cookedFileDir + 'Capes/Skins/SinisterBlueCape/' + cookedFile4)
    print('Copied: ' + cookedFile4 + ' to ' + fileDir + cookedFileDir)
    copyfile(fileDir + cookedFilesDir + 'Capes/Skins/SinisterBlueCape/' + cookedFile5, fileDir + cookedFileDir + 'Capes/Skins/SinisterBlueCape/' + cookedFile5)
    print('Copied: ' + cookedFile5 + ' to ' + fileDir + cookedFileDir)
    copyfile(fileDir + cookedFilesDir + 'Capes/Skins/SinisterBlueCape/' + cookedFile6, fileDir + cookedFileDir + 'Capes/Skins/SinisterBlueCape/' + cookedFile6)
    print('Copied: ' + cookedFile6 + ' to ' + fileDir + cookedFileDir)
    
def packageMod():
    if SkinOrCape == '2':
        pakScript = fileDir + 'Scripts/u4pak.py'
        GamePaks = gameDir + RequesterName + '-Cape.pak'
        subprocess.call(['python', pakScript, 'pack', GamePaks, 'Dungeons', '-p', '-z'])
    else:
        pakScript = fileDir + 'Scripts/u4pak.py'
        GamePaks = gameDir + RequesterName + '-Skin.pak'
        subprocess.call(['python', pakScript, 'pack', GamePaks, 'Dungeons', '-p', '-z'])

def skinFormat():
    skinFolderFile = os.listdir(fileDir + 'Skin/Skin/')
    skinNameDirImage = fileDir + 'Skin/Skin/' + skinFolderFile[0]
    if Format == '1':
        skinFolderFile = os.listdir(fileDir + 'Skin/Skin/')
        skinNameDirImage = fileDir + 'Skin/Skin/' + skinFolderFile[0]
        skinImageTest = Image.open(skinNameDirImage)
        width, height = skinImageTest.size
        if width == 64 and height == 64:
            print(width)
            print(height)
            if IncludeEyes == '2':
                print('Removing Eyes')
                convertedTexture = displace('steve', skinNameDirImage, keepEyesAndMouth = False)
                convertedTexture.save(skinNameDirImage)
                convertedTexture.save(fileDir + 'Skin/T_Steve_S.png')
                mainFiles()
            elif IncludeEyes == '1':
                print('Keeping Eyes')
                convertedTexture = displace('steve', skinNameDirImage, keepEyesAndMouth = True)
                convertedTexture.save(skinNameDirImage)
                convertedTexture.save(fileDir + 'Skin/T_Steve_S.png')
                mainFiles()
            else:
                print('Error: Cannot Determine Whether to Keep Eyes')
        elif width == 64 and height == 32:
            if IncludeEyes == '2':
                print('Removing Eyes')
                convertedTexture = displace('old', skinNameDirImage, keepEyesAndMouth = False)
                convertedTexture.save(skinNameDirImage)
                convertedTexture.save(fileDir + 'Skin/T_Steve_S.png')
                mainFiles()
            elif IncludeEyes == '1':
                print('Keeping Eyes')
                convertedTexture = displace('old', skinNameDirImage, keepEyesAndMouth = True)
                convertedTexture.save(skinNameDirImage)
                convertedTexture.save(fileDir + 'Skin/T_Steve_S.png')
                mainFiles()
            else:
                print('Error: Cannot Determine Whether to Keep Eyes')
    elif Format == '2':
        if IncludeEyes == '2':
            print('Removing Eyes')
            convertedTexture = displace('alex', skinNameDirImage, keepEyesAndMouth = False)
            convertedTexture.save(skinNameDirImage)
            convertedTexture.save(fileDir + 'Skin/T_Steve_S.png')
            mainFiles()
        elif IncludeEyes == '1':
            print('Keeping Eyes')
            convertedTexture = displace('alex', skinNameDirImage, keepEyesAndMouth = True)
            convertedTexture.save(skinNameDirImage)
            convertedTexture.save(fileDir + 'Skin/T_Steve_S.png')
            mainFiles()
        else:
            print('Error: Cannot Determine Whether to Keep Eyes')
    else:
        print('Error: Format is Incorrect')

def mainFiles():
    if SkinOrCape == '2':
        capeFolderFile = os.listdir(fileDir + 'Skin/Cape/')
        capeNameDirImage = fileDir + 'Skin/Cape/' + capeFolderFile[0]
        capeImageTest = Image.open(capeNameDirImage)
        width, height = capeImageTest.size
        if width == 64 and height == 64:
            print(width)
            print(height)
            manageCapeFolders()
            writeCapeJson()
            openUnreal()
            cookAssets()
            copyCookedCapeFiles()
            packageMod()
        elif width == 32 and height == 32:
            print(width)
            print(height)
            manageCapeFolders()
            writeCapeJson()
            openUnreal()
            cookAssets()
            copyCookedCapeFiles()
            packageMod()
        elif width == 92 and height == 44:
            print("Resizing Cape as it's in the Wrong Format")
            processOFCapeImage()
            mainFiles()
        elif width == 46 and height == 22:
            print("Resizing Cape as it's in the Wrong Format")
            processSmallOFCapeImage()
            mainFiles()
        elif width == 64 and height == 32:
            print("Resizing Cape as it's in the Wrong Format")
            processCapeImage()
            mainFiles()
        elif width == 44 and height == 34:
            print("Resizing Cape as it's in the Wrong Format")
            capeFolderFile = os.listdir(fileDir + 'Skin/Cape/')
            capeNameDirImage = fileDir + 'Skin/Cape/' + capeFolderFile[0]
            capeImage = Image.open(capeNameDirImage).convert("RGBA")
            capeImage = capeImage.crop((0, 0, 64, 64))
            capeImage.save(capeNameDirImage)
            print('Resized Cape to fit OptiFine Format')
            mainFiles()
        elif width == 22 and height == 17:
            print("Resizing Cape as it's in the Wrong Format")
            capeFolderFile = os.listdir(fileDir + 'Skin/Cape/')
            capeNameDirImage = fileDir + 'Skin/Cape/' + capeFolderFile[0]
            capeImage = Image.open(capeNameDirImage).convert("RGBA")
            capeImage = capeImage.crop((0, 0, 32, 32))
            capeImage.save(capeNameDirImage)
            print('Resized Cape to fit Normal Format')
            mainFiles()
    elif SkinOrCape == '1':
        if Name in NameList:
            manageCapeFolders()
            manageFolders()
            writeJson()
            openUnreal()
            cookAssets()
            copyCookedFiles()
            packageMod()
        else:
            print('Error: Name is Incorrect')
    else:
        print('Error: File Selection is Incorrect')
if sys.argv[2] == "''":
    SkinOrCape = input("Do you want to Import a Skin or Cape? (1 = Skin, 2 = Cape) : ")
    print('File Selection: ' + SkinOrCape)
    if SkinOrCape == '2':
        RequesterName = input("Enter the Requesters Name : ")
        print('Requesters Name: ' + RequesterName)
        sys.argv = ['', '', '', '', '', '']
        delSkinFolders()
        mainFiles()
    elif SkinOrCape == '1':
        if sys.argv[1] == "''":
            Format = input("What format is the Skin in? (1 = JavaSteve, 2 = JavaAlex) : ")
        else:
            Format = sys.argv[1]
        IncludeEyes = input("Do you want to Include Eyes? (1 = Yes, 2 = No) : ")
        print('Include Eyes: ' + IncludeEyes)
        RequesterName = input("Enter the Requesters Name : ")
        print('Requesters Name: ' + RequesterName)
        Name = input("Enter Skin to Replace (Ex. Alex, Steve, etc.) with Correct Capitalization - List of Names is in Scripts/Names.txt : ")
        print('Name: ' + Name)
        skinFormat()
        sys.argv = ['', '', '', '', '', '']
else:
    SkinOrCape = sys.argv[2]
    RequesterName = sys.argv[3]
    Name = sys.argv[4]
    IncludeEyes = sys.argv[5]
    if SkinOrCape == '2':
        delSkinFolders()
        mainFiles()
    elif SkinOrCape == '1':
        Format = sys.argv[1]
        delCapeFolders()
        skinFormat()