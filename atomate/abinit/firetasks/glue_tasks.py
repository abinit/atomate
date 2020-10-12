# coding: utf-8


"""
This module defines tasks that acts as a glue between other Abinit Firetasks to allow communication
between different Firetasks and Fireworks.
"""


from fireworks import explicit_serialize, FiretaskBase

from atomate.utils.utils import get_logger
from atomate.common.firetasks.glue_tasks import CopyFiles

logger = get_logger(__name__)

__author__ = 'David Waroquiers'
__email__ = 'david.waroquiers@uclouvain.be'


@explicit_serialize
class CopyAbinitOutputs(CopyFiles):
    """
    Copy files from one or multiple previous Abinit run directories to the current directory.

    TODO: define what needs to be copied, what is required as inputs etc ... also think about a more general CopyFiles
    TODO: is this task needed or do we put everything in a ResolveDeps task or the ResolveDeps task just defines what needs to be copied to a general CopyFiles task ?
    """

    required_params = []
    optional_params = []

    def run_task(self, fw_spec):
        raise NotImplementedError


@explicit_serialize
class CreateAbinitFolders(FiretaskBase):
    """
    Firetask to create in, out and tmp folders for abinit.
    TODO: is it worth to allow changing them ??
    TODO: see if this should be a subclass of a general CreateFolders Task ? (there is the CreateFolder task that creates just ONE folder and optionally moves to it)

    Optional params:
        in_dir(str): Directory for abinit input files (e.g. _DEN file from previous calculation).
        out_dir(str): Directory for abinit output files (e.g. final _DEN file of the current calculation).
        tmp_dir(str): Directory for temporary abinit files during calculation.
    """

    required_params = []
    optional_params = ["in_dir", "out_dir", "tmp_dir"]

    def run_task(self, fw_spec):
        raise NotImplementedError


@explicit_serialize
class ResolveDeps(FiretaskBase):
    """
    Firetask resolve dependencies for abinit.

    Should deal whether its a restart of a non converged calculation or a follow up calculation (e.g. nscf after scf).

    TODO: define required and optional params
    """

    required_params = []
    optional_params = []

    def run_task(self, fw_spec):
        raise NotImplementedError
