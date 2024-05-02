# Microsoft Teams Room Front Row Display Size Calculator

## Overview
This Python program calculates the required screen dimensions for displaying picture-in-picture (PIP) content in Microsoft Teams Rooms Front Row experience following AVIXA's DISCAS standards. It takes into account the furthest viewer's distance and various aspect ratios to determine the optimal screen size for clear visibility and readability. The program can handle both general and detailed content types and supports commonly used aspect ratios such as 21:9 and 16:9.

## Variables Explained
- `diagonal`: The diagonal size of the screen for which you want to calculate the height and width based on the aspect ratio. Adjust this value based on the actual size of the screen you are considering.
- `aspect_ratio_width_21_9` and `aspect_ratio_height_21_9`: These constants define the width and height parts of the aspect ratio for a 21:9 screen. They are used to calculate screen dimensions for this specific aspect ratio.
- `aspect_ratio_width_16_9` and `aspect_ratio_height_16_9`: These constants define the width and height parts of the aspect ratio for a 16:9 screen, which is typical for most video content and presentations.
- `area_factor`: This represents the size reduction percentage (60% in this example) of the main content displayed in Microsoft Teams Room Front Row. It affects the calculations of the new width and height when the main content is scaled down.
- `furthest_distance`: This is the distance in feet from the screen to the furthest viewer. It is crucial for calculating the minimum screen dimensions required for all viewers to comfortably see the content.

## Functions
### `inches_to_feet_and_inches(inches)`
Converts a measurement from inches to a string format in feet and inches for easier readability.
- **Input**: `inches` (float) - the measurement in inches.
- **Returns**: A string representing the measurement in feet and inches.

### `calculate_screen_dimensions(furthest_distance, aspect_ratio_width, aspect_ratio_height, content_type)`
Calculates the minimum screen dimensions required to meet AVIXA's DISCAS standards based on the specified aspect ratio and content type.
- **Parameters**:
  - `furthest_distance` (float): The distance from the screen to the furthest viewer in feet.
  - `aspect_ratio_width` (int): Width part of the aspect ratio.
  - `aspect_ratio_height` (int): Height part of the aspect ratio.
  - `content_type` (str): Type of content ('general' or 'detailed'). 
- **Returns**:
  - A tuple containing the minimum screen height and width in inches.

## Example Usage
Modify the `furthest_distance`, `diagonal`, and `area_factor` variables based on your specific room and screen setup. Run the program to see the calculated screen dimensions and recommended viewing distances. Here's how you adjust the variables:
```python
diagonal = 150  # Modify this as per the screen size you are evaluating
furthest_distance = 17  # Set this to the distance from the screen to the furthest viewer in your setup
area_factor = 0.6  # Adjust this based on how much you want to reduce the main content size
```

After setting the variables, execute the program. The output will include the recommended screen dimensions for both 21:9 and 16:9 content, along with the minimum and maximum viewing distances for each setup.

## How to Run

    - Install Python on your computer if it is not already installed.
    - Save this script as a .py file.
    - Open a command line interface (CLI), navigate to the directory where you saved the file, and run the command:

```shell
python <filename>.py
```

Review the output directly in your CLI to see the calculated dimensions and viewing distances.

```shell 
$ python3.9 MTR-screensize-selector-viewdistance.py
Native Aspect Ratio (21:9)

Full Screen Dimensions:

    Width: 137.87 inches
    Height: 59.09 inches
    Diagonal: 150.00 inches
    DISCAS Min Viewing Distance: 88.63 inches (7ft 4.6in)
    DISCAS Max Viewing Distance: 118.18 inches (9ft 10.2in)

60% Screen Dimensions (size of 21:9 content in picture-in-picture):

    Width: 106.80 inches
    Height: 45.77 inches
    Diagonal: 116.19 inches
    DISCAS Min Viewing Distance: 68.65 inches (5ft 8.7in)
    DISCAS Max Viewing Distance: 91.54 inches (7ft 7.5in)

Common Aspect Ratio (16:9)

Full Screen Dimensions:

    Width: 105.05 inches
    Height: 59.09 inches
    Diagonal: 120.52 inches
    DISCAS Min Viewing Distance: 88.63 inches (7ft 4.6in)
    DISCAS Max Viewing Distance: 118.18 inches (9ft 10.2in)

60% Screen Dimensions (size of 16:9 content pillarboxed on 21:9 in picture-in-picture):

    Width: 81.37 inches
    Height: 45.77 inches
    Diagonal: 93.36 inches
    DISCAS Min Viewing Distance: 68.65 inches (5ft 8.7in)
    DISCAS Max Viewing Distance: 91.54 inches (7ft 7.5in)

DISCAS minimum screen dimensions for aspect ratio 16:9 furthest viewer 20 ft:
Minimum screen dimensions for general 16:9 content at a distance of 20 ft: 53.33 inches (width) x 30.00 inches (height) diag: 61.191865835619396 inches
Minimum screen dimensions for detailed 16:9 content at a distance of 20 ft: 106.67 inches (width) x 60.00 inches (height) diag: 122.38373167123879 inches
Minimum screen dimensions for general 21:9 content at a distance of 20 ft: 70.00 inches (width) x 30.00 inches (height) diag: 76.15773105863909 inches
Minimum screen dimensions for detailed 21:9 content at a distance of 20 ft: 140.00 inches (width) x 60.00 inches (height) diag: 152.31546211727817 inches
```

This program ensures that all participants in a Microsoft Teams Room can comfortably view presentations and other content, adhering closely to professional AV standards.


This markdown file is comprehensive, guiding the end-user on how to modify and use the program effectively. It provides explanations of each variable and step-by-step instructions on how to run the program, making it accessible for users with a basic understanding of Python and command-line operations.
