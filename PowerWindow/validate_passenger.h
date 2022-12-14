/**************************************************************************************************\
 *** 
 *** Simulink model       : powerwindow_tl_v01
 *** TargetLink subsystem : powerwindow_tl_v01/PowerWindow_ClosedLoop/power_window_controller
 *** Codefile             : validate_passenger.h
 ***
 *** Generated by TargetLink, the dSPACE production quality code generator
 *** Generation date: 2017-01-20 14:45:06
 ***
 *** CODE GENERATOR OPTIONS:
 *** Code generation mode                     : Standard
 *** Compiler                                 : <unknown>
 *** Target                                   : Generic
 *** ANSI-C compatible code                   : yes
 *** Code Optimization                        : enabled
 *** Constant style                           : decimal
 *** Clean code option                        : enabled
 *** Logging mode                             : Do not log anything
 *** Code Coverage                            : disabled
 *** Generate empty conditional branches      : disabled
 *** Loop unroll threshold                    : 5
 *** Variable vector widths                   : enabled
 *** Shift mode                               : automatic
 *** Handle unscaled SF expr. with TL type    : enabled
 *** Assignment of conditions                 : AllBooleanOutputs 
 *** Scope reduction only to function level   : disabled
 *** Exploit ranges if not erasable           : disabled
 *** Exploit Compute Through Overflow         : optimized
 *** Linker sections                          : disabled
 *** Enable Assembler                         : disabled
 *** Variable name length                     : 31 chars
 *** Use global bitfields                     : disabled
 *** Stateflow: use of bitfields              : enabled
 *** State activity encoding limit            : 5
 *** Omit zero inits in restart function      : disabled
 *** Share functions between TL subsystems    : disabled
 *** Generate 64bit functions                 : enabled
 *** Inlining Threshold                       : 6
 *** Line break limit                         : 100
 *** Target optimized boolean data type       : enabled
 *** Keep saturation elements                 : disabled
 *** Extended variable sharing                : disabled
 *** Extended lifetime optimization           : enabled
 *** Style definition file                    : C:\dspace\TL41\Matlab\Tl\Config\codegen\cconfig.xml
 *** Root style sheet                         : C:\dspace\TL41\Matlab\Tl\XML\CodeGen\Stylesheets\TL_
 ***                                            CSourceCodeSS.xsl
 ***
 *** TargetLink version      : 4.1 from 12-Oct-2015
 *** Code generator version  : Build Id 4.1.0.21 from 2015-09-25 11:04:18

\**************************************************************************************************/

#ifndef VALIDATE_PASSENGER_H
#define VALIDATE_PASSENGER_H

/*----------------------------------------------------------------------------*\
  DEFINES (OPT)
\*----------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------*\
  INCLUDES
\*----------------------------------------------------------------------------*/
#include "tl_defines_a.h"
#include "tl_basetypes.h"
/*----------------------------------------------------------------------------*\
  DEFINES
\*----------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------*\
  TYPEDEFS
\*----------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------*\
  ENUMS
\*----------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------*\
  VARIABLES
\*----------------------------------------------------------------------------*/

/******************************************************************************\
   SLGlobal: Default storage class for global variables | Width: 8
\******************************************************************************/
extern Bool Sa4_validated_down;
extern Bool Sa4_validated_neutral;
extern Bool Sa4_validated_up;

/*----------------------------------------------------------------------------*\
  PARAMETERIZED MACROS
\*----------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------*\
  FUNCTION PROTOTYPES
\*----------------------------------------------------------------------------*/
/******************************************************************************\
   GlobalFcnSpecStep: Default function class for not static model step functions
\******************************************************************************/
extern void validate_passenger(void);


#endif /* VALIDATE_PASSENGER_H */
/*----------------------------------------------------------------------------*\
  END OF FILE
\*----------------------------------------------------------------------------*/
