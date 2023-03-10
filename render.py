import imageio
import glob
import os
import pdb

if os.path.exists("../../../videos"):
    import shutil

    shutil.rmtree("../../../videos")
    os.mkdir("../../../videos")
for i in range(1):
    writer = imageio.get_writer(f"~/gomp/videos/env{i}.gif", fps=30)
    file_names = [
        file
        for file in glob.glob(os.path.join("graphics_images", f"rgb_env{i}_cam1*.png"))
    ]
    file_names.sort()
    # pdb.set_trace()
    for file in file_names:
        im = imageio.imread(file)
        writer.append_data(im)
    writer.close()

    writer = imageio.get_writer(f"~/gomp/videos/boxless_env{i}.mp4", fps=30)
    file_names = [
        file
        for file in glob.glob(
            os.path.join("graphics_images", f"boxless_rgb_env{i}_cam1*.png")
        )
    ]
    file_names.sort()
    # pdb.set_trace()
    for file in file_names:
        im = imageio.imread(file)
        writer.append_data(im)
    writer.close()

    writer = imageio.get_writer(f"~/gomp/videos/depth_env{i}.gif", fps=30)
    file_names = [
        file
        for file in glob.glob(
            os.path.join("graphics_images", f"depth_env{i}_cam1*.jpg")
        )
    ]
    file_names.sort()
    # pdb.set_trace()
    for file in file_names:
        im = imageio.imread(file)
        writer.append_data(im)
    writer.close()

    writer = imageio.get_writer(f"~/gomp/videos/seg_env{i}.gif", fps=30)
    file_names = [
        file
        for file in glob.glob(os.path.join("graphics_images", f"seg_env{i}_cam1*.jpg"))
    ]
    file_names.sort()
    # pdb.set_trace()
    for file in file_names:
        im = imageio.imread(file)
        writer.append_data(im)
    writer.close()
