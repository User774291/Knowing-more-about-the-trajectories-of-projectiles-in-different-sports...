# Knowing-more-about-the-trajectories-of-projectiles-in-different-sports...

I play many diverse sports as hobbies—Tennis,badminton,Ping Pong and volleyball— but not only. I also major in math, physics and chemistry and computer science in highschool which I also consider as hobbies. I then decided to reunite these differents passions in this project which purpose is to study the mouvements of the different projectiles used in the sports I play through a simulation and using the laws of physics involved.

# Using pygame:
I never used pygame so I had to learn how to open a pygame window and all of the different simple tasks possible. I choose pygame because, it was a library that we had talked about in computer science in the context of developping games.
# creating the projectiles
I used a class — **POO**(_Programmation Oriented Objets_)— to create my projectiles. This class essentially stores the information realtive to the image or the shapes displayed. As we were in a two dimensional plan, I had to  divide the speed into it's two components— a speed in the x-axis and a speed in a y-axis— usinf the angle at which it was thrown: I multiplied the speed by the cosine and the sine of the angle to get respectively the speed in the x an y axis. Principle of the mouvement in the simulation can be sumarized as follows: The object are submised to differents forces implying that their speed changes meaning that we have to find the accleration of the object to accurately describe the speed of the object and thus accurately update it's newly calculated coordinates or position by multiplying the speed by the time. 

I then identified the different forces invloved in the mouvement: **the gravitational pull and the aerodynamic dragging force**.   The aerodynamic dragging force vector had to be also decomposed into to the sum of vectors respectively in the x and y axis to know the accelerations of the object from these axis. The formula I used to calculate the accelation is derived from the formula used to calulate the aerodynamic drag applied to an object: F= 1/2*density of the aire*drag coefficient*cross sectional area* speed^2 .
According to Newton's second law, we know that:
**F=mass*acceleation**. As I was looking for the accleration of the object, I deduced the formula:
a=(1/2*density of the aire*drag coefficient*cross sectional area* speed*(speed_x/y))/mass where speed_x/y stands for the speed in the x axis or the y axis giving us the accelaration in the x or the y axis.
  The gravitational pull applies downward, in the y axis, and it is the same for everybody, g the constant of the gravitational fiel on earth which is approximately 9.81. I added g to the accleration from the areodynamic drag in the y axis giving me the total acclelaration in the y axis. As no other force was being applied, the total accelaration in the x axis was just the accelaration in the x axis derived from the areodynamic drag force.
  One problem remained, the coordinate system of pygame which origin is the top left corner of the window instead of the middle and the way of the y axis which was oriented downward. The tricky part of the project was adapting to that by changing the sign of the speed in the y axis to negative as well as the accelaration in the y axis.
# Keeping the esthetics and interaction
  To make the simulation esthetically pleasing, I created frames in the window, I divided the window into four equal parts defined by the intersection of intervals realted to the x and y coordinates and each part hax a backgrounnd corresponding to the sport it corresponds to. For example, for the tennis ball to be in it's frame, it's x coordinates had to be between values a and b and its y axis between c and d. It leaded me to making a loop of the simulation— when one object leaves its frame, it's mouvement restarts. 
  To make the program more interactive withe the user, I created a Tkinter window before the pygame window which fetches the preferences of the user in terms of speed and angle for each sport to see how a changing one affects the mouvement. I also added  buttons not only to let the user know which frame corresponds to which sport but also to let him restart the mouvement at his will.

# How to use the program

To use the program, one must have python, pygame and Tkinter installed in his or her device and to lauch the python program.

_**I hope you will enjoy it. It is my first git hub project, so don't hesitate to tell me if you have any suggestions.
**_



