# coding: utf-8


"""
This module defines tasks that checks the proper execution of Abinit, and possibly takes appropriate measures to
correct errors or problems.
"""


from fireworks import explicit_serialize, FiretaskBase

from atomate.utils.utils import get_logger


__all__ = ("CheckTask", )


logger = get_logger(__name__)

__author__ = 'David Waroquiers'
__email__ = 'david.waroquiers@uclouvain.be'


@explicit_serialize
class CheckTask(FiretaskBase):
    """
    Check an Abinit Run and take appropriate corrections if errors occurred.
    """

    required_params = []
    optional_params = []

    def run_task(self, fw_spec):
        raise NotImplementedError
