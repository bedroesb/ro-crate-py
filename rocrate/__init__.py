#!/usr/bin/env python

## Copyright 2019-2020 The University of Manchester, UK
##
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
##
##     http://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.

"""
Create/parse RO-Crate metadata.

This module intends to help create or parse
RO-Crate metadata, see rocrate_ 


.. _rocrate: https://w3id.org/ro/crate/
"""

__author__      = "Stian Soiland-Reyes <http://orcid.org/0000-0001-9842-9718>"
__copyright__   = "Copyright 2019-2020 The University of Manchester"
__license__     = "Apache License, version 2.0 <https://www.apache.org/licenses/LICENSE-2.0>"

# Convenience export of public functions/types
from .model.metadata import Metadata
from ._version import __version__
