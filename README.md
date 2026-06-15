# Command-Line Blackjack Game

A fully functional, interactive Blackjack game built from scratch using Python. The game runs entirely in the terminal and accurately simulates real casino dealer behavior and card deck tracking.

## 🃏 Features

* **Dynamic Ace Logic:** Includes a custom validation loop for both the player and the dealer. If a hand is about to bust (go over 21), the game automatically scans the hand and converts Aces from `11` to `1` to keep the player alive.
* **Realistic Deck Tracking:** Uses a standard multi-deck shoe structure. When cards are dealt or drawn, they are permanently removed from the deck array so they cannot be duplicated.
* **Instant Win Check:** Instantly checks for "Natural Blackjacks" (21 on the opening deal) for both the user and computer before the hitting rounds begin.
* **Smart Dealer AI:** The computer follows classic casino rules, automatically hitting on any total under 17 and standing once it hits 17 or higher.
* **Clean Endgame Logic:** Handles complex score evaluations including player busts, dealer busts, ties (pushes), and high-score wins without overlapping print statements.

## 🚀 How to Play

1. Make sure you have Python installed on your computer.
2. Download or clone this repository.
3. Open your terminal or command prompt, navigate to the folder, and run:
   ```bash
   python blackjack.py
   ```
4. Follow the on-screen prompts to `hit` or `stand`!
