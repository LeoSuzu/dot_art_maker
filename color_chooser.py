import colorgram

import colorgram

rgb_colors = []
brightness_threshold = 200  # Adjust this threshold according to your needs

colors = colorgram.extract('SamplePictures/EnkojiTemple.jpg', 100)  # Extract more colors initially

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    # Calculate the brightness of the color
    brightness = (r + g + b) / 3

    if brightness < brightness_threshold and len(rgb_colors) < 30:
        new_colour = (r, g, b)
        if new_colour not in rgb_colors:  # Check for uniqueness
            rgb_colors.append(new_colour)
    elif len(rgb_colors) >= 30:
        break

palette = tuple(rgb_colors)