from PIL import Image
import numpy as np

import av
import av.datasets


container = av.open(
    "/home/rgbellion/Videos/ANIVESICARIO/peripheria4.mp4"
    #"videos/hydra.mp4"
)
container.streams.video[0].thread_type = "AUTO"  # Go faster!

columns = []
height = 0
for frame in container.decode(video=0):
    height+=1
    print(frame)
    array = frame.to_ndarray(format="rgb24")
    # Collapse down to a column.
    if False:
        column = array.std(axis=1)
    else:
        column = array.mean(axis=1)
    width = len(array)
    # Convert to bytes, as the `mean` turned our array into floats.
    column = column.clip(0, 255).astype("uint8")

    # Get us in the right shape for the `hstack` below.
    column = column.reshape(-1, 1, 3)

    columns.append(column)

# Close the file, free memory
container.close()



print("height,width")
print(height,width)
full_array = np.hstack(columns)
full_img = Image.fromarray(full_array, "RGB")
full_img = full_img.resize((width, height))
full_img.save("barcode.jpg", quality=100)
