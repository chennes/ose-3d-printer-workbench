
from ose3dprinter.app.enums import AxisOrientation

from .add_universal_axis_base import AddUniversalAxisBase


class AddUniversalYAxis:
    """
    Command to add Universal Y Axis object.
    """

    NAME = 'AddUniversalYAxis'

    def __init__(self):
        self.base = AddUniversalAxisBase(AxisOrientation.Y)

    def Activated(self):
        self.base.Activated()

    def IsActive(self):
        return self.base.IsActive()

    def GetResources(self):
        return self.base.GetResources()