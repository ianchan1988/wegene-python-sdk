# -*- coding: utf-8 -*-

"""
   wegene.Models.GenotypesModel

   This file was automatically generated by APIMATIC BETA v2.0 on 02/22/2016
"""
from wegene.APIHelper import APIHelper
from wegene.Models.GenotypeModel import GenotypeModel

class GenotypesModel(object):

    """Implementation of the 'genotypes' model.

    An array of genotypes

    Attributes:
        genotypes (list of GenotypeModel): An array of genotypes

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the GenotypesModel class

        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    genotypes -- list of GenotypeModel -- Sets the attribute genotypes

        """
        # Set all of the parameters to their default values
        self.genotypes = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "genotypes": "genotypes",
        }

        # Parse all of the Key-Value arguments
        if kwargs is not None:
            for key in kwargs:
                # Only add arguments that are actually part of this object
                if key in replace_names:
                    setattr(self, replace_names[key], kwargs[key])

            # Other objects also need to be initialised properly
            if "genotypes" in kwargs:
                # Parameter is an array, so we need to iterate through it
                self.genotypes = list()
                for item in kwargs["genotypes"]:
                    self.genotypes.append(GenotypeModel(**item))

    def resolve_names(self):
        """Creates a dictionary representation of this object.

        This method converts an object to a dictionary that represents the
        format that the model should be in when passed into an API Request.
        Because of this, the generated dictionary may have different
        property names to that of the model itself.

        Returns:
            dict: The dictionary representing the object.

        """
        # Create a mapping from Model property names to API property names
        replace_names = {
            "genotypes": "genotypes",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)
