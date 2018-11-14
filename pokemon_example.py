vida_pikachu = 100
vida_enemigo = 0
ataque_pokemon = 0
pokemon_elegido = input("contra que pokemon quieres combatir? ( squirtle / charmander / bulbasaur): ")

if pokemon_elegido == "charmander":
    vida_enemigo = 80
    nombre_pokemon = "charmander"
    ataque_pokemon = 7
elif pokemon_elegido == "squirtle":
    vida_enemigo = 90
    nombre_pokemon = "squirtle"
    ataque_pokemon = 8
elif pokemon_elegido == "bulbasaur":
    vida_enemigo = 100
    nombre_pokemon = "bulbasaur"
    ataque_pokemon = 10

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("que ataque quieres usar? (chispazo / vola voltio):")
    if ataque_elegido == "chispazo":
        vida_enemigo -= 10
        print("haz hecho 10 de daño")
    elif ataque_elegido == "vola voltio":
        vida_enemigo -= 12
        print("haz hecho 12 de daño")
    print("la vida de {} ahora es de {}".format(nombre_pokemon ,vida_enemigo))
    print("{} te hace un ataque de {}".format(nombre_pokemon , ataque_pokemon))
    vida_pikachu -= ataque_pokemon
    print("la vida de pikachu ahora es de {}".format(vida_pikachu))
    if vida_pikachu <= 0:
        print("¡haz perdido!")

    elif vida_enemigo <= 0:
        print("¡haz ganado!")

print("el combate ha terminado")
input("quieres volver a combatir?:")