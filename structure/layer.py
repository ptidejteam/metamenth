import uuid
from datatypes.interfaces import AbstractMeasure
from structure.material import Material
from misc import Validate


class Layer:
    """
    A layer in the envelope of a building

    Author: Peter Yefi
    Email: peteryefi@gmail.com
    """
    def __init__(
        self,
        height: AbstractMeasure,
        length: AbstractMeasure,
        thickness: AbstractMeasure,
        material: Material,
        has_vapour_barrier: bool = False,
        has_air_barrier: bool = False,

    ):

        self._UID = str(uuid.uuid4())  # Generate a unique identifier
        self._height = height
        self._length = length
        self._thickness = thickness
        self._has_vapour_barrier = has_vapour_barrier
        self._has_air_barrier = has_air_barrier
        self._material = material

    @property
    def UID(self):
        return self._UID

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value is None:
            raise ValueError("height should be of type BinaryMeasure")
        self._height = value

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value is None:
            raise ValueError("length should be of type BinaryMeasure")
        self._length = value

    @property
    def thickness(self):
        return self._thickness

    @thickness.setter
    def thickness(self, value):
        if value is None:
            raise ValueError("thickness should be of type BinaryMeasure")
        self._thickness = value

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        if value is None:
            raise ValueError("material cannot be None")
        self._material = value

    @property
    def has_vapour_barrier(self):
        return self._has_vapour_barrier

    @has_vapour_barrier.setter
    def has_vapour_barrier(self, value):
        self._has_vapour_barrier = value

    @property
    def has_air_barrier(self):
        return self._has_air_barrier

    @has_air_barrier.setter
    def has_air_barrier(self, value):
        self._has_air_barrier = value

    def __str__(self):
        material_str = f"Material: {str(self.material)}" if self.material else "Material: None"
        return (
            f"Layer("
            f"UID: {self.UID}, "
            f"Height: {self.height.value} {self.height.measurement_unit}, "
            f"Length: {self.length.value} {self.length.measurement_unit}, "
            f"Thickness: {self.thickness.value} {self.thickness.measurement_unit}, "
            f"Vapour Barrier: {self.has_vapour_barrier}, "
            f"Air Barrier: {self.has_air_barrier}, "
            f"{material_str})"
        )
