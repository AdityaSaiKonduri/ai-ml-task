import numpy as np
import cv2
import easyocr
from sklearn.cluster import KMeans

def euclidean_dist(x, y):
    return np.sqrt(np.sum((x - y) ** 2))

image_path = 'ai-ml-task\\sample.jpeg'

image = cv2.imread(image_path)
reader = easyocr.Reader(['en'])
results = reader.readtext(image)

extracted_colors = {}

for (bbox, text, prob) in results:
    (top_left, top_right, bottom_right, bottom_left) = bbox
    top_left = tuple(map(int, top_left))
    bottom_right = tuple(map(int, bottom_right))
    text_area = image[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
    reshaped_text_area = text_area.reshape(-1, 3)
    kmeans = KMeans(n_clusters=2)
    kmeans.fit(reshaped_text_area)
    dominant_colors = kmeans.cluster_centers_.astype(int)
    extracted_colors[text.strip()] = dominant_colors

subheads = []
content = []

for text, colors in extracted_colors.items():
    for color in colors:
        if color[0] >= 250 and color[1] >= 250 and color[2] >= 250:
            continue
        elif color[0] <= 30 and color[1] <= 30 and color[2] <= 30:
            content.append(text)
        elif color[0] < color[2] - 100 and color[1] < color[2] - 100:
            subheads.append(text)

heading = subheads[0]
subheads.pop(0)

coordinates = {}

for (bbox, text, prob) in results:
    (top_left, top_right, bottom_right, bottom_left) = bbox
    top_left = tuple(map(int, top_left))
    bottom_right = tuple(map(int, bottom_right))
    center = ((top_left[0] + bottom_right[0]) / 2, (top_left[1] + bottom_right[1]) / 2)
    if text not in coordinates:
        coordinates[text] = [center]
    else:
        coordinates[text].append(center)

result_dict = {subhead: [] for subhead in subheads}

for content_text in content:
    content_centers = coordinates[content_text]
    for content_center in content_centers:
        nearest_subhead = None
        min_distance = float('inf')
        for subhead_text in subheads:
            subhead_center = coordinates[subhead_text][0]
            distance = euclidean_dist(np.array(content_center), np.array(subhead_center))
            if distance < min_distance and content_center[1] > subhead_center[1]:
                min_distance = distance
                nearest_subhead = subhead_text
        if nearest_subhead:
            result_dict[nearest_subhead].append(content_text)
            


for key in result_dict:
    result_dict[key] = ' '.join(result_dict[key])

for key in result_dict.keys():
    if result_dict[key] == '':
        print(key, end=" ")
    else:
        print(f"{key} : {result_dict[key]}")
