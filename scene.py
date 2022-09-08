import tkinter as tk  # tkinter
from PIL import Image, ImageTk  # adding an image
import math

'''Draw an outdoor scene using functions and tkinter.'''


def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    # Add image to canvas
    img = (Image.open('deer.png'))  # open img
    resize_image = img.resize((70, 80))  # resized width, height
    new_img = ImageTk.PhotoImage(resize_image)  # new resized img
    canvas.create_image(400, 300, image=new_img)  # display, coordinates

    img2 = (Image.open('rabbit.png'))
    resize_image2 = img2.resize((40, 35))
    new_img2 = ImageTk.PhotoImage(resize_image2)
    canvas.create_image(640, 465, image=new_img2)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Sky
    draw_sky(canvas, 0, 0)  # first num is x axis, second is y axis
    draw_sun(canvas, 90, 70)
    draw_clouds(canvas, 100, 100)
    draw_clouds(canvas, 130, 110)
    draw_clouds(canvas, 130, 90, scale=.8)
    draw_clouds(canvas, 420, 70, scale=1.5)
    draw_clouds(canvas, 400, 60)
    draw_clouds(canvas, 460, 50)
    draw_clouds(canvas, 465, 110)

    # Ground
    draw_ground(canvas, 0, 300)
    draw_mounts(canvas, -40, 230)
    draw_mounts(canvas, 50, 200)
    draw_mounts(canvas, 150, 250)
    draw_mounts(canvas, 240, 280, scale=.5)

    # Pine tree forest
    draw_trunk(canvas, 40, 430)
    draw_trunk(canvas, 110, 400)
    draw_trunk(canvas, 190, 430)
    draw_trunk(canvas, 230, 410)
    draw_pine_tree(canvas, 50, 270)
    draw_pine_tree(canvas, 100, 270)
    draw_pine_tree(canvas, 150, 270)
    draw_pine_tree(canvas, 200, 270)
    draw_pine_tree(canvas, 30, 300, scale=1.4)
    draw_pine_tree(canvas, 80, 300, scale=1.4)
    draw_pine_tree(canvas, 120, 300, scale=1.4)
    draw_pine_tree(canvas, 170, 300, scale=1.4)
    draw_pine_tree(canvas, 50, 340, scale=1.7)
    draw_pine_tree(canvas, 120, 310, scale=1.7)
    draw_pine_tree(canvas, 195, 330, scale=1.7)
    draw_pine_tree(canvas, 240, 300, scale=1.7)

    # Autumn forest
    draw_yellow_tree(canvas, 750, 230)
    draw_yellow_tree(canvas, 700, 250)
    draw_yellow_tree(canvas, 650, 230)
    draw_yellow_tree(canvas, 600, 240)
    draw_trunk(canvas, 660, 380)
    draw_red_tree(canvas, 710, 300, scale=1.2)
    draw_red_tree(canvas, 620, 300, scale=1.5)
    draw_red_tree(canvas, 560, 300)
    draw_trunk(canvas, 580, 410)
    draw_trunk(canvas, 720, 410)
    draw_orange_tree(canvas, 530, 380)
    draw_orange_tree(canvas, 520, 350, scale=.8)
    draw_orange_tree(canvas, 560, 360, scale=.7)
    draw_orange_tree(canvas, 670, 390)
    draw_orange_tree(canvas, 660, 360, scale=.8)
    draw_orange_tree(canvas, 700, 370, scale=.7)


def draw_sky(canvas, sky_left, sky_top):
    """Draw sky.
    Parameters: canvas, sky_left, sky_top
    Return: nothing
    """
    sky_width = 800
    sky_height = 300
    sky_right = sky_left + sky_width
    sky_bottom = sky_top + sky_height

    canvas. create_rectangle(sky_left, sky_top, sky_right,
                             sky_bottom, fill='lightSkyBlue1', width=0)  # width=0 deleter border


def draw_ground(canvas, ground_left, ground_top):
    """Draw ground.
    Parameters: canvas, ground_left, ground_top
    Return: nothing
    """
    ground_width = 800
    ground_height = 200
    ground_right = ground_left + ground_width
    ground_bottom = ground_top + ground_height

    canvas. create_rectangle(ground_left, ground_top, ground_right,
                             ground_bottom, fill='tan3', width=0)


