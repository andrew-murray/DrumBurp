# Copyright 2011-12 Michael Thomas
#
# See www.whatang.org for more information.
#
# This file is part of DrumBurp.
#
# DrumBurp is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DrumBurp is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with DrumBurp.  If not, see <http://www.gnu.org/licenses/>
'''
Created on 12 Dec 2010

@author: Mike Thomas
'''

class BadTimeError(StandardError):
    "The given note position is invalid."

class BadNoteSpecification(StandardError):
    "The given note index is not valid for this DrumKit."

class DuplicateDrumError(StandardError):
    "This drum already appears in this drum kit."

class NoSuchDrumError(StandardError):
    "The specified drum was not found."

class OverSizeMeasure(StandardError):
    "The Score contains a Measure which is too large to format for this width."

class DbReadError(StandardError):
    "There was an error reading the score."

class UnrecognisedLine(StandardError):
    "The line type was not recognised."

class InvalidInteger(DbReadError):
    "The value must be an integer."

class InvalidNonNegativeInteger(DbReadError):
    "The value must be a non-negative integer."

class InvalidPositiveInteger(DbReadError):
    "The value must be a positive integer."

class TooManyBarLines(DbReadError):
    "There are too many bar lines specifed for this measure."

class BadCount(DbReadError):
    "The given count is not recognised."

