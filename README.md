
# Max Contrast Ratio Calculator

This application calculates the maximum contrast ratio for a projector-screen setup in a conference room based on various parameters such as ambient light, screen gain, projector lumens, and screen size.

## Requirements

- Python 3.11 or higher
- A CSV file named `screen_database.csv` containing screen data
- A CSV file named `projector_database.csv` containing projector data

## Setup

1. **Install Python:**
   Ensure you have Python 3.11 or higher installed on your system.

2. **Prepare Data Files:**
   - Create a `screen_database.csv` file with the following structure:
     ```csv
     model_name,screen_gain,color_factor,alr_percentage
     ScreenModel1,1.2,0.9,30
     ScreenModel2,1.0,1.0,25
     ```
   - Create a `projector_database.csv` file with the following structure:
     ```csv
     projector_name,lumens,lumen_reduction_percentage
     ProjectorModel1,3000,20
     ProjectorModel2,3500,15
     ```

3. **Place Data Files:**
   Ensure the `screen_database.csv` and `projector_database.csv` files are in the same directory as the `max_contrast_ratio.py` script.

## Usage

1. **Run the Script:**
   Navigate to the directory containing the script and data files, and run the script using Python:
   ```bash
   $ python3.11 max_contrast_ratio-v3.1.py
   ```

2. **Enter or Verify Settings:**
   - If a `settings.ini` file is not found, you will be prompted to enter the required settings for the screen, projector, and room.
   - If a `settings.ini` file exists, the current settings will be displayed, and you will be prompted to verify or update them.

3. **Results:**
   The script will calculate and display the following results:
   - Max screen black level (nit)
   - Screen width (mm)
   - Screen height (mm)
   - Screen area (m²)
   - Max screen white level (nit)
   - Max possible contrast ratio

## Configuration

The `settings.ini` file will store the verified or entered settings. It has the following structure:

```ini
[Screen]
model_name = ScreenModel1
screen_gain = 1.2
color_factor = 0.9
alr_percentage = 30

[Projector]
projector_name = ProjectorModel1
lumens = 3000
lumen_reduction_percentage = 20

[Room]
ambient_light = 275
screen_size = 135
aspect_ratio = 21:9
```

You can manually edit this file to update settings if needed.

## Troubleshooting

- **KeyError: 'screen_gain':**
  This error occurs if the `screen_gain` value is missing in the `settings.ini` file. Ensure all required keys are present in the `settings.ini` file or rerun the script to be prompted for missing values.

- **FileNotFoundError:**
  Ensure that the `screen_database.csv` and `projector_database.csv` files are present in the same directory as the script.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
