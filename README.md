# snake
Classic Snake: Real-Time Arcade Game
An event-driven desktop game featuring dynamic growth logic and coordinate-based collision systems.

Tech Stack
-Language: Python 
-Library: Tkinter (Canvas API for graphics)

Key Features
-Dynamic Growth System
-The game features a "Snake" and "Food" class structure
-Class-Based Architecture: The Snake class manages a list of body coordinates and canvas objects, while the Food class handles random spawning within the grid.
-Eat & Grow Logic: When the snake's head coordinates match the food's coordinates, the score increases, a new food item spawns, and the snake's tail is not deleted, allowing it to grow longer.

Physics & Collision Detection
I implemented a multi-layered validation system to ensure fair play:

-Boundary Checks: Detects if the snake's head coordinates get outside of the GAME_WIDTH or GAME_HEIGHT.

-Self-Collision: Scans the entire list of body coordinates to see if the head has overlapped with any other part of the body.


//Python
if check_collisions():
    game_over()
else:
    game.after(SPEED, next_turn) # Schedules the next frame
Incoming changes:
- Speed Scaling: Increase the SPEED variable as the score gets higher to make the game more challenging.

- High Score Persistence: Use a text file or local database to save the user's all-time highest score.

- Obstacles: Add "Wall" objects in the middle of the map that trigger a Game Over.
