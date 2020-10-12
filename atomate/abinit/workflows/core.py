# coding: utf-8

"""
This module defines Workflow generators for abinit.
"""


from atomate.common.workflows.base import BaseStructureWFGenerator
from atomate.abinit.fireworks.core import scf_fw
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from pymatgen.core.structure import Structure
from fireworks import Workflow


class ScfWFGenerator(BaseStructureWFGenerator):
    """Workflow generator for Self-Consistent Field (SCF) calculations."""

    def __init__(self):
        """Constructor for the SCF Workflow generator."""

        raise NotImplementedError

    def get_wf(self, structure: Optional[Structure] = None,
               name: str = 'Structure Workflow',
               prev_calc_locs: Optional[Union[List[str], str, bool]] = None,
               metadata: Optional[Union[Dict["str", Any], bool]] = None,
               name_tag: Optional[str] = None):

        """
        Generate and return a SCF Workflow.

        Args:
            structure: Pymatgen Structure object to be used as an input for the Workflow.
            name: Name of this workflow.
            prev_calc_locs:
            metadata:
            name_tag:

        Returns:
            Fireworks' Workflow object
        """

        fw = scf_fw(structure=structure)
        return Workflow([fw])
