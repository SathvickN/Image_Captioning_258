# Image_Captioning_258 (Project Milestone)



I have created a baseline CNN+LSTM model for image captioning task on the Flickr30K dataset.I have trained this baseline model on the Flickr30K dataset and I checked the efficiency of the model using BLEU score.I have also used a pretrained model called BLIP (Bootstrapping Language-Image Pre-training) I used this model to test it on my dataset and checked the BLEU score to see its efficiency on the dataset. I have used The above mentioned modules are fully functional.I will try to increase the efficiency of the above models. I am going to use one more pretrained model called CLIP (Contrastive Language-Image Pre-training) and check its efficiency on my dataset. I will also experiment with other CNN architectures (like ResNet, MobileNet,EfficientNet) to extract visual features from images. I want to compare the accuracy provided by the same model but by using different CNN architectures.This is in the development phase. After this is done I will use Vision Transformers on this dataset and check its performance on the dataset.



The reason to choose the CNN+LSTM architecture as baseline module is because of the research paper “ Show And Tell: A Neural Image Caption Generator” which was the first research paper to use this unique approach of extracting image features using CNN and passing these features into an LSTM to generate the caption for the image.





References 
https://ieeexplore.ieee.org/document/7298935 (Show and tell: A neural image caption generator)
https://arxiv.org/abs/2201.12086  (BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation)
Challenges 
The challenges which I faced initially were related to computational power and memory as it is a very large dataset and has a lot of images.
I am using Kaggle Notebooks with GPU P100 and I will also use HPC to overcome this challenge of computational power and memory
