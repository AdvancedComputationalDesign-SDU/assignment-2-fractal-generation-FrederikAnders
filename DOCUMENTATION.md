# Assignment 2: Fractal Generation Documentation

## Table of Contents

- [Pseudo-Code](#pseudo-code)
- [Technical Explanation](#technical-explanation)
- [Results](#results)
- [References](#references)

---

## Pseudo-Code

1. **Define function that generates a color based on recursion depth**
**function** get_color(depth, max_depth):
    **return** color based on depth / max_depth using color map

2. **Initialize tree structure**
**initialize** tree_branches as empty list
**initialize** fact with random value
**initialize** starting curve (vertical line) as LineString [(0, 0), (0, 1)]
**add** starting curve to tree_branches

3. **define recursive function for tree generation**
**function** recursive_tree(curve_list, counter, angle, kinks, tilt):
    **initialize** new_branches as empty list
    
   **for** each curve in curve_list:
        # calculate translation and kinks
        dx, dy = calculate the difference between start and end points of curve
        
        # generate kinks within each branch
        segment_length = 1 / (kinks + 1)
        kink_points = list starting from the line's endpoint
        
        **for** each kink:
            calculate new kink point based on a random small offset
            translate/move and rotate kink point around the previous kink point
            append kink point to kink_points

        # create kinked curve from kink points
        create line segments from kink_points using LineString
        
        # rotate kinked curve to create left and right branches
        branch_left = rotate kinked curve by angle * fact
        branch_right = rotate kinked curve by -angle * fact
        
        # add new branches to new_branches
        **append* branch_left and branch_right to new_branches
    
    # count recursions and stop when max depth is reached
   **increment** counter
   **add** new_branches to tree_branches
   **if** counter < recursion_depth:
        call recursive_tree with new_branches and updated counter

4. **set parameters for the recursion**
recursion_depth = 10 (repetitions)
angle = 30 (angle for branching)
kinks = 5 (number of kinks per branch)
tilt = 0.3 (tilt for kink direction)

5. **start tree generation**
**call** recursive_tree with initial parameters

6. **plot the result**
**create** a figure and axis for plotting
**set** canvas background color to 'palegreen'

**for** each recursion level in tree_branches:
    **for** each branch in level:
        plot branch with color based on recursion depth using get_color

# finalize and display
**set** aspect ratio to 1
**hide** plot axes
**show** plot

---

## Technical Explanation

---

## Results


![Image 1](images/fig_1-depth7_angle30_kinks3_tilt0.2.png)

![Image 2](images/fig_2-depth5_angle40_kinks7_tilt0.5.png)

![Image 3](images/fig_3-depth9_angle90_kinks1_tilt0.5.png)

![Image 4](images/fig_4-depth5_angle15_kinks3_tilt0.9.png)

![Image 5](images/fig_5-depth10_angle30_kinks5_tilt0.3.png)


Example:

### Fractal Pattern 1: Basic Fractal Tree

![Fractal Tree](images/example.png)

- **Parameters**:
  - `angle_change`: 30°
  - `length_scaling_factor`: 0.7
  - `recursion_depth`: 5
- **Observations**:
  - The fractal tree exhibits symmetry and balance.
  - As the recursion depth increases, the level of detail in the branches increases.

*(Repeat for other fractal patterns.)*

---

## References

- **L-Systems**: [https://en.wikipedia.org/wiki/L-system](https://en.wikipedia.org/wiki/L-system)

