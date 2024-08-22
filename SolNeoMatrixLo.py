#!/usr/bin/env python
#
#===============================================================================
#
#                         OOOO
#                       OOOOOOOO
#      PPPPPPPPPPPPP   OOO    OOO   PPPPPPPPPPPPP
#    PPPPPPPPPPPPPP   OOO      OOO   PPPPPPPPPPPPPP
#   PPP         PPP   OOO      OOO   PPP         PPP
#  PPP          PPP   OOO      OOO   PPP          PPP
#  PPP          PPP   OOO      OOO   PPP          PPP
#  PPP          PPP   OOO      OOO   PPP          PPP
#   PPP         PPP   OOO      OOO   PPP         PPP
#    PPPPPPPPPPPPPP   OOO      OOO   PPPPPPPPPPPPPP
#     PPPPPPPPPPPPP   OOO      OOO   PPP
#               PPP   OOO      OOO   PPP
#               PPP   OOO      OOO   PPP
#               PPP   OOO      OOO   PPP
#               PPP    OOO    OOO    PPP
#               PPP     OOOOOOOO     PPP
#              PPPPP      OOOO      PPPPP
#
# 
# File modified by Thomas Fulenwider on 4/15/21
#
# @file:   regrCfg.py
# @author: Hugh Spahr
# @date:   07/10/2016
#
# @note:   Open Pinball Project
#          Copyright 2012-2019, Hugh Spahr
#

# Setsup an STM32 bluepill for Solenoid+Neopixel on Wing0, Solenoid on Wing1, 
#   Switch matrix out (columns) active low on Wing2 and Switch matrix in (rows) on Wing3

testVers = '00.00.02'

import rs232Intf

# Config inputs as all state inputs
wingCfg = [ [ rs232Intf.WING_NEO_SOL, rs232Intf.WING_SOL, rs232Intf.WING_SW_MATRIX_OUT_LOW, rs232Intf.WING_SW_MATRIX_IN ] ]

# Config inputs as all state inputs
inpCfg = [ [ rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, \
             rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, \
             rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, \
             rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, \
             rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, \
             rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, \
             rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, \
             rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE ] ]

# solenoid config - this is a null config
solCfg =  [ [ '\x00', '\x00', '\x00', '\x00', '\x00', '\x00',
              '\x00', '\x00', '\x00', '\x00', '\x00', '\x00',
              '\x00', '\x00', '\x00', '\x00', '\x00', '\x00',
              '\x00', '\x00', '\x00', '\x00', '\x00', '\x00',
              '\x00', '\x00', '\x00', '\x00', '\x00', '\x00', \
              '\x00', '\x00', '\x00', '\x00', '\x00', '\x00', \
              '\x00', '\x00', '\x00', '\x00', '\x00', '\x00', \
              '\x00', '\x00', '\x00', '\x00', '\x00', '\x00' ] ]

# Config color table
#              bytesPerPxl (1 byte), numPixels (1 byte, if 0, then 256 pixels), boot color (3 bytes), unused (92 bytes) 
colorCfg = [ [ '\x03', '\x00', '\x00', '\x00', '\x04', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', \
               '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', \
               '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', \
               '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', \
               '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', \
               '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', \
               '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', \
               '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', '\xff', \
               '\xff', \
            ] ]
