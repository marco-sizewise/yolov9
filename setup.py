# YOLO v9, GPL-3.0 license

__version__ = "0.3.2"
# import os
from setuptools import setup, find_packages

# Set ENV variables - place before imports -
# if not os.environ.get("OMP_NUM_THREADS"):
#     os.environ["OMP_NUM_THREADS"] = "1"  # default for reduced CPU utilization during training

# Define the setup configuration
setup(
    name="yolov9",  # Package name
    version=__version__,
    author="Sizewise",
    author_email="your_email@example.com",
    description="YOLOv9: A new version of YOLO object detection framework",
    long_description=open("README.md").read(),  # Include README content
    long_description_content_type="text/markdown",
    url="https://github.com/marco-sizewise/yolov9",  # GitHub repository URL
    license="GPL-3.0",
    packages=find_packages(),  # Automatically find packages (like `models`)
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in
    package_data={
        "yolov9": ["models/detect/*.yaml","models/hub/*.yaml","models/segment/*.yaml"],  # Include YAML files in this folder
    },
    python_requires=">=3.9",  # Specify Python version compatibility
    install_requires=open("requirements.txt").read().splitlines(),  # Dependencies from requirements.txt
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],

)
# End of setup.py