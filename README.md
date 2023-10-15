 Conway's Game of Life

Description: This project is inspired by Tech With Tim's tutorial a

Adding Cells: By clicking on the grid, you can add or remove cells. Clicking on a cell toggles its state (alive or dead).

Start/Pause: You can start and pause the simulation by pressing the spacebar. When the simulation is running, the cells will evolve based on certain rules.

Clear Grid: Pressing the 'c' key clears the grid, resetting all cells to the dead state.

Generate Random Cells: Pressing the 'g' key generates a random set of alive cells on the grid.

Game Logic:
The game follows the rules of Conway's Game of Life:

A live cell with 2 or 3 live neighbors survives.
A dead cell with exactly 3 live neighbors becomes alive.
All other live cells die, and all other dead cells remain dead.
The grid is updated at a set frequency, and cells evolve based on these rules.

Code:
The code is implemented in Python using Pygame. It initializes a grid, allows you to interact with it, and visualizes the state of the cells on the screen.

## Acknowledgments

Tech With Tim:This project draws inspiration from Tech With Tim's tutorial on YouTube.
