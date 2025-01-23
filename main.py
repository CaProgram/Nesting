print("sports or commedy?")
print("_______________")
favoriteShow = input ("Do you perfer to watch sports or commedy?")
if favoriteShow == "sports":
  print("So you must like the competitve seen!")
  favoriteSport = input("Do you perfer to watch basketball or football? ")
  if favoriteSport == "football":
    print("You must be a football fan!")
  else:
    print("You must be a basketball fan!")
elif favoriteShow == "commedy":
      print("You must like a good laugh!")
      favoriteActor = input("Do you perfer to watch Tom Cruse or Jim Carrey? ")
      if favoriteActor == "Jim Carrey":
        print("You must be a funny guy!")
      else:
        print("Tom Cruse is not that funny")