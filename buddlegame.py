import cv2

# Initial position of the circle
circle_x, circle_y = 100, 100

# Function to update circle position
def update_circle(event, x, y, flags, param):
    global circle_x, circle_y
    if event == cv2.EVENT_MOUSEMOVE:
        circle_x, circle_y = x, y

# Create a window and set the mouse callback
cv2.namedWindow('Game Window')
cv2.setMouseCallback('Game Window', update_circle)

while True:
    # Create a black window
    frame = cv2.imread('black.png')

    # Draw the circle at the current position
    cv2.circle(frame, (circle_x, circle_y), 20, (0, 0, 255), -1)

    # Display the frame
    cv2.imshow('Game Window', frame)

    # Exit the game when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the window and close it
cv2.destroyAllWindows()
