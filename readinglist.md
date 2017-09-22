
# 编译原理课拓展实验
**目录**

* [选题一](#选题一-staitc-analysis-to-find-bugsrules)
* [选题二](#选题二-language-improvement-for-securitysafety)
* [选题三](#选题三-verification-for-system-correctness)
* [选题四](#选题四编译器优化方法)
* [选题五](#选题五面向基因电路或dna计算机的编译器)
* [选题六](#选题六面向生物化学试验的编译器)
* [选题七](#选题七开放性问题新的机器学习语言及其编译器)
* [选题八](#选题八语法分析程序的翻译确认)
* [选题九](#选题九静态检查程序的验证)
* [选题十](#选题十编译器验证的翻译确认方法)

These papers included related projects with source code, and adopted theory and technology based on Compiler-related and other(such as data mining, machine learning,etc.) Technology.

想进一步了解某篇论文或选定一篇论文或有自己的新颖想法作为拓展实验的目标后，请与王老师和陈老师联系。

## 选题一： Staitc Analysis to Find Bugs/Rules
 - [Improving integer security for systems with Kint](http://pdos.csail.mit.edu/papers/kint:osdi12.pdf),OSDI 2012

   - [Kint Project](http://css.csail.mit.edu/kint/)

 - [Verifying Systems Rules Using Rule-Directed Symbolic Execution](http://www.cs.columbia.edu/~junfeng/papers/woodpecker-asplos13.pdf) ASPLOS 2013

   - project方面可找陈老师要

 - [Juxta: Cross-checking Semantic Correctness for File Systems](https://taesoo.gtisc.gatech.edu/pubs/2015/min:juxta.pdf), SOSP 2015

   - [juxta project](https://github.com/sslab-gatech/juxta)

 - [RID: Finding Reference Count Bugs with Inconsistent Path Pair Checking](http://dl.acm.org/citation.cfm?doid=2872362.2872389), ASPLOS 2016

   - project方面可找陈老师要 

 - [APISan: Sanitizing API Usages through Semantic Cross-checking](https://sslab.gtisc.gatech.edu/assets/papers/2016/yun:apisan.pdf) USENIX SECURITY 2016

   - [apisan project](https://github.com/sslab-gatech/apisan)

### 具体要求
1. 深入阅读上述列出的**一篇论文**，理解设计思路，写出阅读报告，并能够给老师做汇报
2. 对论文中的project，能够编译/运行并重现论文中的实验结果，写出实验分析报告，并能够给老师做汇报
3. 针对新的目标(比如另外一个有bug的软件子系统/软件等)，使用论文中的project，发现新（论文中没有提到的）的bug/rule/result，写出分析报告，并能够给老师做汇报
4. 分析理解论文中的project中代码的具体实现，能够升级到新版本（比如以前project是基于llvm-3.6，现在升级到llmv-5.0等），写出project详细分析报告，并能够给老师做汇报
5. 分析理解论文中的project中代码的具体实现，能够改进project（比如提升性能，增加功能，修复bug等），写出改进报告，并能够给老师做汇报

## 选题二： Language improvement for security/safety
 - [Secure Virtual Architecture: A Safe Execution Environment for Commodity Operating Systems](http://llvm.org/pubs/2007-SOSP-SVA.pdf)， SOSP 2007

   - [SVA project](https://github.com/jtcriswell/SVA)
   
### 具体要求
1. 深入阅读上述列出的**一篇论文**，理解设计思路，写出阅读报告，并能够给老师做汇报
2. 对论文中的project，能够编译/运行并重现论文中的实验结果，写出实验分析报告，并能够给老师做汇报
3. 针对新的目标(比如另外一个有bug的软件子系统/软件等)，使用论文中的project，发现新（论文中没有提到的）的bug/rule/result，写出分析报告，并能够给老师做汇报
4. 分析理解论文中的project中代码的具体实现，能够升级到新版本（比如以前project是基于llvm-3.6，现在升级到llmv-5.0等），写出project详细分析报告，并能够给老师做汇报
5. 分析理解论文中的project中代码的具体实现，能够改进project（比如提升性能，增加功能，修复bug等），写出改进报告，并能够给老师做汇报

## 选题三： Verification for system correctness
 - [Push-Button Verification of File Systems via Crash Refinement.](http://locore.cs.washington.edu/papers/sigurbjarnarson-yggdrasil.pdf),OSDI 2016

   - [yggdrasil project](http://locore.cs.washington.edu/yggdrasil/)
   
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

## 选题七：开放性问题：新的机器学习语言及其编译器
目前，主流的机器学习编程采用MATLAB、R、Python、Java、ELM等，需要编程人员具有机器学习基础与实际编程经验，通过问题分析与建模，建立机器学习模型并训练得到模型参数。对于基于神经网络的机器学习模型，还需要通过Tensorflow、Caffe、Theano等框架搭建合适的神经网络结构。思考如何创立一种新的机器学习语言，使得不具备机器学习基础的应用人员能够完成基本的程序设计，提出自己的机器学习要求与数据输入。对应的编译器可以根据以往的求解问题经验，编译程序，产生合适的机器学习模型或神经网络结构，并编译生成Tensorflow、Caffe、Theano等框架上可以运行的代码。该机器学习语言和编译器在未来的类脑计算机上将有重要的应用价值。

## 选题八：语法分析程序的翻译确认
在高安全性要求的关键领域，对编译器的要求是非常苛刻的，要确保每个翻译步骤都要进行正确性验证。因为语法分析程序常常由大家认可的自动工具生成，可信度比较高，所以相对于可信编译器的其他设计阶段来说，对语法分析阶段进行严格验证的优先级是较低的。但如果验证代价不是很高的话，就很有必要去做了，为什么不呢？
语法分析程序所采用的算法往往非常复杂，直接对其进行严格的形式化验证是非常困难的，一种办法是采用确认（validating）的方法，仅对翻译前后的程序进行等价性方面的验证，而不对翻译过程进行验证。以下论文介绍了这方面的一项实际工作，用在CompCert编译器（http://compcert.inria.fr/）中。

1. Jacques-Henri Jourdan, François Pottier, and Xavier Leroy. Validating LR(1) parsers. In Programming Languages and Systems -- 21st European Symposium on Programming, ESOP 2012, volume 7211 of Lecture Notes in Computer Science, pages 397--416. Springer, 2012. Available at: http://gallium.inria.fr/~xleroy/publi/validated-parser.pdf 

### 具体要求
1.深入阅读以上论文，理解设计思路，写出阅读报告，并能够给老师做汇报。
2.尝试将该论文的设计思路（或改进后）应用于实际的语法分析程序。源语言可选择本课程实验中的Decaf语言，也可以选择一个实际项目中的语言。后者的语法定义可参见：（http://soft.cs.tsinghua.edu.cn/~wang/projects/L2C/Languages/LustreStar-v6.pdf ）。
注：对于选择后者且能够形成初步成果的同学，我们诚邀将其成果进行改进，并集成到将要开源的L2C可信编译器项目中。若在方法上有所改进，也鼓励撰写相关的论文。正在建设中的开源L2C项目网页见：http://soft.cs.tsinghua.edu.cn:8000/ 。


## 选题九：静态检查程序的验证
这里所说的静态检查程序，不是我们课程中介绍的用于静态语义分析的检查器，而是针对程序动态性质的静态检查。这些动态性质如，程序运行中是不是会发生除零，访问缓冲区是否会越界，等等。普通的找bug程序也通常是通过静态的方法检查动态运行中潜在的bug。与普通找bug的静态分析程序不同，我们这里强调的是要对静态检查程序进行验证。普通找bug程序往往是只能找到某一类bug中的一部分，不是全部，而且若是没找到bug的话，也不代表程序中没有此类bug。而对于经过验证的检查程序，我们的要求是能找到某一类bug的全部，而且如果没找到bug的话，可以保证一定不存在此类bug。
以下论文介绍了一个基于CompCert编译器（http://compcert.inria.fr/）实现的经过验证的静态检查工具verasco的设计：
1. Jacques-Henri Jourdan, Vincent Laporte, Sandrine Blazy, Xavier Leroy, and David Pichardie. A formally-verified C static analyzer. In POPL 2015: 42nd symposium Principles of Programming Languages, pp 247-259. ACM Press, January 2015. Available at: https://hal.inria.fr/hal-01078386/document .

有关Verasco的文档的项目源码，参见  http://compcert.inria.fr/verasco/ .

### 具体要求
1. 深入阅读以上论文，理解设计思路，写出阅读报告，并能够给老师做汇报。
2. 尝试对该论文工作的改进，如增加新的动态特性检查功能。因为难度很大，所以仅要求有设计思路和初步的实验结论。
3. 若是有兴趣，可以尝试在L2C可信编译器项目基础上实现类似该论文工作。当然，我们也只是建议初步尝试。若能够有初步成果，我们诚邀将其成果进行进一步改进，并鼓励撰写相关的论文。正在建设中的开源L2C项目网页见：http://soft.cs.tsinghua.edu.cn:8000/ 。

## 选题十：编译器验证的翻译确认方法
编译器的验证主要有两种方案。一种是直接对翻译过程进行验证，如CompCert编译器（http://compcert.inria.fr/）的设计与实现。另外一种是翻译确认（translation validation）。翻译确认的方法不是直接验证翻译程序，而是用统一的语义框架为某一翻译过程的源和目标代码建模，两个模型之间定义一种特定的语义等价关系，设计一种可自动证明语义等价性的确认程序（返回成功与否，成功时或给出证明脚本，不成功时或给出反例）。两种方案各有利弊。前者是一种比较完美的解决方案，原理上可以保证源程序的一般性质都可以保持到目标程序，然而其缺点是难以扩展，一旦编译器有所变化，证明就可能需要大范围修改。翻译确认的方法只对编译器的输入和输出作检查，而不关心编译器的具体实现，因而具有较好的可重用性，然而，因确认程序本身是编译器的一部分，它必须是一个自动化的过程，这从理论上决定了它可能出现误报（false alarm），从而使程序员无所适从。实际上，根据各个翻译步骤的不同特点，将这两种方案混合使用是十分有益的做法。由于具有可重用性好的特点，翻译确认的方法非常适合于某些优化步骤的验证，优化算法的改进不会对确认程序造成影响。以下是相关工作的部分论文：

1. A. Pnueli, M. Siegel and E. Singerman, "Translation Validation", In Proceedings of TACAS'98, Lecture Notes in Computer Science, Volume 1384, pp 151-166, 1998.
2. A. Pnueli and O. Shtrichman and M. Siegel. Translation validation for synchronous languages, In Proceedings of ICALP'1998. Lecture Notes in Computer Science, Volume 1443, pp 235-246,1998.
3. G. C. Necula. Translation validation for an optimizing compiler. In PLDI 2000, pages 83–95. ACM Press, 2000.  
4. C. W. Barret, Y. Fang, B. Goldberg, Y. Hu, A. Pnueli, and L. Zuck. TVOC: A translation validator for optimizing compilers. In CAV2005, LNCS 3576, pages 291–295. Springer, 2005.
5. J.-B. Tristan, P. Govereau and G. Morrisett. Evaluating Value-Graph Translation Validation for LLVM. In PLDI 2011, pages 295–305. ACM Press, 2011.
6. J.-B. Tristan, X. Leroy. Formal verification of translation validators: A case study on instruction scheduling optimizations. In POPL, pages 17–27, 2008.
7. J.-B. Tristan, X. Leroy. Verified validation of lazy code motion.  In PLDI, pages 316-326, 2009.
8. J.-B. Tristan, Xavier Leroy. A simple, verified validator for software pipelining. In POPL, pages 83-92, 2010.
9. G. Barthe, D. Demange, and D. Pichardie. A formally verified SSA-based middle-end - Static Single Assignment meets CompCert. In ESOP '12, 2012.

注：如有兴趣，为节省时间可以通过email向老师要这些论文，当然也可以从网上搜到后下载。

### 具体要求
1. 深入阅读上述列出的一篇论文，理解设计思路，写出阅读报告，并能够给老师做汇报
2. 对论文中的基于LLVM，GCC，ORC（Open64）或CompCert的project，如果能找到源码的，则可以尝试编译/运行并重现论文中的实验结果，写出实验分析报告，并能够给老师做汇报
3. 基于LLVM，GCC，ORC（Open64）或CompCert，参考以上论文中的工作，尝试实现针对某种优化的翻译确认程序（基本原型即可），写出实验报告，并能够给老师做汇报。
