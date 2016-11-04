import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation

# update the data for each frame
def anim(n):
    global data

    # get some new data
    data += np.random.random((100,100)) - .5
    # update the data into the image
    imobj.set_array(data)

    # returns a list of drawables which have been changed (needed for blitting)
    return imobj,

# create the figure
fig = plt.figure()
ax = fig.add_subplot(111)

# plot a static image
x = np.linspace(0, 2*np.pi, 200)
ax.plot(x, np.sin(x), 'r', lw=2)

# some data
data = np.random.random((100,100)) - .5

# create the image on top
imobj = ax.imshow(data, extent=[0,2*np.pi, -1.2, 1.2], origin='lower', cmap=plt.cm.gray, vmin=-2, vmax=2, alpha=.7, zorder=10)

# create the animation
ani = matplotlib.animation.FuncAnimation(fig, anim, frames=100)
ani.save("test.mp4", fps=10, codec="libx264", extra_args=['-pix_fmt', 'yuv420p'])