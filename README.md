# s4_example_py

This directory contains a set of examples that solve simple problems
or approximately reproduce simulation results in existing publications.
For a quick set of examples and instructions on how to run the them,
refer to the directories 1d/ for a simple non-MPI script, and
MPI_example/ for a simple MPI script.

该目录包含一组解决简单问题的示例或近似重现现有出版物中的模拟结果。

有关如何运行它们的快速示例和说明，请参阅目录1d/以获取简单的非mpi脚本。

Example listing:

Simple examples
---------------
patterns    - 展示了如何使用各种层图案化方法

fabry_perot - 演示在最简单的结构上执行的常见计算。

1d          - 展示了如何指定一维周期性和需要注意的问题。


Published result examples
-------------------------
Fan_PRB_65_2002             - 通过光子晶体平板传输光谱的简单例子。

Antonoyiannakis_PRB_60_1999 - 演示各种力的作用。
Suh_APL_82_1999_2003        - High Q Fano resonances.
Liu_OE_17_21897_2009        - Resonance enhancement of forces.
Li_JOSA_14_2758_1997        - Convergence test with original FMM
                              reformulation examples, including
                              a non-orthogonal lattice.
Tikhodeev_PRB_66_45102_2002 - Example of transmission spectrum
                              through a photonic crystal slab.
Christ_PRB_70_125113_2004   - Metal grating transmission spectrum.


Other examples
--------------
spectrum_sampler - Demonstrates how to use the SpectrumSampler
                   object on any function.
interpolator - Simple example of how to use the interpolator
               object.
polarization_basis - Shows the vector fields generated for
                     various lattices.
threading - Shows how to parallelize computations when threading
            support is enabled.
magneto - Test case for tensor dieletric compared against analytic
          theory.
