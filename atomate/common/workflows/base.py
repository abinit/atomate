# coding: utf-8

"""
This module defines the base workflow generator classes.
"""

import abc
from monty.json import MSONable
from monty.serialization import dumpfn, loadfn
from typing import TypeVar
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from pymatgen.core.structure import Structure


BaseWFGeneratorType = TypeVar('BaseWFGeneratorType', bound='BaseWFGenerator')


class BaseWFGenerator(MSONable):
    """
    Base class for all workflow generators.

    All atomate workflows should inherit from this BaseWFGenerator.
    """

    def to_file(self, path: str) -> None:
        """
        Dump the serialized object to a yaml or json file.

        Args:
            path (str): path to the file that should be created.

        Returns:
            None
        """
        dumpfn(self.as_dict(), path, indent=2)

    @classmethod
    def from_file(cls, path: str) -> BaseWFGeneratorType:
        """
        Construct an instance of the object from a serialized yaml or json file.

        Args:
            path (str): path to the yaml or json file from which to construct the object.

        Returns:
            An instance of the object.
        """
        return cls.from_dict(loadfn(path, cls=None))


class BaseStructureWFGenerator(BaseWFGenerator):
    """
    Base class for all workflow generators involving a structure as an input.
    """

    @abc.abstractmethod
    def get_wf(self, structure: Optional[Structure] = None,
               name: str = 'Structure Workflow',
               prev_calc_locs: Optional[Union[List[str], str, bool]] = None,
               metadata: Optional[Union[Dict["str", Any], bool]] = None,
               name_tag: Optional[str] = None):
        """
        Generate and return a Fireworks Workflow object.

        TODO: explain the difference between using structure and prev_calc_locs here

        Args:
            structure: Pymatgen Structure object to be used as an input for the Workflow.
            name: Name of this workflow.
            prev_calc_locs:
            metadata:
            name_tag:

        Returns:
            Fireworks' Workflow object
        """
