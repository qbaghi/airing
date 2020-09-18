ptemceeg
========

**ptemcee** /'tɛmsiː/ (noun):
    `Adaptive parallel tempering <http://arxiv.org/abs/1501.05823>`_ meets |emcee|_.

*ptemcee*, pronounced "tem-cee", is fork of Daniel Foreman-Mackey's |emcee|_ to implement parallel
tempering more robustly.  As far as possible, it is designed as a drop-in replacement for *emcee*.

*ptemceeg* is a fork of Will Vousden's |ptemcee|_ to implement parallel
tempering within a Blocked Gibbs sampler.

If you're trying to characterise awkward, multi-modal probability distributions, 
but want to sample your parameter space by blocks, then *ptemceeg* is
your friend.

.. image:: http://img.shields.io/travis/willvousden/ptemcee/master.svg?style=flat
        :target: http://travis-ci.org/willvousden/ptemcee
.. image:: https://ci.appveyor.com/api/projects/status/3wrvp0ecggmpv0s1?svg=true
        :target: https://ci.appveyor.com/project/willvousden/ptemcee
.. image:: http://img.shields.io/pypi/v/ptemcee.svg?style=flat
        :target: https://pypi.python.org/pypi/ptemcee/
.. image:: http://img.shields.io/badge/license-MIT-blue.svg?style=flat
        :target: https://github.com/willvousden/ptemcee/blob/master/LICENSE
.. image:: http://img.shields.io/badge/arXiv-1501.05823-orange.svg?style=flat
        :target: http://arxiv.org/abs/1501.05823


Attribution
-----------

Please cite `Vousden, Farr, and Mandel (2015) <http://arxiv.org/abs/1501.05823>`_ and `Foreman-Mackey,
Hogg, Lang, and Goodman (2012) <http://arxiv.org/abs/1202.3665>`_ if you find this code useful in your
research.


License
-------

*ptemceeg* is free software distributed under the MIT License; see the `LICENSE
<https://github.com/willvousden/ptemcee/blob/master/LICENSE>`_ file for details.

.. |emcee| replace:: *emcee*
.. _emcee: https://github.com/dfm/emcee
