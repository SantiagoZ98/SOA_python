# SOA with Python on Docker

A simple SOA server using Python, dockerized for easy execution in any environment.

## Description

This is a basic SOA server implemented with Python, which sends a hello to the user using it.

## Technologies used

- Python
- SOA
- Docker

## Prerequisites

To run this project, you must have Docker installed on your machine. If you don't have it, you can download it from [here](https://www.docker.com/products/docker-desktop).

## Instructions to run the project

1. *Clone this repository:*

If you haven't cloned the repository yet, you can do so with the following command:

bash
git clone git clone git clone https://github.com/SantiagoZ98/SOA_python.git

2. **Build the Docker image:**

Before running the container, build the Docker image with the following command:

bash
docker build -t santiagozurita26/my-python-arq3 .

3. *Push the image to Docker Hub (if necessary):*

If you want to push the image to Docker Hub for others to use, you can do so with:

bash
docker push santiagozurita26/my-python-arq3:tagname

4. **Run the Docker container:**

After building the image, run the container with the following command:

bash
docker pull santiagozurita26/my-python-arq3
