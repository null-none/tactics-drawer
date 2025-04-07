import cv2

from tactics_drawer.utils import TacticsDrawer

pitch = TacticsDrawer(cv2.imread("pitch.png"))

pitch.draw_arrow((100, 100), (200, 150), color="green")
pitch.draw_filled_circle((50, 50), radius=12, color="red")
pitch.draw_cross((150, 150), size=10, color="green")

pitch.save("annotated_output.jpg")