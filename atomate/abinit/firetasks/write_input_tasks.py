# coding: utf-8


"""
This module defines tasks to write inputs for Abinit or other related executables.
"""


from fireworks import explicit_serialize, FiretaskBase

from atomate.utils.utils import get_logger


__all__ = ("WriteInput",)


logger = get_logger(__name__)

__author__ = 'David Waroquiers'
__email__ = 'david.waroquiers@uclouvain.be'



@explicit_serialize
class WriteInput(FiretaskBase):
    """
    Write input for Abinit.

    TODO: define if/what are required/optional params
    """

    required_params = []
    optional_params = []

    def run_task(self, fw_spec):
        raise NotImplementedError

