# OCR and Image Text Categorization

This project extracts and categorizes text from an image using Optical Character Recognition (OCR) and K-Means clustering. The purpose is to identify headings, subheadings, and content within the image based on their dominant colors and organize them in a structured format.

## Table of Contents

- [Overview](#overview)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Example Output](#example-output)

## Overview

The script processes an image to:
1. Read text and their bounding boxes using OCR (`easyocr`).
2. Extract dominant colors from the text areas using K-Means clustering.
3. Categorize text as subheadings or content based on the color properties.
4. Organize the extracted information and print it in a structured format.

## Dependencies

The following libraries are required:

- `numpy`
- `opencv-python`
- `easyocr`
- `scikit-learn`

Ensure all dependencies are installed before running the script.

## Installation

To install the required packages, run:

```bash
pip install numpy opencv-python easyocr scikit-learn
