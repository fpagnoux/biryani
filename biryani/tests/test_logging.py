# -*- coding: utf-8 -*-


# Biryani -- A conversion and validation toolbox
# By: Emmanuel Raviart <emmanuel@raviart.com>
#
# Copyright (C) 2009, 2010, 2011, 2012, 2013, 2014, 2015 Emmanuel Raviart
# http://packages.python.org/Biryani/
#
# This file is part of Biryani.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Tests about converters logging outputs."""


import logging

from biryani.baseconv import debug_converters, function, input_to_int, pipe


log = logging.getLogger(__name__)


def setup():
    logging.basicConfig(level = logging.DEBUG)


def test_pipe_empty():
    conv = pipe()
    conv(None)


def test_pipe_contains_only_none():
    conv = pipe(None)
    conv(None)


def test_pipe_contains_none():
    conv = pipe(input_to_int, None)
    conv(None)


def test_pipe_debug_iteration():
    test_log = log.getChild('test_pipe_debug_iteration')
    conv = pipe(*debug_converters([input_to_int, function(lambda value: value * 10)], test_log))
    conv('1')