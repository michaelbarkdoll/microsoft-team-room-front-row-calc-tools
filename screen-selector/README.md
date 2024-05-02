# Program Documentation

## Program Overview
This program calculates the required screen dimensions for displaying content in Microsoft Teams Rooms following AVIXA's DISCAS standards. It supports multiple aspect ratios and adjusts for different content types to determine the optimal screen size based on the viewing distance of the furthest viewer. 

## Key Functionalities
1. **Screen Dimension Calculation**: Determines the minimum necessary screen dimensions (height and width) to ensure content visibility and readability from the furthest viewer, adhering to AVIXA's DISCAS standards.
2. **Aspect Ratio Flexibility**: Supports both 21:9 and 16:9 aspect ratios, allowing customization based on user needs or existing equipment configurations.
3. **Content Type Specific**: Adjusts calculations based on 'general' and 'detailed' content types, applying different visibility standards to each.
4. **Visual Comfort**: Calculates both minimum and maximum recommended viewing distances to ensure content is comfortably viewable without causing eye strain.
5. **Unit Conversion**: Converts measurements from inches to feet and inches for ease of interpretation and practical application.

## Modules and Functions

### `inches_to_feet_and_inches(inches)`
- **Purpose**: Converts inches to a more readable format of feet and inches.
- **Input**:
  - `inches` (float): Measurement in inches.
- **Returns**:
  - A string representing the measurement in feet and inches.

### `calculate_screen_dimensions(furthest_distance, aspect_ratio_width, aspect_ratio_height, content_type)`
- **Purpose**: Calculates minimum screen dimensions required to meet AVIXA's DISCAS standards based on the given aspect ratio and content type.
- **Parameters**:
  - `furthest_distance` (float): Distance from the screen to the furthest viewer in feet.
  - `aspect_ratio_width` (int): Width component of the aspect ratio.
  - `aspect_ratio_height` (int): Height component of the aspect ratio.
  - `content_type` (str): Type of content ('general' or 'detailed'), which affects the visibility requirements.
- **Returns**:
  - A tuple containing the minimum screen height and width in inches.

## Usage Example

```python
# Example usage for a 16:9 aspect ratio screen from a viewer 20 feet away
aspect_ratio_width = 16
aspect_ratio_height = 9
furthest_distance = 20  # Furthest viewer is 20 feet away
content_type = 'general'

minimum_height, minimum_width = calculate_screen_dimensions(furthest_distance, aspect_ratio_width, aspect_ratio_height, content_type)
print(f"Minimum screen dimensions for {content_type} content at a distance of {furthest_distance} ft: {minimum_width:.2f} inches width x {minimum_height:.2f} inches height")
