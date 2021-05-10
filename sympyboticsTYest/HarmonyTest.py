# -*- coding: utf-8 -*-
import sympy
import numpy
import sympybotics


# 建立机器人模型
arr = [
        ('0',       0,       0,         'q'),  # list of tuples with Denavit-Hartenberg parameters
        ('-pi/2',   0,       0,         'q'),
        ('pi/2',    0.23762, -0.24492,  'q'),
        ('-pi/3',   0,       0,         'q'),
        ('pi/3',    0,       0,         'q'),
        ('0',       0.281,   0,         'q')
];

rbtdef = sympybotics.RobotDef('Example Robot', # robot name
                              arr,  # (alpha, a, d, theta)
                              dh_convention='modified'  # either 'standard' or 'modified'
                              )

# 设定重力加速度的值（沿z轴负方向）
rbtdef.gravityacc=sympy.Matrix([0.0, -9.81, 0.0])
# 设定摩擦力 库伦摩擦与粘滞摩擦
rbtdef.frictionmodel = {'Coulomb', 'viscous'}
# 显示动力学全参数
print(rbtdef.dynparms())
#构建机器人动力学模型
rbt = sympybotics.RobotDynCode(rbtdef, verbose=True)
# 转换为C代码
tau_str = sympybotics.robotcodegen.robot_code_to_func('C', rbt.invdyn_code, 'tau_out', 'tau', rbtdef)
print(tau_str) #打印
#计算并显示动力学模型的回归观测矩阵，转换为C代码
rbt.calc_base_parms()#就这行有毛病
print(rbt.dyn.baseparms) #打印
# print(rbt.dyn.baseparms)# 打印最小参数集P
# rbt.Hb_code
# print(rbt.Hb_code)#打印观测矩阵
# Yr = sympybotics.robotcodegen.robot_code_to_func('C', rbt.Hb_code, 'H', 'Hb_code', rbtdef)
# print(Yr) #打印显示转换为C代码后的观测矩阵Yr
# #把动力学全参数模型，关节力矩模型，观测矩阵和最小惯性参数集结果保存为txt
# data=open("D:\data.txt",'w+')
# print(rbt.dyn.dynparms,tau_str,Yr,rbt.dyn.baseparms,file=data)
# data.close()

