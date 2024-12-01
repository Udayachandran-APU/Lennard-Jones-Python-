Note: lj_no_numpy.py was what I started out with until I realized I have no choice but to use numpy to speed up the computation. The most releveant and current iteration of the code is lj_numpy.py. It is working really well until 20 particles, after which the potential never converges to the exact minima, it is usually a bit higher. 

# Aim
The aim of this project is to get an introduction to computational thermodynamics. 
# Introduction

# Methods
I am using monte carlo method, where the acceptance criteria is based off a $e^{\frac{E_a}{T}}$. I am also using annealling method, where I reduce down the temperatue slowly so that it explores more areas at the begining, but then focuses on the local minima as the temperature reduces. I it reducing in a linear way. I have also experimented with make it logarithmic and exponential to see how it alters the behaviour and if I can get it to converge better. 

Since it is not converging exactly after 20 particles, one suggestion I found somewhere was to use a method like gradual descent after a certain point so that I get best of both worlds.

Also for the code please check lj_numpy.py
# Results
I am too tired to be able to put proper proper screenshots eventually I should make a new commit when I feel better where it's a proper report but for now I am really sorry but you'll have to run it yourself and check results. Only dependencies I use that you will need should be numpy, everythiong else I used it builtin. You can change the number of particles and other factors. It makes an output under subdirectories for images and csv files but you can remove those lines if you want to. Also it may not work if you try it in linux as the folder naming schemes for windows and linux are differnet I couldn't account for both and make it OS agnostic. 
![lj_numpy](https://github.com/user-attachments/assets/30e058af-0212-456f-97bd-d3b4e7eea4d4) plotted the particles in 3d space using matplotlib. Note that this is actually not the lowest energy config, but it's just some random photo I already had of wrong results. 

# Discussion
I used random youtube videos and websites to figure out the monte carlo method. I think it is my obgligation to also mention the extensive use of chatgpt as a learing tool and for debugging. I mostly used it to fix silly errors with syntax that would have taken way longer to fix. I also used it to understand new lines of code and make it explain how they work amd clear doubts. At some point I directly pasted code from chatpgt, but it was so that I can understand the apporach it took and improve mine. I evenetually wrote everything myself and there shouldn't be any remanants of code from gpt.  

I started out with an easy impletementation withot using numpy and using very simnple logic. I was unaware of the issue with local and global minimas at this point. Once I learnt about how a true monte carlo method worked, I started adapting my code to work with global minima. My early iterations of logic for the code were inefficient at best and downright wrong at worst. But eventually as I learnt more they imrpoved. 

At some point I felt limited by computational speed and the next logical step was to rewrite it all in numpy. This part took me the longest as I had to not only learn numpy syntax but also change my method of doing calculations from whatever it was before to a more "vectorized" matrix manipulation style. I had to learn new concepts such a numpy array broadcasting and extensive slicing to make it more performant. 
# Conclusion
This was really challenging I am sad I was unable to reach cluster with 37 particles but I will keep working on this over the break and hopefully I will reach at least 37 particles. It was a LOT tougher than it initally appeared to be. 
