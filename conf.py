#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2019 releng-tool

from sphinx.util.pycompat import execfile_
import os
import sys

base_dir = os.path.dirname(os.path.abspath(__file__))
releng_tool_dir = os.path.join(base_dir, 'releng-tool')
releng_tool_doc_dir = os.path.join(releng_tool_dir, 'Documentation')

# inject releng-tool into system path to allow autodocs content to render
sys.path.insert(0, releng_tool_dir)

# load releng-tool's sphinx configuration
execfile_(os.path.join(releng_tool_doc_dir, 'conf.py'), globals())

# localization options
locale_dirs = [os.path.join(base_dir, 'locale/')]
gettext_compact = False

def setup(app):
    # point application documentation to releng-tool's set
    app.confdir = releng_tool_doc_dir
    app.srcdir = releng_tool_doc_dir
