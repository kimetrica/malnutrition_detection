"""Fake module containing a function that can be called with an image path and returns fake data."""
from PIL import Image


def analyze_image(image_path, score=False, classification=False):
    """Accept an image path, optionally score and classification, return fake data."""
    with open(image_path, 'rb') as image_file:
        img = Image.open(image_file)
        result_dict = {'width': img.width, 'height': img.height}
        if score:
            result_dict['score'] = img.width/img.height
        if classification:
            result_dict['classification'] = img.height/img.width
        return result_dict
