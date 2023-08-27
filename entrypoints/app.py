from math import pi
from random import randint

from pytmlib import AbstractExercise
from pytmlib import entrypoint


class Exercise(AbstractExercise):
    _epsilon = 0.01
    _hint = r'''
    $$d = 2r$$
    $$C = d\pi$$
    $$A = r^{2}\pi$$
    '''

    @property
    def version(self) -> str:
        return '0.1.0'

    @entrypoint
    def start(self):
        return self.output \
            .add_action('Diameter', self.diameter) \
            .add_action('Circumference', self.circumference) \
            .add_action('Area', self.area)

    @entrypoint
    def diameter(self):
        """
        Calculate the diameter of a circle.
        """
        radius = randint(1, 100)

        return self.output \
            .add_latex('Calculate the diameter of a circle with radius %f.' % radius) \
            .add_latex(self._hint) \
            .add_number_field(name='diameter', label='Diameter', step=self._epsilon) \
            .add_action('Solve', self.solve, radius=radius)

    @entrypoint
    def circumference(self):
        radius = randint(1, 100)

        return self.output \
            .add_latex('Calculate the circumference of a circle with radius %f.' % radius) \
            .add_latex(self._hint) \
            .add_number_field(name='circumference', label='Circumference', step=self._epsilon) \
            .add_action('Solve', self.solve, radius=radius)

    @entrypoint
    def area(self):
        radius = randint(1, 100)

        return self.output \
            .add_latex('Calculate the area of a circle with radius %f.' % radius) \
            .add_latex(self._hint) \
            .add_number_field(name='area', label='Area', step=self._epsilon) \
            .add_action('Solve', self.solve, radius=radius)

    def solve(self, **kwargs):
        score = 1.0 if self.check(**kwargs) else 0.0

        _ = kwargs.pop('radius')
        attribute, _ = kwargs.popitem()
        method = getattr(self, attribute, self.start)

        return self.output \
            .add_score(score) \
            .add_paragraph(f'Your score: {score}') \
            .add_action('Back', method)

    @classmethod
    def check(cls, radius, diameter=None, circumference=None, area=None):
        if diameter is not None:
            return radius * 2 == diameter
        if circumference is not None:
            return abs(radius * 2 * pi - circumference) < cls._epsilon
        if area is not None:
            return abs(radius * radius * pi - area) < cls._epsilon
        return False


app = Exercise()
