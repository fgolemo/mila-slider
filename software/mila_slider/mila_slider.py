from numpy import sum
from functools import partial

from pypot.creatures import AbstractPoppyCreature
from pypot.creatures.ik import IKChain


class MilaSlider(AbstractPoppyCreature):
    @classmethod
    def setup(cls, robot):
        robot._primitive_manager._filter = partial(sum, axis=0)

        c = IKChain.from_poppy_creature(robot,
                                        motors=robot.motors,
                                        passiv=[],
                                        tip=[0, 0, -0.07])

        robot.chain = c


        for m in robot.motors:
            m.pid = (4, 2, 0)
            m.torque_limit = 70.
            m.led = 'off'

