# Facial Recognition Database Management System

Back-end for <https://github.com/ivan-ngchakming/facial-recognition-web>

## Introduction

Facial Recognition Database Management System (FRDMS) is a facial recognition system made for everyone.

Powered by python and react, and packaged into a single executable that can be used by anyone with zero dependencies required.

![Demo](./docs/demo.gif)

## Pages

### Facial Recognition

![Facial Recognition](./docs/rec.png)

### Images

![Images](./docs/images.png)

### Profiles

![Profiles](./docs/profiles.PNG)

### Upload Image

![Upload Images](./docs/upload.png)

## Features

### Facial Recognition (In-progress)

Find a face match by supplying an input image, and the system will search the database to locate possible matches

1. face identification (Done)

   Classifies a face to a specific identity selected from existing profile in the database

2. face verification (In-progress)

   Determine whether a pair of faces belongs to the same identity
   so un-identified faces can be grouped together

3. Batch processing (In-progress)

   To perform the 2 task above in batch.

### Web Crawling (To-do)

Launch web crawling workers to craw through social platforms for images and profiles

### Personnel Classification (To-do)

Face profiles can be classified into multiple groups using supervised or unsupervised machine learning models

### Automatic Profile Creation (To-do)

Supply large amount of unlabelled images into the system to be classified by person.
New unnamed profile can be created automatically when input photo fail to match any existing profiles
Data crawled from social medias will be used to populate newly created profile as much as possible.

### Live Video Recognition (To-do)

Identify known faces in the database from a live video

## Contributing

For guidance on setting up a development environment and how to make a contribution to FRDMS, see the [contributing guidelines](./CONTRIBUTING.md).

## Special Thanks

Special thanks to [Kabiirk](https://github.com/Kabiirk) for making the project logo.
