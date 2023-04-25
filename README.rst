airing
======

*airing* is a fork of Will Vousden's |ptemcee|_ to implement parallel
tempering within a Blocked Gibbs sampler. It means mArkov chaIn monte-caRlo wIthiN Gibbs.
See `Vousden, Farr, and Mandel (2015) <http://arxiv.org/abs/1501.05823>`_ and `Foreman-Mackey,
Hogg, Lang, and Goodman (2012) <http://arxiv.org/abs/1202.3665>`_ for information on *ptemcee*.

We assume that the parameter vector can be separated in two parts $p_1$ and $p_2$, and that $p_2$ can be easily sampled with a special sampler, while the  first block of parameters $p_1$ is sampled via parallel tempering. *ptemceeg* simply implements the following scheme:

1. Sample for p1 | p2 using PTMCMC
2. Sample for p2 | p1 using another sampler


Quick start
-----------
*airing* is used very similarly as *ptemcee*. The only difference is that there are extra arguments to set when instantiating the sampler.
These extra arguments are the following:

* the secondary sampler
* the dimension of the second parameter block
* the extra arguments and keyword arguments of the secondary sampler

License
-------

*airing* is free software distributed under the MIT License; see the `LICENSE
<https://github.com/willvousden/ptemcee/blob/master/LICENSE>`_ file for details.

.. |emcee| replace:: *emcee*
.. |ptemcee| replace:: *ptemcee*
.. _emcee: https://github.com/dfm/emcee
.. _ptemcee: https://github.com/willvousden/ptemcee
