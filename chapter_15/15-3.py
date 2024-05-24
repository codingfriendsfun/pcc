import matplotlib.pyplot as plt

from molecular_motion import MolecularMotion

while True:

    # Make a random walk.
    rw = MolecularMotion(5000)
    rw.move_pollen()

    plt.style.use('classic')

    fig,ax = plt.subplots(figsize=(15,9))

    point_numbers = range(rw.num_points)
    
    ax.plot(rw.x_values, rw.y_values, linewidth=2)
    ax.set_aspect('equal')
    
    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another map? (y/n): ")
    if keep_running.lower() == 'n':
        break



