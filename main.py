import time
def main():
  am = 0
  for i in range(1,101):
    print('\n')
  print("Welkom bij HoekFinder!")
  graden = input('Wat is het aantal graden van je hoek?\n')
  if int(graden) > 360:
    print("Het aantal graden moet nog niet hoger zijn dan 360, lager maken....")
    while int(graden) > 360:
      graden = int(graden) - 360
      if am == 1:
        print(graden)
      continue
  print('Berekenen hoeksoort...')
  g = graden
  if g == 0:
    print('Error, graden 0 is niet mogelijk.')
  else:
    if g == 360:
      print('Het is een volle hoek')
      time.sleep(4)
      main()
    if int(g) == 180:
      print('Het is een gestrekte hoek')
      time.sleep(4)
      main()
    if int(g) == 90:
      print('Het is een rechte hoek.')
      time.sleep(4)
      main()
    if int(g) < 90:
      print('Het is een scherpe hoek.')
      time.sleep(4)
      main()
    if int(g) > 90:
      print('Het is een stompe hoek.')
      time.sleep(4)
      main()
main()