#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Gettings Things Gnome! - a personnal organizer for the GNOME desktop
# Copyright (c) 2008-2009 - Lionel Dricot & Bertrand Rousseau
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.
#
#===============================================================================
#
# Getting things Gnome!: a gtd-inspired organizer for GNOME
#
# @author : B. Rousseau, L. Dricot
# @date   : November 2008
#
#   main.py contains the configuration and data structures loader
#   taskbrowser.py contains the main GTK interface for the tasklist
#   task.py contains the implementation of a task and a project
#   taskeditor contains the GTK interface for task editing
#       (it's the window you see when writing a task)
#   backends/xml_backend.py is the way to store tasks and project in XML
#
#   tid stand for "Task ID"
#   pid stand for "Project ID"
#   uid stand for "Universal ID" which is generally the tuple [pid,tid]
#
#   Each id are *strings*
#   tid are the form "X@Y" where Y is the pid.
#   For example : 21@2 is the 21th task of the 2nd project
#   This way, we are sure that a tid is unique accross multiple projects 
#
#=============================================================================== 

#=== IMPORT ====================================================================

#our own imports
from GTG.taskbrowser.browser import TaskBrowser
from GTG.core.datastore      import DataStore
from GTG.core                import CoreConfig

#=== OBJECTS ===================================================================

#=== MAIN CLASS ================================================================

def main():
    config        = CoreConfig()
    backends_list = config.get_backends_list()
    
    # Load data store
    ds = DataStore()
    
    for backend_dic in backends_list :
        ds.register_backend(backend_dic)
        
    # Launch task browser
    req = ds.get_requester()
    tb  = TaskBrowser(req, config.conf_dict)
    tb.main()

    # Ideally we should load window geometry configuration from a config.
    # backend like gconf at some point, and restore the appearance of the
    # application as the user last exited it.

    # Ending the application: we save configuration
    config.save_config()
    config.save_datastore(ds)

#=== EXECUTION =================================================================

if __name__ == "__main__":
    main()