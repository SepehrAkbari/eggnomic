# Mathematical Modeling Of A Chicken Egg

To wrap up my high school mathematics course, I decided to take a look at objects around me and try to investigate them with my mathematical knowledge. I was particularly excited about the idea, since it allowed me to develop my own methodology and apply it creatively, rather than following a textbook approach. It did not take long till I lay my eyes on an object simple, yet full of imperfections: the chicken egg. I decided to set a goal for myself: calculate the amount of egg shell (surface area) and the amount of egg white and yolk (volume) of the egg. I knew this would require modeling, which I was excited about, since I new it's full of nuance, and allows for creativity and exploration.

The results include three very different approaches to modeling the egg, each with its own strengths and weaknesses. After obtaining a model, I used it to calculate the surface area and volume of the egg through some simple calculus. Please read the [methodology](#methodology) section for a summary, or read the whole [paper](/paper/IB-MATH-IA-2022.pdf) for a detailed explanation of the process.

## The Egg

The egg used in this project is a standard chicken egg, from my fridge... The goal of this exploration is not to develop a general model of all eggs, but rather investigate different approaches to modeling the egg's curvature and volume. It is however worth noting that every chicken egg has the same oval properties, so the model can be used for other similar shapes as well, with some parameter adjustments.

## Methodology

I started by uploading a picture of my egg to desmos, to get a sense of its curvature and to be able to visualize my models and get a sense of their accuracy. I also automated the process of finding the axis of symmetry and the center with [this script](/scripts/axis.py). I then started with my simplest idea, which was using the standard ellipse equation, and adding a parameter, `c`, to adjust the curvature:

$$
\frac{x^2}{{r_x}^2} + \frac{y^2}{{r_y}^2 + cy} = 1, \quad c > 0
$$

Next, I tried using a more general approach, to try to fit the egg's curvature by just looking at the length of the egg. I used oviform curve, which is a generalization of the ellipse, and has a parameter `w` that adjusts the curvature:

$$
y = \pm \frac{b}{2} \cdot \sqrt{\frac{L^2 + 4x^2}{{L}^2 + 8wx + 4w^2}}
$$

Finally, I tried a more complex approach to raise the accuracy of my model by using polynomials, specifically a Lagrange interpolation. I used three polynomials as a proof of concept, which can, of course, be extended to more polynomials for higher accuracy:

$$P(x) = y_0 \frac{(x-x_1)(x-x_2)\dots(x-x_n)}{(x_0-x_1)(x_0-x_2)\dots(x_0-x_n)} + \dots + y_n \frac{(x-x_0)(x-x_1)\dots(x-x_{n-1})}{(x_n-x_0)(x_n-x_1)\dots(x_n-x_{n-1})}$$

## Contributing

To contribute to this project, you can fork this repository and create pull requests. You can also open an issue if you find a bug or wish to make a suggestion.

## License

This project is licensed under the [GNU General Public License (GPL)](LICENSE).