def draw_mounts(canvas, mount_left, mount_top, scale=1):
    """Draw a mount.
    Parameters: canvas, mount_left, mount_top, scale
    Return: nothing
    """
    mount_width = 130 * scale
    mount_height = 230 * scale
    mount_right = mount_left + mount_width
    mount_bottom = mount_top + mount_height

    canvas. create_oval(mount_left, mount_top, mount_right,
                        mount_bottom, fill='tan3', width=0)


def draw_clouds(canvas, cloud_left, cloud_top, scale=1):
    """Draw cloud.
    Parameters: canvas, cloud_left, cloud_top, scale
    Return: nothing
    """
    cloud_width = 130 * scale
    cloud_height = 50 * scale
    cloud_right = cloud_left + cloud_width
    cloud_bottom = cloud_top + cloud_height

    canvas. create_oval(cloud_left, cloud_top, cloud_right,
                        cloud_bottom, fill='white', width=0)


def draw_sun(canvas, sun_left, sun_top):
    """Draw the sun.
    Parameters: canvas, sun_left, sun_top
    Return: nothing
    """
    sun_width = 85
    sun_height = 85
    sun_right = sun_left + sun_width
    sun_bottom = sun_top + sun_height
    ray_length = 70
    ray_width = 3
    ray_count = 10

    canvas. create_oval(sun_left, sun_top, sun_right,
                        sun_bottom, fill='gold', width=0)

    # drawing sun rays
    sun_center_x = sun_left + (sun_width / 2)
    sun_center_y = sun_top + (sun_height / 2)

    for i in range(ray_count):
        angle = (2 * math.pi / ray_count) * i
        ray_x = sun_center_x + math.cos(angle) * ray_length
        ray_y = sun_center_y + math.sin(angle) * ray_length
        canvas.create_line(sun_center_x, sun_center_y, ray_x,
                           ray_y, width=ray_width, fill='gold')


def draw_yellow_tree(canvas, tree_left, tree_top, scale=1):
    """Draw a yellow large tree using ovals.
    Parameters: canvas, tree_left, tree_top, scale
    Return: nothing
    """
    tree_width = 50 * scale
    tree_height = 130 * scale
    tree_right = tree_left + tree_width
    tree_bottom = tree_top + tree_height

    canvas. create_oval(tree_left, tree_top, tree_right,
                        tree_bottom, fill='goldenrod1', width=0)


def draw_red_tree(canvas, tree_left, tree_top, scale=1):
    """Draw a red round tree using ovals.
    Parameters: canvas, tree_left, tree_top, scale
    Return: nothing
    """
    tree_width = 70 * scale
    tree_height = 70 * scale
    tree_right = tree_left + tree_width
    tree_bottom = tree_top + tree_height

    canvas. create_oval(tree_left, tree_top, tree_right,
                        tree_bottom, fill='indianred2', width=0)


def draw_orange_tree(canvas, tree_left, tree_top, scale=1):
    """Draw a tree using ovals.
    Parameters: canvas, tree_left, tree_top, scale
    Return: nothing
    """
    tree_width = 130 * scale
    tree_height = 50 * scale
    tree_right = tree_left + tree_width
    tree_bottom = tree_top + tree_height

    canvas. create_oval(tree_left, tree_top, tree_right,
                        tree_bottom, fill='orange', width=0)


def draw_trunk(canvas, trunk_left, trunk_top):
    """Draw a trunk tree.
    Parameters: canvas, trunk_left, trunk_top
    Return: nothing
    """
    trunk_width = 20
    trunk_height = 70
    trunk_right = trunk_left + trunk_width
    trunk_bottom = trunk_top + trunk_height

    canvas. create_rectangle(trunk_left, trunk_top, trunk_right,
                             trunk_bottom, fill='saddlebrown', width=0)


def draw_pine_tree(canvas, peak_x, peak_y, scale=1):
    """Draw a single pine tree.
    Parameters: canvas, peak_x, peak_y, scale
    Return: nothing
    """

    skirt_width = 100 / 2 * scale
    skirt_height = 80 * scale
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
                          skirt_right, skirt_bottom,
                          skirt_left, skirt_bottom,
                          fill="paleGreen4", width=0)


# Call the main function so that
# this program will start executing.
main()
