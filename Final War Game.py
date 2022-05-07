from itertools import count
from tkinter import *
import random
from PIL import Image, ImageTk


root = Tk()
root.title('Card Deck')
root.iconbitmap()
root.geometry("900x550")
root.configure(background="green")

# Resize cards
def resize_cards(card):
      # Open images
      our_card_img = Image.open(card)

      # Resize image
      our_card_resize_image = our_card_img.resize((150, 218))

      #output card
      global our_card_image
      our_card_image = ImageTk.PhotoImage(our_card_resize_image)

      # Return card
      return our_card_image

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
  global dealer, player, dscore, pscore
  dealer = []
  player = []
  dscore = []
  pscore = []
  
  # Grab Random Card
  dealer_card = random.choice(deck)
  # Remove Card from Deck
  deck.remove(dealer_card)
  # Append Card to Dealer List
  dealer.append(dealer_card)
  # Output Card to Screen
  global dealer_image
  dealer_image = resize_cards(f'images/cards/{dealer_card}.png')
  dealer_label.config(image=dealer_image)

  #dealer_label.config(text=card)
  
  # Grab Random Card
  player_card = random.choice(deck)
  # Remove Card from Deck
  deck.remove(player_card)
  # Append Card to Dealer List
  player.append(player_card)
  # Output Card to Screen
  global player_image
  player_image = resize_cards(f'images/cards/{player_card}.png')
  player_label.config(image=player_image)

  #player_label.config(text=card)
  
  # Remaining Cards in Title Bar
  root.title(f'Card Deck - {len(deck)} Cards Left')

  # Get the score
  score(dealer_card, player_card)
  
# Deal Cards
def deal_cards():
    try:
  # Get Dealer Card
        dealer_card = random.choice(deck)
  # Remove Card from Deck
        deck.remove(dealer_card)
  # Append Card to Dealer List
        dealer.append(dealer_card)
  # Output Card to Screen
        global dealer_image
        dealer_image = resize_cards(f'images/cards/{dealer_card}.png')
        dealer_label.config(image=dealer_image)
        #dealer_label.config(text=card)
    
  # Get Player Card
        player_card = random.choice(deck)
  # Remove Card from Deck
        deck.remove(player_card)
  # Append Card to Dealer List
        player.append(player_card)
  # Output Card to Screen
  # Output Card to Screen
        global player_image
        player_image = resize_cards(f'images/cards/{player_card}.png')
        player_label.config(image=player_image)
        #player_label.config(text=card)
  
  # Remaining Cards in Title Bar
        root.title(f'Card Deck - {len(deck)} Cards Left')
  # Get the score
        score(dealer_card, player_card)
    
    except:
            # Tie
            if dscore.count("x") == pscore.count("x"):
                  root.title(f'Card Deck - No Cards In Deck! Tie! {dscore.count("x")} to {pscore.count("x")}')
            # Dealer Wins
            elif dscore.count("x") > pscore.count("x"):
                  root.title(f'Card Deck - No Cards In Deck! Dealer Wins! {dscore.count("x")} to {pscore.count("x")}')
            # Player Wins
            else:
                  root.title(f'Card Deck - No Cards In Deck! Player Wins! {pscore.count("x")} to {dscore.count("x")}')
  
def score(dealer_card, player_card):
      # Split out numbers
      dealer_card = int(dealer_card.split("_", 1)[0])
      player_card = int(player_card.split("_", 1)[0])

      # Compare Card Numbers
      if dealer_card == player_card:
            score_label.config(text="Tie! Play Again!")

      elif dealer_card > player_card:
            score_label.config(text="Dealer Wins!")
            dscore.append("x")
      else:
            score_label.config(text="Player Wins!")
            pscore.append("x")

      root.title(f'Card Deck - {len(deck)} Cards Left |     Dealer: {dscore.count("x")}      Player: {pscore.count("x")}')
      

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

# Create Score Label
score_label = Label(root, text="", font=("Helvetica", 14), bg="green")
score_label.pack(pady=20)

# Create Buttons
shuffle_button = Button(root, text="Shuffle Deck", font=("Helvetica", 14), command=shuffle)
shuffle_button.pack(pady=20)

card_button = Button(root, text="Get Cards", font=("Helvetica", 14), command=deal_cards)
card_button.pack(pady=20)

shuffle()

root.mainloop()