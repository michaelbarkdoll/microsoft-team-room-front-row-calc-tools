
from math import sqrt, tan, radians

def projector_luminance_calculations_advanced(diagonal_inches, aspect_ratio_width, aspect_ratio_height, inches_to_meters, screen_gain, user_projector_lumens, ambient_lux, alr_ambient_percentage, alr_projector_percentage, half_gain_angle, content_area_percentage):
    diagonal_meters = diagonal_inches * inches_to_meters
    sqrt_sum_of_squares = sqrt(aspect_ratio_width**2 + aspect_ratio_height**2)
    width_inches = (aspect_ratio_width / sqrt_sum_of_squares) * diagonal_inches
    height_inches = (aspect_ratio_height / sqrt_sum_of_squares) * diagonal_inches
    width_meters = width_inches * inches_to_meters
    height_meters = height_inches * inches_to_meters
    screen_area = width_meters * height_meters
    effective_projector_lumens = (user_projector_lumens / screen_gain) * alr_projector_percentage
    effective_ambient_lux = ambient_lux * alr_ambient_percentage
    brightness_lux = effective_projector_lumens / screen_area
    total_effective_brightness = brightness_lux + effective_ambient_lux
    system_contrast_ratio = total_effective_brightness / effective_ambient_lux if effective_ambient_lux != 0 else float('inf')
    half_gain_width = width_meters * tan(radians(half_gain_angle))
    max_viewing_distance = 1.5 * diagonal_meters
    smpte_viewing_distance = 1.6 * height_meters
    thx_viewing_distance = diagonal_meters
    max_thx_viewing_distance = 1.2 * diagonal_meters
    adjusted_content_width = width_meters * sqrt(content_area_percentage)
    adjusted_content_height = height_meters * sqrt(content_area_percentage)
    adjusted_content_area = adjusted_content_width * adjusted_content_height
    discas_recommended_image_size = adjusted_content_height  # Assuming height governs visibility per DISCAS

    results = {
        'Width inches': width_inches,
        'Width meters': width_meters,
        'Height inches': height_inches,
        'Height meters': height_meters,
        'Screen Area sq meters': screen_area,
        'Effective Projector Lumens': effective_projector_lumens,
        'Screen Brightness lux': brightness_lux,
        'Total Effective Brightness with Ambient and ALR': total_effective_brightness,
        'Effective Ambient Lux': effective_ambient_lux,
        'System Contrast Ratio': system_contrast_ratio,
        'Effective Viewing Range at Half Gain Angle (m)': half_gain_width,
        'Maximum Viewing Distance (m)': max_viewing_distance,
        'SMPTE Viewing Distance (m)': smpte_viewing_distance,
        'THX Viewing Distance (m)': thx_viewing_distance,
        'Maximum THX Viewing Distance (m)': max_thx_viewing_distance,
        'Adjusted Content Width (m)': adjusted_content_width,
        'Adjusted Content Height (m)': adjusted_content_height,
        'DISCAS Recommended Image Size (m)': discas_recommended_image_size
    }
    return results

def suggest_improvements(target_contrast_ratio, current_contrast_ratio, current_ambient_lux, current_projector_lumens, screen_area, alr_ambient_percentage):
    max_ambient_lux = current_projector_lumens / screen_area / target_contrast_ratio / alr_ambient_percentage
    required_projector_lumens = current_ambient_lux * target_contrast_ratio * screen_area * alr_ambient_percentage
    required_alr_ambient_percentage = (current_projector_lumens / screen_area) / (current_ambient_lux * target_contrast_ratio)
    suggestions = {
        'Max Ambient Lux for Target Contrast Ratio': max_ambient_lux,
        'Required Projector Lumens for Target Contrast Ratio': required_projector_lumens,
        'Required ALR Ambient Percentage for Target Contrast Ratio': required_alr_ambient_percentage
    }
    return suggestions
    
def print_selected_values(results, selected_keys):
    for key in selected_keys:
        if key in results:
            print(f"{key.capitalize()}: {results[key]}")

def format_output(results):
    formatted_output = ""
    for key, value in results.items():
        formatted_output += f"{key}: {value}\n"
    return formatted_output

def format_improvements(improvements):
    formatted_improvements = ""
    for key, value in improvements.items():
        formatted_improvements += f"{key}: {value}\n"
    return formatted_improvements

# Define the target contrast ratio
target_contrast_ratio = 30
alr_ambient_percentage = 0.7

# Run the functions with specified inputs
output = projector_luminance_calculations_advanced(diagonal_inches=135,
                                                   aspect_ratio_width=21,
                                                   aspect_ratio_height=9,
                                                   inches_to_meters=0.0254,
                                                   screen_gain=1.0,
                                                   user_projector_lumens=3000,
                                                   ambient_lux=110,
                                                   alr_ambient_percentage=0.7,
                                                   alr_projector_percentage=1.0,
                                                   half_gain_angle=30,
                                                   content_area_percentage=0.60)
improvements = suggest_improvements(target_contrast_ratio,
                                    output['System Contrast Ratio'],
                                    output['Effective Ambient Lux'],
                                    output['Effective Projector Lumens'],
                                    output['Screen Area sq meters'],
                                    alr_ambient_percentage)

formatted_output = format_output(output)
formatted_improvements = format_improvements(improvements)

# Define the keys you want to print along with custom print statements
# selected_keys = ['Width meters', 'Height meters', 'Screen Brightness lux', 'Total Effective Brightness with Ambient and ALR', 'System Contrast Ratio']
selected_keys = ['Width inches', 'Width meters', 'Height inches', 'Height meters', 'Screen Area sq meters', 'Effective Projector Lumens'] #'Screen Brightness lux', 'Total Effective Brightness with Ambient and ALR', 'System Contrast Ratio']

print("\nScreen and projector properties:\n")
print_selected_values(output, selected_keys)
# selected_keys = ['Screen Brightness lux', 'Total Effective Brightness with Ambient and ALR', 'System Contrast Ratio']
selected_keys = ['Screen Brightness lux',
                     'Total Effective Brightness with Ambient and ALR',
                     'Effective Ambient Lux',
                     'System Contrast Ratio',
                     'Effective Viewing Range at Half Gain Angle (m)']
print("\nScreen projected properties:\n")
print_selected_values(output, selected_keys)

selected_keys = ['Maximum Viewing Distance (m)',
                     'SMPTE Viewing Distance (m)',
                     'THX Viewing Distance (m)',
                     'Maximum THX Viewing Distance (m)',
                     'Adjusted Content Width (m)',
                     'Adjusted Content Height (m)',
                     'DISCAS Recommended Image Size (m)']
print("\nScreen projected view distance recommendations for 21:9 content:\n")
print_selected_values(output, selected_keys)

print('\nImprovements:')
print('(Max Ambient Lux for Target Contrast Ratio is the level of ambient light to reduce levels to in the room.  Request Projector Lumens is the amount to increase. Required ALR Ambient Percentage is the amount to increase/reduce.)\n')
print(formatted_improvements)
