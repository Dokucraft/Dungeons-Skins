from PIL import Image

def displace(skinFormat, skinFile, keepEyesAndMouth = False):
  javaSkin = Image.open(skinFile).convert('RGBA')
  size = javaSkin.width
  m = int(size / 64)

  dispMap = Image.open('Scripts/displacement_maps/' + skinFormat.lower() + str(size) + '.png').convert('RGBA')

  dungeonsSkin = Image.new('RGBA', (size, size), (255, 255, 255, 0))

  for x in range(0, size):
    for y in range(0, size):
      d = dispMap.getpixel((x, y))

      if d[3] > 0:
        dungeonsSkin.putpixel((x, y), javaSkin.getpixel(d[0:2]))

  # Portait Base Layer
  skinFace = dungeonsSkin.crop((8*m, 8*m, 16*m, 16*m))
  dungeonsSkin.paste(skinFace, (56*m, 20*m))
  # Portait Overlay
  skinFaceOverlay = dungeonsSkin.crop((40*m, 8*m, 48*m, 16*m))
  dungeonsSkin.paste(skinFaceOverlay, (56*m, 20*m), skinFaceOverlay)

  if keepEyesAndMouth:
    skinSclera = javaSkin.crop((6*m, 6*m, 8*m, 7*m))
    dungeonsSkin.paste(skinSclera, (6*m, 6*m))
    dungeonsSkin.paste(skinSclera, (57*m, 24*m), skinSclera)
    dungeonsSkin.paste(skinSclera, (61*m, 24*m), skinSclera)

    skinPupil = javaSkin.crop((7*m, 5*m, 8*m, 6*m))
    dungeonsSkin.paste(skinPupil, (7*m, 5*m))
    dungeonsSkin.paste(skinPupil, (58*m, 24*m), skinPupil)
    dungeonsSkin.paste(skinPupil, (61*m, 24*m), skinPupil)

    skinMouth = javaSkin.crop((6*m, 7*m, 8*m, 8*m))
    dungeonsSkin.paste(skinMouth, (6*m, 7*m))
    dungeonsSkin.paste(skinMouth, (59*m, 26*m), skinMouth)

  return dungeonsSkin