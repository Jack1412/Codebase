import numpy as np
half_car = 0.92 # need to modify !!!
chessboard = (8, 8)
chess_square_size = 0.035
chess_boundary = 0.040

armrest_pt_x = 1.427
armrest_pt_y = 0.852
armrest_pt_z = 0.775

laptop_length = 0.33

# case 1
x_boundary = armrest_pt_x
y_boundary = chess_square_size + chess_boundary + half_car - armrest_pt_y
z_boundary = chess_boundary + armrest_pt_z
chessboard_gt = []
for yi in range(chessboard[1]):
    tx = x_boundary
    ty = y_boundary + yi * chess_square_size
    for zi in range(chessboard[0]):
        tz = z_boundary + zi * chess_square_size
        chessboard_gt.append([tx, ty, tz])
chessboard_gt = np.array(chessboard_gt)
np.save('case1.npy', chessboard_gt)


# case 2
x_boundary = armrest_pt_x + chess_square_size + chess_boundary
y_boundary = half_car - armrest_pt_y
z_boundary = chess_boundary + armrest_pt_z
chessboard_gt = []
for xi in range(chessboard[1]):
    tx = x_boundary + xi * chess_square_size
    ty = y_boundary
    for zi in range(chessboard[0]):
        tz = z_boundary + zi * chess_square_size
        chessboard_gt.append([tx, ty, tz])
chessboard_gt = np.array(chessboard_gt[0:32])
np.save('case2.npy', chessboard_gt)


# case 3
x_boundary = armrest_pt_x + chess_square_size + chess_boundary
y_boundary = half_car - armrest_pt_y + laptop_length
z_boundary = chess_boundary + armrest_pt_z
chessboard_gt = []
for xi in range(chessboard[1]):
    tx = x_boundary + xi * chess_square_size
    ty = y_boundary
    for zi in range(chessboard[0]):
        tz = z_boundary + zi * chess_square_size
        chessboard_gt.append([tx, ty, tz])
chessboard_gt = np.array(chessboard_gt[0:32])
np.save('case3.npy', chessboard_gt)



print(chessboard_gt)
