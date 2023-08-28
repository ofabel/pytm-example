from enum import StrEnum
from math import pi
from random import randint

from pytmlib import AbstractExercise
from pytmlib import entrypoint


class Circle(StrEnum):
    DIAMETER = 'diameter'
    CIRCUMFERENCE = 'circumference'
    AREA = 'area'


class Exercise(AbstractExercise):
    _operations = {
        Circle.DIAMETER.value: lambda r: r * 2,
        Circle.CIRCUMFERENCE.value: lambda r: r * 2 * pi,
        Circle.AREA.value: lambda r: r * r * pi
    }
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
            .add_latex(r'''
            Calculate the diameter of a circle with radius %f.
            ''' % radius) \
            .add_latex(self._hint) \
            .add_number_field(name=Circle.DIAMETER,
                              label='Diameter',
                              step=self._epsilon) \
            .add_action('Solve', self.solve, radius=radius)

    @entrypoint
    def circumference(self):
        radius = randint(1, 100)

        return self.output \
            .add_latex(r'''
            Calculate the circumference of a circle with radius %f.
            ''' % radius) \
            .add_latex(self._hint) \
            .add_number_field(name=Circle.CIRCUMFERENCE,
                              label='Circumference',
                              step=self._epsilon) \
            .add_action('Solve', self.solve, radius=radius)

    @entrypoint
    def area(self):
        radius = randint(1, 100)

        return self.output \
            .add_latex(r'''
            Calculate the area of a circle with radius %f.
            ''' % radius) \
            .add_latex(self._hint) \
            .add_number_field(name=Circle.AREA,
                              label='Area',
                              step=self._epsilon) \
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
    def check(cls, radius, **kwargs):
        attribute, value = kwargs.popitem()

        if attribute not in cls._operations:
            return False

        operation = cls._operations.get(attribute)

        return abs(operation(radius) - value) < cls._epsilon


app = Exercise()
