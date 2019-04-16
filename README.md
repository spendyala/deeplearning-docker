# Machine Learning Fundamentals - Understanding and Utilizing the Python Library Stack

This repository hold the notebooks, docker images, exercises, etc. for the Machine Learning Fundamentals.

## Prerequisites

1) git - please [install](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and have a basic [working knowledge](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics) of git.
2) docker - please [install](https://docs.docker.com/install/) and have a basic [working knowledge](https://docs.docker.com/get-started/) of docker.
3) python - you may want to have Python3.7 [installed](https://www.python.org/downloads/), although this isn't required. You will want at least an introdctory level of understanding programming in python. (There are numerous sources that will get you up to speed programming python. Try a google search and select the one you fancy.)
4) jupyter - should you elect to install python 3, you may also want to [install](http://jupyter.org/install) jupyter, although this is not required. We also recommend watching or reading through a tutorial to glean a basic understanding of Jupyter prior to participating in these sessions (again, google search...).


# Other Resources for Understanding Machine Learning

## Math Refresher

### Linear Algebra
* [An Intuitive Guide to Linear Algebra](https://betterexplained.com/articles/linear-algebra-guide/)
* [The Essensce of Linear Algebra (YouTube)](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr)
* [MIT OpenCourseWare](https://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/)

### Calculus
* [The Essensce of Calculus (YouTube)](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr)
* [MIT OpenCourseWare](https://ocw.mit.edu/courses/mathematics/18-01sc-single-variable-calculus-fall-2010/)

## Resources for Learning
* [Neural Network Playground](http://playground.tensorflow.org)
* [ML Crash Course](http://developers.google.com/machine-learning/crash-course/ml-intro)
* [Coursera Machine Learning](http://www.coursera.org/learn/machine-learning)
* [Coursera Deep Learning](http://www.coursera.org/specializations/deep-learning)
* [Udacity Machine Learning](https://www.udacity.com/course/intro-to-machine-learning--ud120)
* [Deep Learning by University of San Francisco](https://www.fast.ai/)
* [Python Programming](https://pythonprogramming.net/machine-learning-tutorials/)
* [Computational Linear Algebra](https://www.youtube.com/playlist?list=PLtmWHNX-gukIc92m1K0P6bIOnZb-mg0hY)
* [Spark](https://databricks.com/product/getting-started-guide)

## Interesting Podcasts/VideoCasts
* [Linear Digressions](http://lineardigressions.com/)
* [Data Skeptic](https://dataskeptic.com/)

# Adding python packages to the requirements.txt
- Add to the file `docker/root/tmp/requirements.txt`
- Please don't add the version so that it makes it easier for pip to pick the latest stable version.

# How to use this docker?
- Just clone the package with the following command
  ```
  git clone https://github.com/spendyala/deeplearning-docker.git
  ```
- Run the command in terminal mode
  ```
  run-notebook
  ```
  It should open a browser with Jupyter Notebook.


# Some of the docker commands
| Info | command |
| ------------- |:-------------|
| Running docker containers.      | `docker ps` |
| Docker images      | `docker images` |
| Purging none images to clear space | `docker system prune -a` |
| Remove images | `docker rmi <image>` |
| SSH into running container | `docker exec -it <container_id_from_ps> /bin/sh` |


# Credits to [Daniel Rapp](https://github.com/rappdw).
Without his help and knowledge, this docker image might have taken more time to consolidate and compose this Dockerfile.
