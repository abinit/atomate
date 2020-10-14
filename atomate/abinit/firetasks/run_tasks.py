# coding: utf-8


"""
This module defines tasks to run Abinit or other related executables (e.g. anaddb, mrgddb, ...).
"""


from fireworks import explicit_serialize, FiretaskBase

from atomate.utils.utils import get_logger


__all__ = ("RunAbinit",
           "RunAnaDdb",)


logger = get_logger(__name__)

__author__ = 'David Waroquiers'
__email__ = 'david.waroquiers@uclouvain.be'



@explicit_serialize
class RunAbinit(FiretaskBase):
    """
    Run Abinit.

    TODO: define if/what are required/optional params
    """

    required_params = []
    optional_params = []

    def run_task(self, fw_spec):
        raise NotImplementedError


@explicit_serialize
class RunAnaDdb(FiretaskBase):
    """
    Run anaddb.

    TODO: define if/what are required/optional params
    """

    required_params = []
    optional_params = []

    def run_task(self, fw_spec):
        raise NotImplementedError
