This Docker image was created so I could learn Python and Pandas primarily
Also, I wanted to learn how to create a docker image

The folder "code" is used to store python scripts and test data

Run this command to build thw image.

    docker build -t robs-pandas:latest .

This is the docker run command to instantiate the docker container
setup a volume to the code folder
And then run the Python pandas script from the mapped volume

docker run --rm -v $(pwd)/code:/app/code robs-pandas:latest python /app/code/pandas-readcsv.py



