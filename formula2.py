# declarations
points_bortoleto = 196.5
points_hadjar = 191
points_map = {
    1: 25, 2: 18, 3: 15, 4: 12, 5: 10,
    6: 8, 7: 6, 8: 4, 9: 2, 10: 1
}
fast_lap_points = 1

while True:
    try:
        # Input for Bortoletto position
        position_bortoletto = int(input("Digite a posição Bortoletto (somente números): "))
        if position_bortoletto < 1 or position_bortoletto > 22:
            print("Entrada inválida para Bortoletto! Deve ser entre 1 e 22.")
            continue
        
        # Input for Hadjar position
        position_hadjar = int(input("Digite a posição Hadjar (somente números): "))
        if position_hadjar < 1 or position_hadjar > 22:
            print("Entrada inválida para Hadjar! Deve ser entre 1 e 22.")
            continue
        
        # Adding points
        points_bortoleto += points_map.get(position_bortoletto, 0)
        points_hadjar += points_map.get(position_hadjar, 0)
        
        # fast lap
        fast_lap_winner = input("Volta rápida foi conquistada por (B para Bortoletto e H para Hadjar. Digite outra letra para outros)? ").strip().lower()
        if fast_lap_winner == "b":
            if (position_bortoletto > 11):
              points_bortoleto += fast_lap_points
        elif fast_lap_winner == "h":
              if (position_hadjar > 11):
                points_hadjar += fast_lap_points
        
        # Final Results
        print(f"Pontuação final Bortoletto: {points_bortoleto}")
        print(f"Pontuação final Hadjar: {points_hadjar}")

        if (points_bortoleto > points_hadjar):
            print("Bortoletto campeão!")
        elif (points_hadjar > points_bortoleto):
            print("Hadjar campeão :(")

        break  # Exit the loop after valid results
    
    except ValueError:
        print("Entrada inválida! Por favor, digite números inteiros.")
