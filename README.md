# Markov chain Monte Carlo(MCMC) for Bayesian inference 
## 1. *Why Bayesian inference?*
#### Bayesian inference is usually used to make statements about the Universe based on data. 
In particular in gravitational-wave astronomy Bayesian inference allows us to reconstruct sky maps of where an astrophysical event has occurred. 
#### First of all we have to construct a posterior distribution 
$p(\theta |d)$

where $\theta$ is a set of parameters and $d$ the experimental data.

The posterior distribution is what we use to construct credible intervals that gives us informations about the parameters.

According to **Bayes** theorem, the posterior distribution is given by

$p(\theta|d))=\frac{\mathcal{L}(d|\theta)\pi(\theta)}{\mathcal{Z}}$

where 

* $\mathcal{L}(d|\theta)$ is the **likelihood function** of the data given the parameters
* $\pi(\theta)$ is the **prior distribution** for $\theta$
* $\mathcal{Z}$ is the normalisation factor called **evidence**

The likelihood function is something we choose as a Gaussian

$\mathcal{L}(d|\theta)=\frac{1}{\sqrt{2\pi\sigma^{2}}}exp \big( -\frac{1}{2}\frac{(d-\mu(\theta))^{2}}{\sigma^{2}}\big)$

to simulate the noise genereted during data acquisition.
* $\sigma^{2}$ is the so called **variance**
* $\mu$ is the **expected value**
Like the likelihood function, the prior is something we get to choose. 

In most cases it is reasonable to choose a prior that weights each ?? element ??  as equally probable and for this reason we choose a **continuos uniform distribution** in a given interval. 
## 2. *Where's the catch? (problem)?*
#### Let's imagine that we want to calculate the posterior probability for the 15 parameters describing a binary black hole merger.
Even if we create a grid with 10 bins in evert dimension and we evaluate the likelihood at each grid pont our calculation suffers from the curse of the dimensionality (it is computationally impossible to carry out $10^{15}$ likelihood evaluations. 
Of course the problem becomes worse as we add dimensions. 
## 3. *What's the solution?*
#### The solution is to use a **stochastic sampler** divided into two methods: 
* **Markiv chain Monte Carlo (MCMC)** 
* **nested sampling**
In our case we will consider only the MCMC algorithm. 
## 4. *MCMC*
####  In MCMC methods, "walkers" undergo a **random walk** through the posterior distribution where the probability of moving to any given point is determined by the transition probability of the Markov chain.
By noting the position of walkers we generate draws from the posterior probability distribution.
Pratically, this is achieved in two steps:
1. At first a *proposed value* $x_{n+1}=y$ is chosen from a *proposal distribution* $q(y|x_{n})$. This corresponds to the random change of the system's state in the example presented at the beginning. 
2. We have to decide whether or not $y$ has to be accepted as the $(n+1)$-th element of the Markov chain. 
This is done on the basis of the *Metropolis ratio*
$r=\frac{p(y)q(x_{n}|y)}{p(x_{n})q(y|x_{n})}$ 
  * if $r\geq 1$ the proposed value is accepted. 
  * if $r\lt 1$ a uniform random number $U$ is sampled. If $U\leq 1$ the psoposal is accepted, otherwise it is rejected and $x_{n+1}\equiv x_{n}$

For more information on the MCMC click the following link [MCMC](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwiym7Xg2Lf6AhXJvKQKHZFgDskQFnoECB8QAQ&url=https%3A%2F%2Farxiv.org%2Fpdf%2F1909.12313&usg=AOvVaw3NXVML5qyA2WoXTM2zVW48).

## 5. *Our work*
#### Before you analyze the code, there are a two things to keep in mind:
1. The program is written for $n$ parameters.
2. We have no real experimental data and it was necessary to simulate them. 
Of course in this case **we** have to give the function (from which to get the parameters) to the program.

3. We decided to simulate experimental data thanks to the use of a Gaussian distribution: 

   $G(x)=\frac{1}{\sqrt{2\pi\sigma^{2}}}e^{-\frac{(x-\mu)^{2}}{2\sigma^{2}}}$ 

   where $\sigma^{2}$ is the variance and $\mu$ the expected value.
   
   This distribution will perturb the analytical data of the function.

As you can see there are four files. 

In [analytic_model](https://github.com/giulava/esame-/blob/main/analytic_model.py) we have: 
  * The function we will try to recover
  * The noise to be superimposed to the model 
  * The computed experimental data points


In [sampler](https://github.com/giulava/esame-/blob/main/sampler.py) we have: 
  * The likelihood 
  * The prior distribution 
  * The posterior distribution 
  * The MCMC algorithm
  
In [bayesian_inference](https://github.com/giulava/esame-/blob/main/bayesian_inference.py) we have the main part of the code that gives us the plots of the function with the estimated parameters.

In [test](https://github.com/giulava/esame-/tree/main/test) we have hypothesis testing that check the correct action of functions. 

This is what we got by inserting the function $y=Ax\cdot sin(bx+c)$


<img width="1134" alt="Schermata 2022-09-28 alle 20 54 05" src="https://user-images.githubusercontent.com/113693199/192865934-b96578c9-a672-46d7-b307-95d34da28bd5.png">



