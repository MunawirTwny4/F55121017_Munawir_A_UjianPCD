clear
clc
close all
img = imread ("foto.jpg");
imshow (img)

c = img+30;
imshow (c)

k = 2*c;
imshow(k)

k = c;
k (:,:,1) =2* k(:,:,1);