# Sorghum competition code using CI/CD
## Intro


This repo contains the code for my submission for [Sorghum kaggle competition](https://www.kaggle.com/competitions/sorghum-id-fgvc-9 "Link to the sorghum image classification competition"). <br> 
**I ranked 29 (top 8 %)** in **only 2 weeks** (my competitors have been working on it for 3 months) using only a **single medium size GPU** (Nvidia 1080 TI) <br>
My goal on this project was not to spend a lot of time fine-tuning a complex solution (annotating extra data, customizing pipeline,..), but have a **simple yet effective approach** leading to **very good results**, using **simple methods** that I can **implement quickly**. <br>
As an engineer, I know that I have to focus on maintaining a **high quility Ml model while keeping the developement cost (time) low**, so this is what this project intends. <br>
I also used [CircleCI](https://circleci ) as a **CI/CD** tool on this project. <br><br>


### 1) The competition

Sorghum is an open image classification competition with more than 250 teams, where competitors have to correctly **classify images** from 100 different sorghum cultivars grown in June of 2017 

<a href="url"><img src="./markdown_images/kaggke_100.png" height="480" width="480"></a><br>

*Some of the 100 sorghum images to classify*

The Sorghum-100 dataset consists of 48,106 images and 100 different sorghum cultivars grown in June of 2017 (the images come from the middle of the growing season when the plants were quite large but not yet lodging -- or falling over).

Each image is taken using an RGB spectral camera taken from a vertical view of the sorghum plants in the TERRA-REF field in Arizona. Image are in png format and are 1024 x 1024 each. 


### 2) CircleCI

[CircleCI](https://circleci ) is as continious integration / continious developement tool (CI/CD). <br> It as been founded in 2011 and it is now one of the most popular CICD platform. It is very similar to buildkite. <br> 
<a href="url"><img src="./markdown_images/circleCI2.jpg" height="380" width="480"></a><br>

Every time I will try to merge a branch to my main branch, CircleCI will perfom some test on my code to ensure everything is working fine. 
I use pytest to perform my test. I had to redefine wich functions pytest had to test threw pytest.ini file as some library I was importing (fastai) had some functions matching the default pytest behavior. <br> 
It is therefore impossible to merge a branch to the main branch if one or several circleCI test have failed. <br>
An other good thing about circleCI is that has it runs in docker container, you are sure your repository contains a perfect description of your environnement, as circleCI will have to reproduce it to test your code. 

### 3) Environnement

My code is in Python3.7, you will find all my package in the requirement.txt [requirements.txt](requirements.txt) file. <br>
With conda, you just have to run : 
 > conda env create -f environment.yml <br>
 > conda activate $new_environment_name <br>
 > jupiter notebook <br>

 I am mainly using [Fastai](https://docs.fast.ai/), you can see it as a very good pytorch wrapper. <br>
 Fastai is developped especialy for jupyter notebook (data visualisation,... ) this is why my code in mainly in [main notebook](main_notebook.ipynb)

 ### 4) The competition

Now that we have our environnement dans CI/CD tools set up correctly, let's foccus on the competition itself. <br>
A mention earlier, my goal here was to have a **simple yet effective approach** leading to **very good results**, using **simple methods** that I can **implement quickly**. <br>
I first used as very simple network, resnet18 that I can train quickly on slamm images (256*256). It is very handy as : 
- a small model is perfect to debug and itterate quickly
- it gave us a good baseline. 

if I do more complex stuff resulting in a similar/lower model performance, **it is therefore very likely that I have a bug**

