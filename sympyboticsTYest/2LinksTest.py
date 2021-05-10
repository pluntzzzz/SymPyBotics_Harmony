# import sympy
# import sympybotics
# rbtdef = sympybotics.RobotDef('Example Robot', # robot name
#                               [('-pi/2', 0, 0, 'q+pi/2'),  # list of tuples with Denavit-Hartenberg parameters
#                                ( 'pi/2', 0, 0, 'q-pi/2')], # (alpha, a, d, theta)
#                               dh_convention='standard' # either 'standard' or 'modified'
#                               )
# rbtdef.frictionmodel = {'Coulomb', 'viscous'} # options are None or a combination of 'Coulomb', 'viscous' and 'offset'
# rbtdef.gravityacc = sympy.Matrix([0.0, 0.0, -9.81]) # optional, this is the default value
#


import sympy
import sympybotics
rbtdef = sympybotics.RobotDef('left_arm',
                         [('pi/2', 0, 0, 'pi/2'),
                         ('pi/2', 0.03, 0.246, '-pi'),
                         ('-pi/2', -0.03, 0, '-pi/4'),
                         ('pi/2', 0, 0.186, 'pi'),
                         ('pi/2', 0, 0, 'pi'),
                         ('pi', 0, 0, 'pi/2')],
                        dh_convention='standard'
                         )
rbt = sympybotics.RobotDynCode(rbtdef, verbose=True)
rbt.calc_base_parms(verbose=True)