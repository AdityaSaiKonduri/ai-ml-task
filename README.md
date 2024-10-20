# OCR and Image Text Categorization

This project extracts and categorizes text from an image using Optical Character Recognition (OCR) and K-Means clustering. The purpose is to identify headings, subheadings, and content within the image based on their dominant colors and organize them in a structured format.

## Table of Contents

- [Overview](#overview)
- [Detailed Explanation](#detailed-explanation)
- [Dependencies](#dependencies)
- [Installation](#installation)

## Overview

The script processes an image to:
1. Read text and their bounding boxes using OCR (`easyocr`).
2. Extract dominant colors from the text areas using K-Means clustering.
3. Categorize text as subheadings or content based on the color properties.
4. Organize the extracted information and print it in a structured format.

## Detailed Explanation

### Step 1:
- Importing Dependencies and defining required functions
- Using the `cv2` module, reading the image from the path for the *OCR* to process it.
- `cv2` module reads the image in a *BGR* format.

### Step 2:
- Using the easyOCR module to process the image and obtain the text data in a numpy array form.
- The resulting list will be containing details about the detected text in a three-tuple.
- The tuple consists of the bounding box coordinates, the detected text and the confidence score.

### Step 3:
Both the content and the subheads are present in the same list. The problem arises during the seperation of the extracted content into `subheads` and `content`. 
One of the key differentiating features of the content and subheads is their font color.
To segregate them using font color :
- Iterate through the results list to access the details of each piece of detected text.
- Calculate the rectangular area around the text using the 4 coordinates of the bounding box, this localizes the text in the image.
- Using the localized text area, extract the pixel color values in *BGR (x, y, z)* format.
- Using KMeans Clustering, cluster the images into 2 clusters
- After clustering we observe that one of the two clusters that the text has been assigned to will have *BGR* values (x, y, z) where x, y and z all are greater than 250. This denotes that this value belongs to the white background of the localized text area.
- The other value however will tell us about the font color of the localized text.
- Using the *BGR* values, segregate the subheads and content.
```
subheads = [...]
content = [...]
```

### Step 4:
Now the next step will be to store the euclidean centres of each of the detected text in a seperate dictionary.
- These centre coordinates will be used to assign the content to a subhead.
- To prevent the coordinates data from being overwritten due to the dictionary propery of having unique keys, I'm using a list to store the coordinates in case of multiple instances of a text item.

### Step 5:
1. Initialize a dictionary with keys as subheads and values as an empty list.
```
result_dict = {subhead: [] for subhead in subheads}
```
2. Now for each text in the content list, there might me one or more center coordinates.
3. For each of these center coordinates, find the minimum euclidean distance to a subhead.
```
def euclidean_dist(x, y):
    return np.sqrt(np.sum((x - y) ** 2))
```
4. If the value corresponding to the subhead is an empty list, find distance to the subhead.
5. Else, find the distance to the last element of the list which is the corresponding value to a subhead
6. Repeat the points 4 and 5 to find the min distance. It is compulsory that the position of the content item is below its assigned subhead.
So, update the minimum distance only if it's lesser than the previous minimum distance and the y-coordinate of the center of the content item is greater-than *(in this case)* the y-coordinate of the subhead.
```
if distance < min_distance and content_center[1] > subhead_center[1]:
    min_distance = distance
    nearest_subhead = subhead_text
```

## Dependencies

The following libraries are required:

- `numpy`
- `opencv-python`
- `easyocr`
- `scikit-learn`
- `torch`
- `torchvision`

Ensure all dependencies are installed before running the script.

## Installation

To install the required packages, run:

```bash
pip install numpy opencv-python easyocr scikit-learn
