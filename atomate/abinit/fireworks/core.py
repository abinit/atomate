# coding: utf-8

"""
This module defines the function to generate Fireworks for abinit.
"""


from fireworks import Firework
from atomate.abinit.firetasks.glue_tasks import CreateAbinitFolders
from atomate.abinit.firetasks.glue_tasks import ResolveDeps
from atomate.abinit.firetasks.glue_tasks import CopyAbinitOutputs
from atomate.abinit.firetasks.write_input_tasks import WriteInput
from atomate.abinit.firetasks.run_tasks import RunAbinit
from atomate.abinit.firetasks.control_tasks import CheckTask
from atomate.common.firetasks.glue_tasks import PassCalcLocs


__all__ = ("scf_fw", )


def scf_fw(structure):
    """Generate a Firework for a Self-Consistent Field (SCF) calculation.

    Args:
        structure: Pymatgen Structure object.
        TODO: Add arguments needed here

    Returns:
        Firework: Firework object with all Firetasks needed for an SCF calculation.
    """

    spec = {'structure': structure}
    #TODO: only a very general structure is done here :) goal is to foster discussion on the overall architecture
    tasks = []
    tasks.append(CreateAbinitFolders())
    tasks.append(ResolveDeps())  # Does it link/move/copy the files directly or is it just to define which files have to be copied where and then the next task does the work ?
    tasks.append(CopyAbinitOutputs())  # Or a general CopyFiles task, what about moving or symbolic links ?
    tasks.append(WriteInput())
    tasks.append(RunAbinit())
    tasks.append(CheckTask())
    tasks.append(PassCalcLocs())

    raise NotImplementedError
    # return Firework(tasks=tasks, spec=spec)
