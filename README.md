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

Suh_APL_82_1999_2003        - 高Q范诺共振。

Liu_OE_17_21897_2009        - 力的共振增强。

Li_JOSA_14_2758_1997        - 收敛性检验用原FMM重新表述的例子，包括一个非正交格。

Tikhodeev_PRB_66_45102_2002 - 透射光谱通过光子晶体板的例子。

Christ_PRB_70_125113_2004   - 金属光栅透射谱。


Other examples
--------------
spectrum_sampler   - 演示如何在任何函数上使用SpectrumSampler对象。

interpolator       - 如何使用插值器对象的简单示例。

polarization_basis - 显示了为各种格生成的向量场。

threading          - 说明在启用线程支持时如何并行化计算。

magneto            - 张量介质的测试用例与解析理论的比较。
