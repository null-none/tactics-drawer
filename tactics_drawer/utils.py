import cv2
import math


class TacticsDrawer:
    def __init__(self, image):
        """
        Initialize the painter with a valid image.

        :param image: OpenCV image (numpy array)
        :raises ValueError: If the image is None
        """
        if image is None:
            raise ValueError(
                "Invalid image: received None. Make sure the image is loaded correctly."
            )
        self.image = image.copy()

        # Only two allowed colors: red and black
        self.colors = {"red": (0, 0, 255), "black": (0, 0, 0), "blue": (255, 0, 0)}

    def _get_color(self, color):
        """
        Convert color name to BGR. Default is black if invalid.

        :param color: "red" or "black"
        :return: BGR color tuple
        """
        return self.colors.get(color.lower(), self.colors["black"])

    def draw_arrow(self, pt1, pt2, color="black", thickness=1, head_size=6):
        """
        Draw an arrow with a consistent arrowhead size regardless of line length.

        :param pt1: Start point (x, y)
        :param pt2: End point (x, y)
        :param color: 'red' or 'black'
        :param thickness: Line thickness
        :param head_size: Length of arrowhead sides (default: 10)
        """
        color_bgr = self._get_color(color)

        # Draw main line
        cv2.line(self.image, pt1, pt2, color_bgr, thickness)

        # Compute angle of the line
        dx = pt2[0] - pt1[0]
        dy = pt2[1] - pt1[1]
        angle = math.atan2(dy, dx)

        # Arrowhead points (two lines forming a "V")
        left = (
            int(pt2[0] - head_size * math.cos(angle - math.pi / 6)),
            int(pt2[1] - head_size * math.sin(angle - math.pi / 6)),
        )
        right = (
            int(pt2[0] - head_size * math.cos(angle + math.pi / 6)),
            int(pt2[1] - head_size * math.sin(angle + math.pi / 6)),
        )

        # Draw arrowhead "wings"
        cv2.line(self.image, pt2, left, color_bgr, thickness)
        cv2.line(self.image, pt2, right, color_bgr, thickness)

    def draw_circle(self, center, radius=5, color="red", thickness=1):
        """
        Draw a circle (not filled) at the given center.

        :param center: Center of the circle (x, y)
        :param radius: Radius of the circle
        :param color: "red" or "black"
        :param thickness: Line thickness
        """
        cv2.circle(self.image, center, radius, self._get_color(color), thickness)
        cv2.circle(self.image, center, radius - 4, self._get_color(color), thickness=-1)

    def draw_filled_circle(self, center, radius=5, color="red"):
        """
        Draw a filled circle at the given center.

        :param center: Center of the circle (x, y)
        :param radius: Radius of the circle
        :param color: "red" or "black"
        """
        cv2.circle(self.image, center, radius, self._get_color(color), thickness=-1)

    def draw_cross(self, center, size=6, color="red", thickness=1):
        """
        Draw a cross ("+") centered at the given point.

        :param center: Center of the cross (x, y)
        :param size: Half-length of cross arms
        :param color: "red" or "black"
        :param thickness: Line thickness
        """
        x, y = center
        c = self._get_color(color)
        cv2.line(self.image, (x - size, y), (x + size, y), c, thickness)  # horizontal
        cv2.line(self.image, (x, y - size), (x, y + size), c, thickness)  # vertical

    def get_result(self):
        """
        Return the final modified image.

        :return: Modified image (numpy array)
        """
        return self.image

    def show(self, window_name="Image"):
        """
        Display the image in a window.

        :param window_name: Title of the window
        """
        cv2.imshow(window_name, self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def save(self, filename):
        """
        Save the final image to a file.

        :param filename: Output path (e.g., "output.jpg")
        """
        cv2.imwrite(filename, self.image)
