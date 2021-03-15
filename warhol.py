# # CS 5001 
# # lab 6 
# # generating images to the window

import sys
import graphicsPlus as gr

def main( argv ):

    if len(argv) < 2:
        print("usage: python3 image.py <image filename>")
        return

    # read in the image from the filename specified on the command
    filename = argv[1]
    image = gr.Image( gr.Point(0, 0), filename )

    # create a window that is the same size as the image
    rows = image.getHeight()
    cols = image.getWidth()
    win = gr.GraphWin( filename, cols, rows )

    # move the image so it is centered in the window
    image.move( cols/2, rows/2 )

    # call the filter function before the image is drawn into a window
    # reduceRed( image )

    image.draw(win)

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main(sys.argv)



# import sys
# import graphicsPlus as gr

# #read an image an display it in the window 

# def main( argv ):

#     # if statement to check if the right amount of arguments such as filenanme have been given
#     if len(argv) < 2:
#         print(" usage: python3 image.py <image filename> ")
#         return

#     # read in the image from the filename specified on the command
#     filename = argv[1]
#     image = gr.Image( gr.Point(0, 0), filename )

#     # create a window that is that the same size as the image 
#     rows = image.getHeight()
#     cols = image.getWidth()
#     win = gr.GraphWin( filename, cols, rows )

#     # move the image so it is centered in the window 
#     image.move( cols/2, rows/2 )

#     # call the filter function before the image is drawn into a window 
#     # reducedRed( image )
#     image.draw(win)

#     win.getMouse()
#     win.close()

# if __file__ == "__main__":
#     main(sys.argv)


    