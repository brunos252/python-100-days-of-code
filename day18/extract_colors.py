import colorgram


def extract(path):
    colors = colorgram.extract(path, 200)
    rgb_colors = []

    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        if not(r >= 230 and g >= 230 and b >= 230):
            rgb_colors.append((r, g, b))

    return rgb_colors
