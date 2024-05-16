import configparser
import csv
import math
import os

def load_csv(file_name):
    data = {}
    with open(file_name, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data[row['model_name' if 'screen_gain' in row else 'projector_name']] = row
    return data

def prompt_for_value(prompt, default=None, convert_func=str):
    if default is not None:
        prompt = f"{prompt} [{default}]: "
    else:
        prompt = f"{prompt}: "
    
    value = input(prompt)
    if value.strip() == "" and default is not None:
        return convert_func(default)
    return convert_func(value)

def verify_and_prompt_settings(config):
    for section in config.sections():
        for key in config[section]:
            default = config[section][key]
            new_value = prompt_for_value(f"Enter {key.replace('_', ' ')} for {section}", default, str)
            config[section][key] = new_value

def load_settings():
    config = configparser.ConfigParser()
    screen_data = load_csv('screen_database.csv')
    projector_data = load_csv('projector_database.csv')

    if os.path.exists('settings.ini'):
        config.read('settings.ini')
        print("\nCurrent settings:")
        for section in config.sections():
            for key in config[section]:
                print(f"{section} {key.replace('_', ' ')}: {config[section][key]}")
        print("\nPlease verify or update the settings:")
        verify_and_prompt_settings(config)
    else:
        config['Screen'] = {}
        config['Projector'] = {}
        config['Room'] = {}

    required_screen_keys = ['model_name', 'screen_gain', 'color_factor', 'alr_percentage']
    required_projector_keys = ['projector_name', 'lumens', 'lumen_reduction_percentage']
    required_room_keys = ['ambient_light', 'screen_size', 'aspect_ratio']

    # Prompt for missing Screen settings
    if 'Screen' not in config or not all(key in config['Screen'] for key in required_screen_keys):
        screen_model = input("Enter screen model name: ")
        screen = screen_data.get(screen_model, {})
        config['Screen'] = {
            'model_name': screen_model,
            'screen_gain': prompt_for_value("Enter screen gain", screen.get('screen_gain'), float),
            'color_factor': prompt_for_value("Enter color factor", screen.get('color_factor'), float),
            'alr_percentage': prompt_for_value("Enter ALR percentage", screen.get('alr_percentage'), float)
        }

    # Prompt for missing Projector settings
    if 'Projector' not in config or not all(key in config['Projector'] for key in required_projector_keys):
        projector_model = input("Enter projector model name: ")
        projector = projector_data.get(projector_model, {})
        config['Projector'] = {
            'projector_name': projector_model,
            'lumens': prompt_for_value("Enter projector lumens", projector.get('lumens'), float),
            'lumen_reduction_percentage': prompt_for_value("Enter lumen reduction percentage", projector.get('lumen_reduction_percentage'), float)
        }

    # Prompt for missing Room settings
    if 'Room' not in config or not all(key in config['Room'] for key in required_room_keys):
        config['Room'] = {
            'ambient_light': prompt_for_value("Enter ambient light on screen (lux)", None, float),
            'screen_size': prompt_for_value("Enter screen size (inches, diagonal)", None, float),
            'aspect_ratio': prompt_for_value("Enter the aspect ratio (e.g., '16:9', '21:9')", None, str)
        }

    with open('settings.ini', 'w') as configfile:
        config.write(configfile)

    # Debugging print statement
    print("\nLoaded settings:")
    for section in config.sections():
        for key in config[section]:
            print(f"{section} {key}: {config[section][key]}")
    
    return config

def calculate_screen_properties():
    config = load_settings()

    # Extract values from settings
    ambient_light = float(config['Room']['ambient_light'])
    screen_gain = float(config['Screen']['screen_gain'])
    projector_lumens = float(config['Projector']['lumens'])
    screen_size = float(config['Room']['screen_size'])
    aspect_ratio = config['Room']['aspect_ratio']
    alr_percentage = float(config['Screen']['alr_percentage'])
    color_factor = float(config['Screen']['color_factor'])
    lumen_reduction_percentage = float(config['Projector']['lumen_reduction_percentage'])

    # Parse the aspect ratio
    aspect_width, aspect_height = map(int, aspect_ratio.split(':'))

    # Adjust ambient light based on ALR
    effective_light = ambient_light * (1 - alr_percentage / 100)

    # Reduce projector lumens
    effective_projector_lumens = projector_lumens * (1 - lumen_reduction_percentage / 100)

    # Calculations
    black_level = math.ceil((effective_light / 3.1416) * screen_gain * color_factor)

    # Screen dimensions
    aspect_diagonal = math.sqrt(aspect_width**2 + aspect_height**2)
    width_mm = math.ceil(screen_size / aspect_diagonal * aspect_width * 25.4)
    height_mm = math.ceil(screen_size / aspect_diagonal * aspect_height * 25.4)

    # Screen area in square meters
    area_m2 = (width_mm * height_mm) * 0.000001
    area_m2 = round(area_m2, 2)

    # Max white level
    white_level = math.ceil((effective_projector_lumens / area_m2) * screen_gain * color_factor / 3.1416)

    # Contrast ratio
    contrast_ratio = (white_level + black_level) / black_level
    contrast_ratio = round(contrast_ratio, 1)

    # Display results
    print("\nResults:")
    print(f"Max screen black level: {black_level} nit")
    print(f"Screen width: {width_mm} mm")
    print(f"Screen height: {height_mm} mm")
    print(f"Screen area: {area_m2} m²")
    print(f"Max screen white level: {white_level} nit")
    print(f"Max possible contrast ratio: {contrast_ratio}:1")

if __name__ == "__main__":
    calculate_screen_properties()

