
# 编译原理课拓展实验

All papers included related projects with source code. These excellent papers adopted theory and technology based on Compiler-related and other(such as data mining, machine learning,etc.) Technology.

想进一步了解某篇论文或选定一篇论文或有自己的新颖想法作为拓展实验的目标后，请与王老师和陈老师联系。

## 选题一： Staitc Analysis to Find Bugs/Rules
 - [Improving integer security for systems with Kint](http://pdos.csail.mit.edu/papers/kint:osdi12.pdf),OSDI 2012
 - [Verifying Systems Rules Using Rule-Directed Symbolic Execution](http://www.cs.columbia.edu/~junfeng/papers/woodpecker-asplos13.pdf) ASPLOS 2013
 - [Juxta: Cross-checking Semantic Correctness for File Systems](https://taesoo.gtisc.gatech.edu/pubs/2015/min:juxta.pdf), SOSP 2015
 - [RID: Finding Reference Count Bugs with Inconsistent Path Pair Checking](http://dl.acm.org/citation.cfm?doid=2872362.2872389), ASPLOS 2016
 - [APISan: Sanitizing API Usages through Semantic Cross-checking](https://sslab.gtisc.gatech.edu/assets/papers/2016/yun:apisan.pdf) USENIX SECURITY 2016
 
### 具体要求
1. 深入阅读上述列出的**一篇论文**，理解设计思路，写出阅读报告，并能够给老师做汇报
2. 对论文中的project，能够编译/运行并重现论文中的实验结果，写出实验分析报告，并能够给老师做汇报
3. 针对新的目标(比如另外一个有bug的软件子系统/软件等)，使用论文中的project，发现新（论文中没有提到的）的bug/rule/result，写出分析报告，并能够给老师做汇报
4. 分析理解论文中的project中代码的具体实现，能够升级到新版本（比如以前project是基于llvm-3.6，现在升级到llmv-5.0等），写出project详细分析报告，并能够给老师做汇报
5. 分析理解论文中的project中代码的具体实现，能够改进project（比如提升性能，增加功能，修复bug等），写出改进报告，并能够给老师做汇报

## 选题二： Language improvement for security/safety
 - [Secure Virtual Architecture: A Safe Execution Environment for Commodity Operating Systems](http://llvm.org/pubs/2007-SOSP-SVA.pdf)， SOSP 2007

### 具体要求
1. 深入阅读上述列出的**一篇论文**，理解设计思路，写出阅读报告，并能够给老师做汇报
2. 对论文中的project，能够编译/运行并重现论文中的实验结果，写出实验分析报告，并能够给老师做汇报
3. 针对新的目标(比如另外一个有bug的软件子系统/软件等)，使用论文中的project，发现新（论文中没有提到的）的bug/rule/result，写出分析报告，并能够给老师做汇报
4. 分析理解论文中的project中代码的具体实现，能够升级到新版本（比如以前project是基于llvm-3.6，现在升级到llmv-5.0等），写出project详细分析报告，并能够给老师做汇报
5. 分析理解论文中的project中代码的具体实现，能够改进project（比如提升性能，增加功能，修复bug等），写出改进报告，并能够给老师做汇报

## 选题三： Verification for system correctness
 - [Push-Button Verification of File Systems via Crash Refinement.](http://locore.cs.washington.edu/papers/sigurbjarnarson-yggdrasil.pdf),OSDI 2016
 - [Hyperkernel: Push-Button Verification of an OS Kernel](https://www.sigops.org/sosp/sosp17/program.html), SOSP 2017

### 具体要求
1. 深入阅读上述列出的**一篇论文**，理解设计思路，写出阅读报告，并能够给老师做汇报
2. 对论文中的project，能够编译/运行并重现论文中的实验结果，写出实验分析报告，并能够给老师做汇报
3. 针对新的目标(比如另外一个软件子系统/软件等)，使用论文中的project，发现新（论文中没有提到的）的rule/result，写出分析报告，并能够给老师做汇报
4. 分析理解论文中的project中代码的具体实现，能够升级到新版本（比如以前project升级到最新版本的z3等等），写出project详细分析报告，并能够给老师做汇报
5. 分析理解论文中的project中代码的具体实现，能够改进project（比如提升性能，增加功能，修复bug等），写出改进报告，并能够给老师做汇报

## 选题四：编译器优化方法

1. http://groups.csail.mit.edu/cag/metaopt/
2.	Amir H. Ashouri et al., “MiCOMP: Mitigating the Compiler Phase-Ordering Problem Using Optimization Sub-Sequences and Machine Learning”, ACM Transactions on Architecture and Code Optimization (TACO), Volume 14 Issue 3, September 2017, Article No. 29. Online Available: http://dl.acm.org/citation.cfm?id=3124452
3. Sameer Kulkarni, “IMPROVING COMPILER OPTIMIZATIONS USING MACHINE LEARNING”, PhD Dissertation, University of Delaware, 2014. Online Available: http://udspace.udel.edu/bitstream/handle/19716/13442/2014_Kulkarni_Sameer_PhD.pdf
4. https://arxiv.org/abs/1605.07969v2

### 具体要求
调研内容以基于机器学习方法的编译器优化方法为主。
完成至少8页的文献调研报告，报告以双栏论文格式呈现，附有参考文献，中英文不限。参考文献应尽可能完善，如同时实现原型系统则更佳。

## 选题五：面向基因电路或DNA计算机的编译器
1. Alec A. K. Nielsen et al., “Genetic circuit design automation”, Science, Vol. 352, Issue 6281, 01 Apr, 2016. Online Available: http://science.sciencemag.org/content/352/6281/aac7341
2. http://www.qianlab.caltech.edu/SeesawCompiler/AONtoAO.php
3. https://github.com/fanmin1010/DNA-Compiler
4. Programming DNA Circuits: https://www.microsoft.com/en-us/research/project/programming-dna-circuits/
5. https://luckytoilet.wordpress.com/2016/07/28/a-brief-introduction-to-dna-computing/

### 具体要求
部分参考阅读（请自行完善补充）。
完成至少8页的文献调研报告，报告以双栏论文格式呈现，附有参考文献，中英文不限。参考文献应尽可能完善，如同时实现原型系统则更佳。

## 选题六：面向生物化学试验的编译器

[1] Vaishnavi Ananthanarayanan and William Thies, “Biocoder: A programming language for standardizing and automating biology protocols”, Journal of Biological Engineering, 2010, 4:13. Online Available: https://jbioleng.biomedcentral.com/articles/10.1186/1754-1611-4-13
[2] https://www.microsoft.com/en-us/download/details.aspx?id=52556

### 具体要求
部分参考阅读（请自行完善补充）。
用Python语言或Java语言重写BioCoder，如有必要，可进一步优化和完善生化试验语言的特性。
完成至少8页的文献调研报告，报告以双栏论文格式呈现，附有参考文献，中英文不限。参考文献应尽可能完善，如同时实现原型系统则更佳。

## 选题七：开放性问题】新的机器学习语言及其编译器
目前，主流的机器学习编程采用MATLAB、R、Python、Java、ELM等，需要编程人员具有机器学习基础与实际编程经验，通过问题分析与建模，建立机器学习模型并训练得到模型参数。对于基于神经网络的机器学习模型，还需要通过Tensorflow、Caffe、Theano等框架搭建合适的神经网络结构。思考如何创立一种新的机器学习语言，使得不具备机器学习基础的应用人员能够完成基本的程序设计，提出自己的机器学习要求与数据输入。对应的编译器可以根据以往的求解问题经验，编译程序，产生合适的机器学习模型或神经网络结构，并编译生成Tensorflow、Caffe、Theano等框架上可以运行的代码。该机器学习语言和编译器在未来的类脑计算机上将有重要的应用价值。


