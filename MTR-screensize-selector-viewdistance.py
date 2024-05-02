import math

def inches_to_feet_and_inches(inches):
    feet = int(inches // 12)
    remaining_inches = inches % 12
    return f"{feet}ft {remaining_inches:.1f}in"

# Constants
diagonal = 135  # given diagonal of the screen
aspect_ratio_width_21_9 = 21
aspect_ratio_height_21_9 = 9
aspect_ratio_width_16_9 = 16
aspect_ratio_height_16_9 = 9
area_factor = 0.6

# Calculate height (H) and width (W) of the original screen (21:9)
H = diagonal / math.sqrt((aspect_ratio_width_21_9 / aspect_ratio_height_21_9) ** 2 + 1)
W = (aspect_ratio_width_21_9 / aspect_ratio_height_21_9) * H

# New width (W') and height (H') for 60% screen usage maintaining 21:9
W_prime = math.sqrt(area_factor) * W
H_prime = math.sqrt(area_factor) * H

# New diagonal for 60% screen usage (21:9)
D_prime = math.sqrt(W_prime**2 + H_prime**2)

# Full screen 16:9 dimensions
H_16_9_full = H
W_16_9_full = (aspect_ratio_width_16_9 / aspect_ratio_height_16_9) * H_16_9_full
D_16_9_full = math.sqrt(W_16_9_full**2 + H_16_9_full**2)

# 60% screen 16:9 dimensions
H_16_9_60_percent = H_prime
W_16_9_60_percent = (aspect_ratio_width_16_9 / aspect_ratio_height_16_9) * H_16_9_60_percent
D_16_9_60_percent = math.sqrt(W_16_9_60_percent**2 + H_16_9_60_percent**2)

# DISCAS Viewing Distances
discas_min_21_9 = 1.5 * H
discas_max_21_9 = 2.0 * H
discas_min_21_9_60 = 1.5 * H_prime
discas_max_21_9_60 = 2.0 * H_prime
discas_min_16_9 = 1.5 * H_16_9_full
discas_max_16_9 = 2.0 * H_16_9_full
discas_min_16_9_60 = 1.5 * H_16_9_60_percent
discas_max_16_9_60 = 2.0 * H_16_9_60_percent

# Print the results in the desired format
print("Native Aspect Ratio (21:9)\n")
print("Full Screen Dimensions:\n")
print(f"    Width: {W:.2f} inches")
print(f"    Height: {H:.2f} inches")
print(f"    Diagonal: {diagonal:.2f} inches")
print(f"    DISCAS Min Viewing Distance: {discas_min_21_9:.2f} inches ({inches_to_feet_and_inches(discas_min_21_9)})")
print(f"    DISCAS Max Viewing Distance: {discas_max_21_9:.2f} inches ({inches_to_feet_and_inches(discas_max_21_9)})\n")
print("60% Screen Dimensions (size of 21:9 content in picture-in-picture):\n")
print(f"    Width: {W_prime:.2f} inches")
print(f"    Height: {H_prime:.2f} inches")
print(f"    Diagonal: {D_prime:.2f} inches")
print(f"    DISCAS Min Viewing Distance: {discas_min_21_9_60:.2f} inches ({inches_to_feet_and_inches(discas_min_21_9_60)})")
print(f"    DISCAS Max Viewing Distance: {discas_max_21_9_60:.2f} inches ({inches_to_feet_and_inches(discas_max_21_9_60)})\n")
print("Common Aspect Ratio (16:9)\n")
print("Full Screen Dimensions:\n")
print(f"    Width: {W_16_9_full:.2f} inches")
print(f"    Height: {H_16_9_full:.2f} inches")
print(f"    Diagonal: {D_16_9_full:.2f} inches")
print(f"    DISCAS Min Viewing Distance: {discas_min_16_9:.2f} inches ({inches_to_feet_and_inches(discas_min_16_9)})")
print(f"    DISCAS Max Viewing Distance: {discas_max_16_9:.2f} inches ({inches_to_feet_and_inches(discas_max_16_9)})\n")
print("60% Screen Dimensions (size of 16:9 content pillarboxed on 21:9 in picture-in-picture):\n")
print(f"    Width: {W_16_9_60_percent:.2f} inches")
print(f"    Height: {H_16_9_60_percent:.2f} inches")
print(f"    Diagonal: {D_16_9_60_percent:.2f} inches")
print(f"    DISCAS Min Viewing Distance: {discas_min_16_9_60:.2f} inches ({inches_to_feet_and_inches(discas_min_16_9_60)})")
print(f"    DISCAS Max Viewing Distance: {discas_max_16_9_60:.2f} inches ({inches_to_feet_and_inches(discas_max_16_9_60)})\n")
