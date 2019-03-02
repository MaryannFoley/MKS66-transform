from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    with open(fname,"r") as f:
        file=f.read()
    file.split("\n")

    for line in range(len(file)):
        if file[line] == "line":
            line+=1
            params=file[line]
            params.split()
        if file[line]=="ident":
            ident(transform)
        if file[line]=="scale":
            line+=1
            params=file[line]
            params.split()
            make_scale(params[0],params[1],params[2])
        if file[line]=="translate":
            line+=1
            params=file[line]
            params.split()
            make_translate(params[0],params[1],params[2])
        if file[line]=="rotate":
            line+=1
            params=file[line]
            params.split()
            if params[0] == "x":
                make_rotX(params[1])
            if params[0] == "y":
                make_rotX(params[1])
            if params[0] == "z":
                make_rotX(params[1])
        if file[line]=="apply":
            matrix_mult(transform,points)
        if file[line]=="display":
            clear_screen(screen)
            draw_lines(points,screen,color)
            display(screen)
        if file[line]=="save":
            clear_screen(screen)
            draw_lines(points,screen,color)
            save_extension(screen,file[line+1])
        if file[line]=="quit":
            break

    pass
