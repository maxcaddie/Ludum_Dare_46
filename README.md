# Ludum_Dare_46

## Theme: Keep it alive

## Personal objective: 
* Export to Mac and Windows
* Finish!
* Implement an A* pathfinding algorthim
* Stretch (MinMax enemy)

## Title: TBC

### Description:
Turn based endless strategy game
9x9 Board
You have two tiles, when stacked can move 2 squares, otherwise 1 tile
There is an enemy who can AOE explode you, this causes a chain reaction
New enemies spawn with warning

### Technologies:
    - Python3.8.2
    - Pygame

### Plan:

#### Goal 0 Generate board
0.0: Represent board as a 2D array locally <br/>
0.1: Draw squares on screen <br/>
0.2: Leave a boarder around the edge <br/>

#### Goal 1 Player
1.0: Represent the player as positive ints in array <br/>
1.1: Update square on screen to have number of friendly <br/>
1.2: Click and select <br/>
1.3: Highlight tiles 2 away <br/>
1.4: Highlight all tiles reachable <br/>
1.5: Allow movements <br/>




## Documentation

### Use cases
1) The player opens the game
2) The player is able to see the board and the tokens
3) Player is able to select a tile
4) The player is able to move the selected token to a valid tile
4a) If the tile is not valid don't let the player move it there
5) Player is able to see tile move
6) Enemy is makes a move
7) Player is able to see the enemy move
8) Repeat 3-7 until all player tiles die
9) Stop game


## System Sequence Diagram
<img src="/Plan/SSD Use case 1.png"/>

## Class Diagram
<img src="/Plan/Class Diagram.png"/>

