from tkinter import *
import random

user_score=0
computer_score=0
def play_game(user):
    choices = {'Rock': 0, 'Paper': 1, 'Scissors': 2}
    computer = random.choice(list(choices.keys()))
    result = winner(choices[user],choices[computer])
    result_screen.config(text=f"User choice: {user} \n"
                              f"Computer choice: {computer} \n"
                              f"{result}\n"
                              f"User score: {user_score}\n"
                              f"Computer score: {computer_score}")
    return 0

def winner(user,computer):
    global user_score,computer_score
    if user==computer:
        return "It's a tie"
    elif (user-computer)%3 == 1:
        user_score+=1
        return "User wins"
    else:
        computer_score+=1
        return "User loses"

root = Tk()
root.title("Rock Paper Scissors Game")

screen = Label(root, text="Choose rock, paper or scissors", width=92, height=6, bg="black", fg="white", font=('Times', 20))
rock_button = Button(root, text="Rock", command=lambda: play_game('Rock'), width=30, height=5, bg="red", fg="white", font=('Times', 20))
paper_button = Button(root, text="Paper", command=lambda: play_game('Paper'), width=30, height=5, bg="blue", fg="white", font=('Times', 20))
scissors_button = Button(root, text="Scissors", command=lambda: play_game('Scissors'), width=30, height=5, bg="green", fg="white", font=('Times', 20))
screen.grid(row=0, column=0, columnspan=3)
rock_button.grid(row=1, column=0)
paper_button.grid(row=1, column=1)
scissors_button.grid(row=1, column=2)
result_screen = Label(root, text="", width=92, height=6, bg="black", fg="white", font=('Times', 20))
result_screen.grid(row=2, column=0, columnspan=3)
root.mainloop()