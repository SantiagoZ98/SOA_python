# SOA with Python in Docker

A simple SOA server using python, dockerized for easy execution in any environment.

## Description

This is a basic SOA server implemented with python. 

## Technologies Used

- Python
- SOA
- Docker

## Prerequisites

To run this project, you need to have Docker installed on your machine. If you don't have it, you can download it from [here](https://www.docker.com/products/docker-desktop).

## Instructions to Run the Project

1. *Clone this repository:*

   If you haven't cloned the repository yet, you can do so with the following command:

   bash
   git clone git clone git clone https://github.com/SantiagoZ98/SOA_python.git

2. **Build the Docker image:**

   Before running the container, build the Docker image using the following command:

   bash
   docker build -t santiagozurita26/my-python-arq3 .

3. *Push the image to Docker Hub (if needed):*

   If you'd like to upload the image to Docker Hub for others to use, you can do so with:

   bash
   docker push santiagozurita26/my-python-arq3:tagname

4. **Run the Docker container:**

   After building the image, run the container with the following command:

   bash
   docker pull santiagozurita26/my-python-arq3
