import cv2


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

        # Only two allowed colors: red and green
        self.colors = {"red": (0, 0, 255), "green": (0, 255, 0)}

    def _get_color(self, color):
        """
        Convert color name to BGR. Default is green if invalid.

        :param color: "red" or "green"
        :return: BGR color tuple
        """
        return self.colors.get(color.lower(), self.colors["green"])

    def draw_arrow(self, pt1, pt2, color="green", thickness=2, tip_length=0.2):
        """
        Draw an arrow from pt1 to pt2.

        :param pt1: Starting point (x, y)
        :param pt2: Ending point (x, y)
        :param color: "red" or "green"
        :param thickness: Arrow line thickness
        :param tip_length: Arrowhead size (0.0 to 1.0)
        """
        cv2.arrowedLine(
            self.image,
            pt1,
            pt2,
            self._get_color(color),
            thickness,
            tipLength=tip_length,
        )

    def draw_circle(self, center, radius=5, color="red", thickness=2):
        """
        Draw a circle (not filled) at the given center.

        :param center: Center of the circle (x, y)
        :param radius: Radius of the circle
        :param color: "red" or "green"
        :param thickness: Line thickness
        """
        cv2.circle(self.image, center, radius, self._get_color(color), thickness)

    def draw_filled_circle(self, center, radius=5, color="red"):
        """
        Draw a filled circle at the given center.

        :param center: Center of the circle (x, y)
        :param radius: Radius of the circle
        :param color: "red" or "green"
        """
        cv2.circle(self.image, center, radius, self._get_color(color), thickness=-1)

    def draw_cross(self, center, size=10, color="red", thickness=2):
        """
        Draw a cross ("+") centered at the given point.

        :param center: Center of the cross (x, y)
        :param size: Half-length of cross arms
        :param color: "red" or "green"
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
