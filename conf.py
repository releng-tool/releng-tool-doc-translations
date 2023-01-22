#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2019-2021 releng-tool

from runpy import run_path
import os
import sys

if 'RELENG_TARGET_DIR' not in os.environ:
    raise SyntaxError('target directory not provided')

releng_tool_dir = os.path.abspath(os.environ['RELENG_TARGET_DIR'])
releng_tool_doc_dir = os.path.join(releng_tool_dir, 'Documentation')

# inject releng-tool into system path to allow autodocs content to render
sys.path.insert(0, releng_tool_dir)

# load releng-tool's sphinx configuration
conf = os.path.join(releng_tool_doc_dir, 'conf.py')
new_globals = run_path(conf, init_globals=globals())
globals().update(new_globals)

# localization options
if 'RELENG_LOCALE_DIR' not in os.environ:
    raise SyntaxError('locale directory not provided')

locale_dirs = [os.environ['RELENG_LOCALE_DIR']]
gettext_compact = False

def setup(app):
    # point application documentation to releng-tool's set
    app.confdir = releng_tool_doc_dir
    app.srcdir = releng_tool_doc_dir
