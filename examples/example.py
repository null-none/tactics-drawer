import cv2

from tactics_drawer.utils import TacticsDrawer

# Load image (make sure path is correct)
img = cv2.imread("pitch.png")

# Create painter
painter = TacticsDrawer(img)

# Draw some shapes
painter.draw_arrow((100, 100), (200, 150), color="green")
painter.draw_filled_circle((50, 50), radius=12, color="red")
painter.draw_cross((150, 150), size=10, color="green")

# Save result to file
painter.save("annotated_output.jpg")
