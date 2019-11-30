import turtle

# function to build a Koch curve:
def koch(side_len, rank): 
    if rank == 0: 
        turtle.forward(side_len) 
        return
    side_len /= 3.0
    koch(side_len, rank-1) 
    turtle.left(60) 
    koch(side_len, rank-1) 
    turtle.right(120) 
    koch(side_len, rank-1) 
    turtle.left(60) 
    koch(side_len, rank-1) 
  
# main function 
if __name__ == "__main__": 
    # defining the speed of the turtle                     
    length = 400.0 
    rank = input("Write the rank of the curve 0..10: \n") 

    try:
       rank = int(rank)
    except:
        raise TypeError("Must be an integer") 
    if rank in range(11):
        # setup the window with a background color 
        wn = turtle.Screen()
        wn.bgcolor("green") 
        turtle.speed(9)
        # Pull the pen up - when moving 
        # to start position
        turtle.penup()  
        turtle.goto(-200, 100)        

        # Pull the pen down – drawing when moving.         
        turtle.pendown() 
        
        for i in range(3):     
            koch(length, rank) 
            turtle.right(120) 
    else:
        print("Not an integer in ranke 0..10")
     # To control the closing windows of the turtle 
    turtle.mainloop()   
