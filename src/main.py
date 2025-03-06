from dotenv import load_dotenv
from gpt_parser import Parser
import os
import matplotlib.pyplot as plt
import numpy as np

from segment import Segment

if __name__ == "__main__":
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    parser = Parser(api_key)

    seg = Segment()
    image_path = "calibration/image.png"

    sentence = input("> ")
    parsed_result = parser.parse_sentence(sentence)
    print(parsed_result)

    results, center_point = seg.segment(image_path, parsed_result["object"], viz=True)
