# Tractor
##### Introduction
Tractor is a Chinese card game similar to games likes Bridge, Hearts, Spades and Euchre. As a child, I watched my parents playing this complicated game at gatherings and parties. Once I learned this game, it became my favorite card game. 

##### Rules of the Game
Rules of Tractor can be found at [http://www.pagat.com/kt5/tractor.html](http://www.pagat.com/kt5/tractor.html).

##### Version
1.0 

##### Version Log

###### Version 1.0.0
This version contains the basic structure for the game's simplest variant and completely implemented in java. In the context of this project, basic means:
- there are four players, split evenly into two teams
- there are two decks of 54 cards (13 per suit, 4 suits, small joker, big joker)
- players are able to play single cards, pairs and tractors, but not sets of cards
- overriding trump suits can only happen before the bottom cards are picked up, not after

###### Version 1.0.1
Added README.

###### Version 1.0.2
- Added CardCollection class to abstract away a lot of shared functions.
- Fixed a bug with end of round calculations.

###### Version 1.0.3
- Fixed README formatting.

###### Version 1.0.4
- Refactoring down technical debt

###### Version 1.0.5
- Fixed bug in checkBottom()

###### Version 1.0.6
- Fixed bug in first trick / player cycling

###### Version 1.1.0
- Complete translation into python

###### Version 1.1.1
- Removed extraneous comments and files

###### Version 1.1.2
- Untangled dependencies and separated code into multiple files.

###### Version 1.1.3
- Refactored down more unnecessary code

###### Version 1.1.4
- Refactored code dealing with debug code

[Pagat]:<http://www.pagat.com/kt5/tractor.html>