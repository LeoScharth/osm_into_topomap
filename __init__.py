# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Osm2TopoMap
                                 A QGIS plugin
 A plugin intended to intermediate the process of using OSM data for official (authoritative) Topographc Maps, or rather, databases
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2023-06-14
        copyright            : (C) 2023 by Leonardo Scharth; Kauê Vestena; Silvana Camboim
        email                : scharth.leo@gmail.com 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

__author__ = 'Leonardo Scharth; Kauê Vestena; Silvana Camboim'
__date__ = '2023-06-14'
__copyright__ = '(C) 2023 by Leonardo Scharth; Kauê Vestena; Silvana Camboim'


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Osm2TopoMap class from file Osm2TopoMap.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .osm_2_topomap import Osm2TopoMapPlugin
    return Osm2TopoMapPlugin()
