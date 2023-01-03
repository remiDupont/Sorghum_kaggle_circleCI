# Sorghum competition code using CI/CD
## Intro


This repo contains the code for my submission for [Sorghum kaggle competition](https://www.kaggle.com/competitions/sorghum-id-fgvc-9 "Link to the sorghum image classification competition"). <br> 
**I ranked 29 (top 8 %)** in **only 2 weeks** (my competitors have been working on it for 3 months) using only a single medium size GPU (Nvidia 1080 TI) <br>
My goal on this project was not to spend a lot of time fine-tuning a complex solution (annotating extra data, customizing pipeline,..), but have a **simple yet effective approach** leading to **very good results**, using **simple methods** that I can **implement quickly**. <br>
As an engineer, I know that I have to focus on maintaining a **high quility Ml model while keeping the developement cost (time) low**, so this is what this project intends. <br>
I also used [CircleCI](https://circleci ) as a **CI/CD** tool on this project. <br><br>


### 1) The competition

Sorghum is an open image classification competition with more than 250 teams, where competitors have to correctly **classify images** from 100 different sorghum cultivars grown in June of 2017 

<a href="url"><img src="./markdown_images/kaggke_100.png" height="480" width="480"></a><br>

*Some of the 100 sorghum images to classify*

The Sorghum-100 dataset consists of 48,106 images and 100 different sorghum cultivars grown in June of 2017 (the images come from the middle of the growing season when the plants were quite large but not yet lodging -- or falling over).

Each image is taken using an RGB spectral camera taken from a vertical view of the sorghum plants in the TERRA-REF field in Arizona.



This project use fastaiv2 library and circleCI for CI/CD.

sent

