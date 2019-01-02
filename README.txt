Conner Delahanty
Spring, 2018

The objective of this project is to create a solver for the game Codenames.

Codenames is a popular strategy game where two teams, each with one player designated the "spymaster" and the rest
designated "teamates", attempt to reveal words on a board. The board consists of 5x5 words, and the spymasters 
must give a clue of the format "<word>, <number>" meaning that the other players must try and use the <word> as a 
clue to select a <number> of words that pertain to the clue. The first team to reveal their alloted set of words 
wins!

This project's goal is to, given the words on the board and the objective words, using similiarity indicies and 
the Datamuse API (a word similiarity ranking service), create the perfect clue to reveal as many words as possible.
This is playing the game perfectly from the spymaster side.

The second goal of the project is to, given this word and number clue, determine the words to choose.
This is playing the game perfect from the teamate side.