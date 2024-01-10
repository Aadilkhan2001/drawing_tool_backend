from django.db import models
from django.contrib.auth.models import User

SHAPE_CHOICES = (
    ('RECTANGLE', 'RECTANGLE',),
    ('LINE', 'LINE',),
    ('CIRCLE', 'CIRCLE',),
    ('SQUARE', 'SQUARE',),
    ('TRIANGLE', 'TRIANGLE',),
    ('OVAL', 'OVAL',),
    ('ARROW', 'ARROW',),
    ('HEXAGON', 'HEXAGON',),
    ('PENTAGON', 'PENTAGON',),
    ('STAR', 'STAR',),
)

class Drawing(models.Model):
    """
    Model representing a drawing.

    Fields:
        - name (str): The name of the drawing.
        - user (User): The user who created the drawing.
        - created_at (datetime): The timestamp when the drawing was created.
        - height (float): Indicates height of the shape.
        - width (bool): Indicates width of the shape.
    """

    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    height = models.FloatField()
    width = models.FloatField()

    def __str__(self) -> str:
        return str(self.id)


class Shape(models.Model):
    """
    Model representing a shape within a drawing.

    Fields:
        - drawing (Drawing): The drawing to which the shape belongs.
        - shape_type (str): The type of the shape, chosen from predefined options.
        - coordinates (str): The coordinates of the shape.
        - dimensions (str, optional): The dimensions of the shape (optional).
        - is_selected (bool): Indicates whether the shape is selected.
        - height (float): Indicates height of the shape.
        - width (bool): Indicates width of the shape.
    """

    drawing = models.ForeignKey(Drawing, on_delete=models.SET_NULL, null=True)
    shape_type = models.CharField(max_length=50, choices=SHAPE_CHOICES,)
    coordinates = models.TextField()
    dimensions = models.TextField(blank=True, null=True)
    is_selected = models.BooleanField(default=False)
    height = models.FloatField()
    width = models.FloatField()

    def __str__(self) -> str:
        return str(self.id)

class Annotation(models.Model):
    """
    Model representing an annotation for a shape.

    Fields:
        - shape (Shape): The shape to which the annotation is associated.
        - text (str): The text content of the annotation.
        - position (str): The position of the annotation.
    """

    shape = models.ForeignKey(Shape, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    position = models.TextField()

    def __str__(self) -> str:
        return str(self.id)