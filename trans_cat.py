import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def generate_ellipse(x_center, y_center, a, b, t_init, t_term, rot, num_points):
    # x = np.zeros(num_points)
    # y = np.zeros(num_points)
    t = np.linspace(t_init, t_term, num_points)
    tmp_x = a * np.cos(t)
    tmp_y = b * np.sin(t)
    x[part_num, :num_points] = x_center + np.cos(rot) * tmp_x - np.sin(rot) * tmp_y
    y[part_num, :num_points] = y_center + np.sin(rot) * tmp_x + np.cos(rot) * tmp_y
    return
    

# 座標系を設定するパラメータを与える
x_left = -2.2
x_right = 2.2
y_bottom = -2.2
y_top = 2.2
ratio = 1


num_parts = 11
max_num_points = 200
x = np.zeros((num_parts, max_num_points))
y = np.zeros((num_parts, max_num_points))
x_trans = np.zeros((num_parts, max_num_points))
y_trans = np.zeros((num_parts, max_num_points))
# num_points = np.zeros(num_parts, dtype = int)
num_points = np.array([100, 20, 3, 3, 30, 30, 4, 2, 30, 30, 40])

part_num = 0
generate_ellipse(0., 0, 1, 0.85, -9*np.pi/8, np.pi/8, 0., num_points[part_num])

part_num = 1
generate_ellipse(0., 0, 1, 0.8, np.pi * 0.4, np.pi * 0.6, 0., num_points[part_num])

part_num = 2
end_1 = num_points[1] - 1
x[part_num, :num_points[part_num]] = x[0,0], 0.4*x[0,0] + 0.6*x[1,end_1], x[1,end_1]
y[part_num, :num_points[part_num]] = y[0,0], y[0,0] + (y[1,end_1] - y[0,0])*1.8, y[1,end_1]

part_num = 3
x[part_num, :num_points[part_num]] = - x[part_num-1, :num_points[part_num-1]]
y[part_num, :num_points[part_num]] = y[part_num-1, :num_points[part_num-1]]

part_num = 4
generate_ellipse(0.45, 0.08, 0.3, 0.2, np.pi * 0.1, np.pi * 0.9, np.pi/7, num_points[part_num])

part_num = 5
x[part_num, :num_points[part_num]] = - x[part_num-1, :num_points[part_num-1]]
y[part_num, :num_points[part_num]] = y[part_num-1, :num_points[part_num-1]]

part_num = 6
x[part_num, :num_points[part_num]] = 0, 0.05, -0.05, 0
y[part_num, :num_points[part_num]] = -0.2, -0.15, -0.15, -0.2

part_num = 7
x[part_num, :num_points[part_num]] = 0, 0
y[part_num, :num_points[part_num]] = - 0.2, -0.35

part_num = 8
generate_ellipse(0.2, -0.35, 0.2, 0.2, -np.pi, 0, 0, num_points[part_num])

part_num = 9
x[part_num, :num_points[part_num]] = - x[part_num-1, :num_points[part_num-1]]
y[part_num, :num_points[part_num]] = y[part_num-1, :num_points[part_num-1]]

part_num = 10
#generate_ellipse(-0.4, 0.2, 0.05, 0.05, 0, 2 * np.pi, 0, num_points[part_num])
generate_ellipse(-0.75, -0.20, 0.20, 0.17, 0, 2 * np.pi, -np.pi/3, num_points[part_num])


# fig という名前のfigure (ウィンドウ)を生成する
fig = plt.figure(figsize = (5, 5))

# ax という名前のaxes (描画領域)を fig の中に１つ生成する
ax = fig.add_subplot(1, 1, 1)


# ax に座標系を設定する
ax.set_xlim(x_left, x_right)
ax.set_ylim(y_bottom, y_top)
ax.set_aspect(ratio)                     # この図の場合、これは必要

ax.vlines(np.linspace(-5, 5, 11), ymin = y_bottom, ymax = y_top, color = 'black', linewidth = 0.5)
ax.hlines(np.linspace(-5, 5, 11), xmin = x_left, xmax = x_right, color = 'black', linewidth = 0.5)

a11 = st.number_input('a11 = ', step=0.01, format = '%.5f')
a12 = st.number_input('a12 = ', step=0.01, format = '%.5f')
a21 = st.number_input('a21 = ', step=0.01, format = '%.5f')
a22 = st.number_input('a22 = ', step=0.01, format = '%.5f')

for part_num in range(num_parts):
    for point in range(num_points[part_num]):
        x_trans[part_num, point] = a11 * x[part_num, point] + a12 * y[part_num, point]
        y_trans[part_num, point] = a21 * x[part_num, point] + a22 * y[part_num, point]

for part_num in range(num_parts):
   ax.plot(x_trans[part_num, :num_points[part_num]], y_trans[part_num, :num_points[part_num]], color = 'red', linewidth = 4)


# fig を表示する
st.pyplot(fig)
#plt.show()
