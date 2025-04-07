# tactics-drawer

Tactics Drawer 


```python
import cv2

from tactics_drawer.utils import TacticsDrawer

painter = TacticsDrawer(cv2.imread("pitch.png"))

painter.draw_arrow((100, 100), (200, 150), color="green")
painter.draw_filled_circle((50, 50), radius=12, color="red")
painter.draw_cross((150, 150), size=10, color="green")

painter.save("annotated_output.jpg")
```

![area](examples/annotated_output.jpg?raw=true)
