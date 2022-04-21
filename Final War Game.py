from tkinter import *
import random


root = Tk()
root.title('Card Deck')
root.iconbitmap()
root.geometry("900x500")
root.configure(background="green")

# Shuffle Cards
def shuffle():
  # Define Deck
  suits = ["diamonds", "clubs", "hearts", "spades"]
  values = range(2, 15)
  # 11=Jack, 12=Queen, 13=King, 14=Ace
  
  global deck
  deck =[]
  
  for suit in suits:
    for value in values:
      deck.append(f'{value}_of_{suit}')
      
  # Create Players
  global dealer, player
  dealer = []
  player = []
  
  # Grab Random Card
  card = random.choice(deck)
  # Remove Card from Deck
  deck.remove(card)
  # Append Card to Dealer List
  dealer.append(card)
  # Output Card to Screen
  dealer_label.config(text=card)
  
  # Grab Random Card
  card = random.choice(deck)
  # Remove Card from Deck
  deck.remove(card)
  # Append Card to Dealer List
  player.append(card)
  # Output Card to Screen
  player_label.config(text=card)
  
  # Remaining Cards in Title Bar
  root.title(f'Card Deck - {len(deck)} Cards Left')
  
# Deal Cards
def deal_cards():
    try:
  # Get Dealer Card
        card = random.choice(deck)
  # Remove Card from Deck
        deck.remove(card)
  # Append Card to Dealer List
        player.append(card)
  # Output Card to Screen
        player_label.config(text=card)
    
  # Get Player Card
        card = random.choice(deck)
  # Remove Card from Deck
        deck.remove(card)
  # Append Card to Dealer List
        player.append(card)
  # Output Card to Screen
        player_label.config(text=card)
  
  # Remaining Cards in Title Bar
        root.title(f'Card Deck - {len(deck)} Cards Left')
    
    except:
            root.title(f'Card Deck - No Cards In Deck')
  
      

my_frame = Frame(root, bg="green")
my_frame.pack(pady=20)

# Frames for Cards
dealer_frame = LabelFrame(my_frame, text="dealer", bd=0)
dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text="player", bd=0)
player_frame.grid(row=0, column=1, ipadx=20)

# Put Cards in Frames
dealer_label = Label(dealer_frame, text='')
dealer_label.pack(pady=20)

player_label = Label(player_frame, text='')
player_label.pack(pady=20)

# Create Buttons
shuffle_button = Button(root, text="Shuffle Deck", font=("Helvetica", 14), command=shuffle)
shuffle_button.pack(pady=20)

card_button = Button(root, text="Get Cards", font=("Helvetica", 14), command=deal_cards)
card_button.pack(pady=20)


root.mainloop()
