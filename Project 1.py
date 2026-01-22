import random

pilihan = ["batu", "gunting", "kertas"]

player_choice = input("Pilih batu, gunting, atau kertas: ")
computer_choice = random.choice(pilihan)

print(f"Kamu memilih: {player_choice}.")
print(f"Komputer memilih: {computer_choice}.")

if player_choice == computer_choice:
    print("Seri!")

elif player_choice == "batu" and computer_choice == "gunting" :
    print("kamu menang")
elif player_choice == "gunting" and computer == "kertas" :
    print("kamu menang")
elif player_choice == "kertas" and computer == "batu" :
    print("kamu menang")

else:
    print("kamu kalah")
