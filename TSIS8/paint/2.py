import pygame

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width = 640
screen_height = 480

# Set the brush size
brush_size = 10

# Set the brush color
brush_color = (255, 0, 0)

# Create a Pygame display
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Paint")

# Set the background color
background_color = (255, 255, 255)

# Set the mouse position
mouse_x, mouse_y = 0, 0

# Set the mouse button state
left_button_down = False
right_button_down = False

# Set the clock
clock = pygame.time.Clock()

# Start the game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():

        # Check if the user wants to quit
        if event.type == pygame.QUIT:
            running = False

        # Check if a mouse button has been pressed
        elif event.type == pygame.MOUSEBUTTONDOWN:

            # Check if the left mouse button has been pressed
            if event.button == 1:
                left_button_down = True

            # Check if the right mouse button has been pressed
            elif event.button == 3:
                right_button_down = True

        # Check if a mouse button has been released
        elif event.type == pygame.MOUSEBUTTONUP:

            # Check if the left mouse button has been released
            if event.button == 1:
                left_button_down = False

            # Check if the right mouse button has been released
            elif event.button == 3:
                right_button_down = False

        # Check if a key has been pressed
        elif event.type == pygame.KEYDOWN:

            # Check if the user wants to clear the screen
            if event.key == pygame.K_c:
                screen.fill(background_color)

            # Check if the user wants to change the brush color
            elif event.key == pygame.K_r:
                brush_color = (255, 0, 0)
            elif event.key == pygame.K_g:
                brush_color = (0, 255, 0)
            elif event.key == pygame.K_b:
                brush_color = (0, 0, 255)

    # Get the mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Draw on the screen if the left mouse button is down
    if left_button_down:
        pygame.draw.circle(screen, brush_color, (mouse_x, mouse_y), brush_size)

    # Erase on the screen if the right mouse button is down
    if right_button_down:
        pygame.draw.circle(screen, background_color, (mouse_x, mouse_y), brush_size)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
