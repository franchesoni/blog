
# Docker Guide

## Components
We will go through them later

- `Dockerfile`
- Command Line Interface (CLI)
- image
- context 
- Docker daemon
- container

## Introduction

Docker is a software tool that lets you create something similar to "virtual machines" that will be built specifically to run your application. They are supposed to be lightweight and portable. Also, docker containers are isolated but do not need a different OS each like in virtual machines.

<!-- In my case, the application is a Graphical User Interface (GUI) implemented after the work _Reviving Iterative Training with Mask Guidance for Interactive Segmentation_. -->

Once you install docker following the installation documentation on their webpage, you can use this marvelous tool.


## Dockerfile

The "virtual machine" you can create with Docker, whose real name is _container_, can have different programs installed and also different operative systems (OS). The way to define which things this container will include is by writing down a `Dockerfile` (which has to be named like that to be recognized).

The final objective when creating a `Dockerfile` is to be able to run `docker build`. This command builds an _image_ and a _context_. The _image_ is what we called the _container_ before. The _context_ is a set of files at some specified location  `PATH` or `URL`. The `URL` is usually a git repository location.









