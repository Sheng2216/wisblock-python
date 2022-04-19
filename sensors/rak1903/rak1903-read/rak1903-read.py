#!/usr/bin/env python3
"""
Read ambient light data with RAK1903(OPT3001).
"""
__copyright__ = "Copyright 2022, RAKwireless"
__license__ = "GPL"
__version__ = "1.0.0"
__status__ = "Production"
__maintainer__ = "rakwireless.com"

import time
from opt3001 import opt3001 
address = 0x44

opt = opt3001.OPT3001(address) 

# Configure to run in Continuous conversions mode
opt.write_config_reg(opt3001.I2C_LS_CONFIG_CONT_FULL_800MS)

while(True):
  print("Ambient light:", opt.read_lux_float(), "lux")
  time.sleep(1)
