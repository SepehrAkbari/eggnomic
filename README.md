# Mathematical Modeling Of A Chicken Egg

To wrap up my high school mathematics course, I decided to take a look at objects around me and try to investigate them with my mathematical knowledge. I was particularly excited about the idea, since it allowed me to develop my own methodology and apply it creatively, rather than following a textbook approach. It did not take long till I lay my eyes on an object simple, yet full of imperfections: the chicken egg. I decided to set a goal for myself: calculate the amount of egg shell (surface area) and the amount of egg white and yolk (volume) of the egg. I knew this would require modeling, which I was excited about, since I new it's full of nuance, and allows for creativity and exploration.

The results include three very different approaches to modeling the egg, each with its own strengths and weaknesses. After obtaining a model, I used it to calculate the surface area and volume of the egg through some simple calculus. Please read the [methodology](#methodology) section for a summary, or read the whole [paper](/paper/IB-MATH-IA-2022.pdf) for a detailed explanation of the process.

## The Egg

The egg used in this project is a standard chicken egg, from my fridge... The goal of this exploration is not to develop a general model of all eggs, but rather investigate different approaches to modeling the egg's curvature and volume. It is however worth noting that every chicken egg has the same oval properties, so the model can be used for other similar shapes as well, with some parameter adjustments.

## Methodology

Our journey began with uploading an egg image to Desmos to intuitively grasp its curvature and validate our model's accuracy. To ensure precision, we automated the crucial step of finding the egg's axis of symmetry and center using [a dedicated script](/scripts/axis.py).

We then embarked on a comparative study of three distinct mathematical models to represent the egg's unique profile:

1.  **The Modified Ellipse Equation:** Our simplest initial concept involved the standard ellipse, augmented with a curvature parameter, $c$, to fine-tune its shape:
    $$\frac{x^2}{{r_x}^2} + \frac{y^2}{{r_y}^2 + cy} = 1, \quad c > 0$$
    This method offered a foundational, precise fit to specific egg contours.

2.  **The Oviform Curve:** Seeking a more generalized representation, we adopted the oviform curve, a sophisticated generalization of the ellipse. This model incorporates a parameter, $w$, that directly adjusts the curvature based primarily on the egg's overall length:
    $$y = \pm \frac{b}{2} \cdot \sqrt{\frac{L^2 + 4x^2}{{L}^2 + 8wx + 4w^2}}$$
    To visualize this, we wrote [this script](/scripts/oviform.py) to generate the oviform curve based on given parameters. This approach demonstrated remarkable robustness to minor measurement uncertainties, prioritizing broad applicability.

3.  **Lagrange Interpolation:** For the highest fidelity to specific data points, we explored Lagrange interpolation, a polynomial-based method. As a proof of concept, we utilized three polynomials, a framework easily extensible for even greater accuracy:
    $$P(x) = y_0 \frac{(x-x_1)(x-x_2)\dots(x-x_n)}{(x_0-x_1)(x_0-x_2)\dots(x_0-x_n)} + \dots + y_n \frac{(x-x_0)(x-x_1)\dots(x-x_{n-1})}{(x_n-x_0)(x_n-x_1)\dots(x_n-x_{n-1})}$$
    While offering unparalleled precision in fitting exact coordinates, this method inherently sacrificed generality.

Each of these modeling techniques presented a unique balance of precision and generality. The modified ellipse equation provided a precise fit for specific contours. The oviform curve offered broader applicability based on egg length, robust to measurement uncertainties. Conversely, Lagrange interpolation yielded the highest precision for exact coordinates but lacked generality. For subsequent calculations, the ellipse equation was selected for its optimal balance of simplicity, smoothness, and generality, proving more suitable than the oviform curve's broader fit or Lagrange interpolation's high specificity. Ultimately, each method's utility is application-dependent.

With the egg's profile accurately modeled using the chosen ellipse equation, the final, crucial step was to quantify its three-dimensional properties. We leveraged the power of integral calculus to derive both the volume and surface area of the egg. By revolving the 2D mathematical representation of the egg's curvature around its axis of symmetry, we transformed a geometric shape into tangible, quantifiable metrics. The volume ($V$) was calculated using the disk method (or method of washers) for solids of revolution:

$$V=\pi\int_{a}^{b}[f(y)]^{2}dy$$

And the surface area ($A$) was determined by revolving the curve around the axis, using the formula:

$$A=2\pi\int_{a}^{b}f(y)\sqrt{1+[f^{\prime}(y)]^{2}}dy$$

This rigorous mathematical approach allowed us to move beyond visual approximations, providing precise numerical insights into the fascinating geometry of a chicken egg.


## Contributing

To contribute to this project, you can fork this repository and create pull requests. You can also open an issue if you find a bug or wish to make a suggestion.

## License

This project is licensed under the [GNU General Public License (GPL)](LICENSE).