"""
Assignment 2: Fractal Generator

Author: Frederik Andersen

Description:
This script generates fractal patterns using recursive functions and geometric transformations.
"""

# Import necessary libraries
from shapely.geometry import LineString, Point 
from shapely.affinity import translate, rotate
from shapely.plotting import plot_line, plot_points, plot_polygon 
import matplotlib.pyplot as plt
import random

# apply color (gradient color)
def get_color(depth, max_depth):
   return plt.cm.viridis(depth / max_depth)     #viridis is the name of a specific color gradient (you can also try plsma, inferno, etc.)

# initializing empty list for branches
tree_branches = []
fact = random.random()

# Starting curve: a vertical line represented as a LineString 
x = LineString([(0, 0), (0, 1)])
tree_branches.append([x]) # Initial set of branches contains only the starting curve. Add x at the end of the tree_branch

def recursive_tree(curve_list, counter, angle, kinks, tilt): #the stuff in the brackets are parameters for the funtion
    new_branches = []       #list to store the new branches that will be made
    
    for curve in curve_list:    #loops over each curve (branch) in the list
        # calculate the end-start difference to perform the translation in x and y 
        dx = curve.coords[-1][0] - curve.coords[0][0]
        dy = curve.coords[-1][1] - curve.coords[0][1]
        
        # generate kinks within the branch
        # create series of slighty offset points along branch 
        segment_length = 1 / (kinks + 1)    # define/calculate length of each segment along the branch
        kink_points = [curve.coords[-1]]    # endpoint of current branch/curve. This will be the startingpoint for the creating the kinked path

        for _ in range(kinks):
            # extend segment with random small offsets for generating kinks
            dx_kink = dx * segment_length
            dy_kink = dy * segment_length

            kink_point = translate(Point(kink_points[-1]), xoff=dx_kink, yoff=dy_kink)      # Point(kink_points[-1]) takes last point in kink_points which will act as a base from which the new kink will be offset
            kink_point = rotate(kink_point, angle * (random.random() - tilt) * 2, origin=kink_points[-1], use_radians=False)     # rotate new kink point around previous kink point by random small angle. 
            kink_points.append(kink_point)  # add the new kink point to kink_points, so the next kink can build upon this point

        kinked_curve = LineString(kink_points)  #string the points together

        # rotate the kinked curve to create left and right branches
        branch_left = rotate(kinked_curve, angle * fact, origin=curve.coords[-1], use_radians=False)
        branch_right = rotate(kinked_curve, -angle * fact, origin=curve.coords[-1], use_radians=False)

        # add the two new branches to the list of branches that will be used in the next recursion level
        new_branches.extend([branch_left, branch_right])    
        

    # count recersions and define stop for recursions
    counter += 1
    tree_branches.append(new_branches) 
    if counter < recursion_depth:       # if n recursions is reached, print
        print(counter)
        recursive_tree(new_branches, counter, angle, kinks, tilt)

# Parameters:
recursion_depth = 7
angle = 30          # Angle for branches
kinks = 3           # number of kinks per branch
tilt = 0.2         # tilt kinks towards the right or left. (0 = far left, 0.5 = middle, 1 = far right)

recursive_tree([x], 0, angle, kinks, tilt)


# Plotting the result using Matplotlib 
fig, ax = plt.subplots()
fig.patch.set_facecolor('beige') # set color of canvas

for depth, level in enumerate(tree_branches): 
    color = get_color(depth, recursion_depth)   #apply color based on depth of branch
    for branch in level:
        plot_line(branch, add_points=False, color=color, linewidth=1)

ax.set_aspect(1) 
plt.axis('off') 
plt.show()

git add .
git commit -m "add colors"
git push origin main