
# 编译原理新研究方向

## AI4Prog/Compiler

### Paper (Code Generation/program synthesis)
From [codegeex blog](https://models.aminer.cn/codegeex/blog/index_zh.html#%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE)

- Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, et al. Evaluating large language models trained on code. arXiv preprint arXiv:2107.03374, 2021.
- Yujia Li, David Choi, Junyoung Chung, Nate Kushman, Julian Schrittwieser, Rémi Leblond, Tom Eccles, James Keeling, Felix Gimeno, Agustin Dal Lago, et al. Competition-level code generation with alphacode. arXiv preprint arXiv:2203.07814, 2022. 
- Erik Nijkamp, Bo Pang, Hiroaki Hayashi, Lifu Tu, Huan Wang, Yingbo Zhou, Silvio Savarese, and Caiming Xiong. A conversational paradigm for program synthesis. arXiv - preprint arXiv:2203.13474, 2022. 
- Daniel Fried, Armen Aghajanyan, Jessy Lin, Sida Wang, Eric Wallace, Freda Shi, Ruiqi Zhong, Wen-tau Yih, Luke Zettlemoyer, and Mike Lewis. InCoder: A generative model for code infilling and synthesis. arXiv preprint arXiv:2204.05999, 2022. 
- Frank F Xu, Uri Alon, Graham Neubig, and Vincent Josua Hellendoorn. A systematic evaluation of large language models of code. In Proceedings of the 6th ACM SIGPLAN International Symposium on Machine Programming, pp. 1–10, 2022. 
- Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung, Charles Sutton, Sebastian Gehrmann, and et al. Palm: Scaling language modeling with pathways. arXiv preprint arXiv:2204.02311, 2022. 
- Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin Clement, Dawn Drain, Daxin Jiang, Duyu Tang, et al. 2021. Codexglue: A machine learning benchmark dataset for code understanding and generation. arXiv preprint arXiv:2102.04664. 
- Ming Zhu, Aneesh Jain, Karthik Suresh, Roshan Ravindran, Sindhu Tipirneni, and Chandan K Reddy. 2022. XLCoST: A benchmark dataset for cross-lingual code intelligence. arXiv preprint arXiv:2206.08474 
- Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu. 2002. Bleu: a method for automatic evaluation of machine translation. In Proceedings of the 40th annual meeting of the Association for Computational Linguistics, pages 311–318. 
- Shuo Ren, Daya Guo, Shuai Lu, Long Zhou, Shujie Liu, Duyu Tang, Neel Sundaresan, Ming Zhou, Ambrosio Blanco, and Shuai Ma. 2020. Codebleu: a method for automatic evaluation of code synthesis. arXiv preprint arXiv:2009.10297. 
- Jacob Austin, Augustus Odena, Maxwell Nye, Maarten Bosma, Henryk Michalewski, David Dohan, Ellen Jiang, Carrie Cai, Michael Terry, Quoc Le, et al. 2021. Program synthesis with large language models. arXiv preprint arXiv:2108.07732. 
- Dan Hendrycks, Steven Basart, Saurav Kadavath, Mantas Mazeika, Akul Arora, Ethan Guo, Collin Burns, Samir Puranik, Horace He, Dawn Song, et al. 2021. Measuring coding challenge competence with apps. arXiv preprint arXiv:2105.09938. 
- Leo Gao, Stella Biderman, Sid Black, Laurence Golding, Travis Hoppe, Charles Foster, Jason Phang, Horace He, Anish Thite, Noa Nabeshima, et al. The pile: An 800gb dataset of diverse text for language modeling. arXiv preprint arXiv:2101.00027, 2020. 
- Alec Radford, Karthik Narasimhan, Tim Salimans, and Ilya Sutskever. Improving language understanding by generative pre training. 2018. 
- Samyam Rajbhandari, Jeff Rasley, Olatunji Ruwase, and Yuxiong He. ZeRO: Memory optimizations toward training trillion parameter models. In SC20: International Conference for High Performance Computing, Networking, Storage and Analysis, pp. 1–16. IEEE, 2020. 
- Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Ed Chi, Quoc Le, and Denny Zhou. Chain of thought prompting elicits reasoning in large language models. arXiv preprint arXiv:2201.11903, 2022. 

### Projects
- [codegeex](https://models.aminer.cn/codegeex/)

### Ideas
- [一些比较有趣的想法](./ai4sysprog.md)

如果同学对这个比较新的方向感兴趣且想探索一下，请联系陈渝老师、唐杰老师

# 编译原理课扩展实验
**扩展实验目录**

* [选题零 编译器for新语言or新硬件支持](#选题零-编译器for新语言or新硬件支持)
* [选题一 staitc-analysis-to-find-bugsrules](#选题一-staitc-analysis-to-find-bugsrules)
* [选题二 language-improvement-for-securitysafety](#选题二-language-improvement-for-securitysafety)
* [选题三 verification-for-system-correctness](#选题三-verification-for-system-correctness)
* [选题四 静态检查与程序验证](#选题四静态检查与程序验证)
* [选题五 编译器验证的翻译确认方法](#选题五编译器验证的翻译确认方法)
* [选题六 移植CompCert编译器至alpha架构](#选题六移植CompCert编译器至alpha架构)
* [选题七 针对TVM的神经网络训练计算图生成](#选题七针对TVM的神经网络训练计算图生成)
* [选题八 HVML 解释器参考实现](#选题八HVML解释器参考实现)

大部分论文都有对应的开放源码的项目，且与编译等技术紧密相关。想进一步了解某篇论文或选定一篇论文或有自己的新颖想法作为拓展实验的目标后，请与王老师、姚老师或陈老师联系。

## 选题零： 编译器for新语言or新硬件支持
- [rust language](https://www.rust-lang.org/en-US/)
- [go language](https://golang.org/)
- [TVM for Machine Learning hardware](https://www.cs.washington.edu/tr/2017/12/UW-CSE-17-12-01.pdf)
- [Bambu: a usable framework for HW-SW Co-Design](https://panda.dei.polimi.it/)
- [LegUP:an open source high-level synthesis tool ](http://legup.eecg.utoronto.ca/)

### 具体要求
1. 深入阅读上述列出的**论文**(Machine Learning hardware)或Go/Rust语言的某种新特征，理解其编译器针对其特征的设计思路，写出阅读报告，并能够给老师做汇报
2. 对Machine Learning hardwar或Go/Rust语言的某种新特征，能够编译/运行并重现实验结果，写出实验分析报告，并能够给老师做汇报
3. 针对新的目标，使用论文中的project，发现新（论文中没有提到的）的result，写出分析报告，并能够给老师做汇报
4. 分析理解一篇论文中的project中代码的具体实现，能够升级到新版本（比如以前project是基于llvm-3.6，现在升级到llmv-5.0等），写出project详细分析报告，并能够给老师做汇报
5. 分析理解一篇论文中的project中代码的具体实现，能够改进project（比如提升性能，增加功能，修复bug等），写出改进报告，并能够给老师做汇报


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
2. 对一篇论文中的project，能够编译/运行并重现论文中的实验结果，写出实验分析报告，并能够给老师做汇报
3. 针对新的目标(比如另外一个有bug的软件子系统/软件等)，使用论文中的project，发现新（论文中没有提到的）的bug/rule/result，写出分析报告，并能够给老师做汇报
4. 分析理解一篇论文中的project中代码的具体实现，能够升级到新版本（比如以前project是基于llvm-3.6，现在升级到llmv-5.0等），写出project详细分析报告，并能够给老师做汇报
5. 分析理解一篇论文中的project中代码的具体实现，能够改进project（比如提升性能，增加功能，修复bug等），写出改进报告，并能够给老师做汇报

## 选题二： Language improvement for security/safety
 - [2.1 Secure Virtual Architecture: A Safe Execution Environment for Commodity Operating Systems](http://llvm.org/pubs/2007-SOSP-SVA.pdf)， SOSP 2007

   - [SVA project](https://github.com/jtcriswell/SVA)

 - 2.2 **How Rust optimizes async/await**
   - [part1](https://tmandry.gitlab.io/blog/posts/optimizing-await-1/)
   - [part2](https://tmandry.gitlab.io/blog/posts/optimizing-await-2/)
   - [Life of an async fn](https://www.youtube.com/watch?v=ZHP9sUqB3Qs)
   - []()
 
### 具体要求
1. 深入阅读上述列出的**一篇论文/文章**，理解设计思路，写出阅读报告，并能够给老师做汇报
2. 对一篇论文中的project，能够编译/运行并重现论文中的实验结果，写出实验分析报告，并能够给老师做汇报
3. 针对新的目标(比如另外一个有bug的软件子系统/软件等)，使用论文中的project，发现新（论文中没有提到的）的bug/rule/result，写出分析报告，并能够给老师做汇报
4. 分析理解一篇论文中的project中代码的具体实现，能够升级到新版本（比如以前project是基于llvm-3.6，现在升级到llmv-5.0等），写出project详细分析报告，并能够给老师做汇报
5. 分析理解一篇论文中的project中代码的具体实现，能够改进project（比如提升性能，增加功能，修复bug等），写出改进报告，并能够给老师做汇报

## 选题三： Verification for system correctness
 - [Push-Button Verification of File Systems via Crash Refinement.](http://locore.cs.washington.edu/papers/sigurbjarnarson-yggdrasil.pdf),OSDI 2016

   - [yggdrasil project](http://locore.cs.washington.edu/yggdrasil/)

 - [Hyperkernel: Push-Button Verification of an OS Kernel](https://unsat.cs.washington.edu/papers/nelson-hyperkernel.pdf), SOSP 2017
   - [hyper kernel project](https://github.com/locore/hv6)

### 具体要求
1. 深入阅读上述列出的**一篇论文**，理解设计思路，写出阅读报告，并能够给老师做汇报
2. 对一篇论文中的project，能够编译/运行并重现论文中的实验结果，写出实验分析报告，并能够给老师做汇报
3. 针对新的目标(比如另外一个软件子系统/软件等)，使用论文中的project，发现新（论文中没有提到的）的rule/result，写出分析报告，并能够给老师做汇报
4. 分析理解一篇论文中的project中代码的具体实现，能够升级到新版本（比如以前project升级到最新版本的z3等等），写出project详细分析报告，并能够给老师做汇报
5. 分析理解一篇论文中的project中代码的具体实现，能够改进project（比如提升性能，增加功能，修复bug等），写出改进报告，并能够给老师做汇报

## 选题四：静态检查与程序验证
这里所说的静态检查程序，不是我们课程中介绍的用于静态语义分析的检查器，而是针对程序动态性质的静态检查。这些动态性质如，程序运行中是不是会发生除零，访问缓冲区是否会越界，等等。普通的找bug程序也通常是通过静态的方法检查动态运行中潜在的bug。与普通找bug的静态分析程序不同，我们这里强调的是要对静态检查程序进行验证。普通找bug程序往往是只能找到某一类bug中的一部分，不是全部，而且若是没找到bug的话，也不代表程序中没有此类bug。而对于经过验证的检查程序，我们的要求是：如果没找到bug的话，可以保证一定不存在此类bug。然而，“误报”是允许出现的，但要尽可能“减小误报率”。

Prusti项目利用Rust的类型系统极大地简化了Rust程序的规范和验证。特别是从Rust编译器执行的程序的类型检查中提取了分离逻辑证明所需的所有权和与框架相关的信息; 用户规范会自动交织在一起，并专注于以类似于Rust程序表达式的语法表示的所需功能保证。

1. [V. Astrauskas and P. Müller and F. Poli and A. J. Summers: Leveraging Rust Types for Modular Specification and Verification,OOPSLA, 2019.](http://pm.inf.ethz.ch/publications/getpdf.php?bibname=Own&id=AstrauskasMuellerPoliSummers19b.pdf) 

有关Prusti项目的源码，参见 https://github.com/viperproject/prusti-dev

以下论文介绍了一个基于CompCert编译器（ http://compcert.inria.fr ）实现的经过验证的静态检查工具verasco的设计：

2. Jacques-Henri Jourdan, Vincent Laporte, Sandrine Blazy, Xavier Leroy, and David Pichardie. A formally-verified C static analyzer. In POPL 2015: 42nd symposium Principles of Programming Languages, pp 247-259. ACM Press, January 2015. Available at: https://hal.inria.fr/hal-01078386/document .

有关Verasco的文档的项目源码，参见  http://compcert.inria.fr/verasco/ .

### 具体要求
1. 深入阅读以上论文，理解设计思路，写出阅读报告，并能够给老师做汇报。
2. 尝试对该论文工作的改进，如增加新的动态特性检查功能。因为难度很大，所以仅要求有设计思路和初步的实验结论。
3. 若是有兴趣，可以尝试在L2C可信编译器项目基础上实现类似该论文工作。当然，我们也只是建议初步尝试。若能够有初步成果，我们诚邀将其成果进行进一步改进，并鼓励撰写相关的论文。正在建设中的开源L2C项目网页见：http://soft.cs.tsinghua.edu.cn/l2c 。

## 选题五：编译器验证的翻译确认方法
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

## 选题六:移植CompCert编译器至alpha架构

CompCert 编译器[1]是形式化验证的可信编译器的杰出代表。该编译器将 C 的一个重要子集 Clight 翻译为 PowerPC 汇编代码(后来也支持 IA32 和 ARM 后端,目前已扩展至可支持 64 位处理器以及开源的 RISC-V 体系结构),其编译过程划分为多个阶段,前端解析过程之后每个阶段的翻译正确性都借助证明辅助工具 Coq 进行了证明,且这些证明可由独立的证明检查器检查,这是迄今最强的形式化验证手段,达到了人们所能期望的最高可信程度[2]。Xuejun Yang等关于 Csmith[3] 的研究工作表明:CompCert 在正确性方面的表现明显优于常用的开源或商用 C 编译器。因 CompCert 编译器的杰出成就,该项目获得了 2012 年微软研究院 Verified Software Milestone 奖,其代表性论文[4]的作者 Xavier Leroy 获得了 2016 年度的十年前最有影响 POPL 论文奖。

目前 CompCert 缺少对“alpha 架构”的支持,后者作为某重要国产处理器参考架构,本选题对于国内军用/民用关键行业有其实际意义。

1. Xavier Leroy. Formal verification of a realistic compiler, Communications of The ACM - CACM , vol. 52, no. 7, pp. 107-115, 2009.
2. Greg Morrisett, Technical Perspective: A Compiler's Story, Communications of theACM, Volume 52, Number 7, pp. 106-106, 2009.
3. Xuejun Yang, Yang Chen, Eric Eide, John Regehr. "Finding and understanding bugs in C compilers". In Proceedings of the 2011 ACM SIGPLAN Conference on Programming Language Design and Implementation (PLDI 2011), pp.283-294, Jun.2011.
4. X. Leroy. Formal certification of a compiler back-end or: programming a compiler with a proof assistant. Proceedings of the 33rd ACM SIGPLAN-SIGACT symposium on Principles of programming languages, 41(1):42–54, January 2006.

### 具体要求
1. 深入理解 CompCert 编译器(http://compcert.inria.fr/)后端部分代码, 参考某个或某几个架构的具体实现,添加 alpha后端,使用交互式证明辅助工具 Coq(Coq home, at http://coq.inria.fr/)或 Ocaml 语言实现。
2. 至少要求可以正常生成 alpha 代码,相关证明代码可暂不考虑。
3. 若有兴趣，可先与老师联系，可能需要进一步向有关单位咨询。

## 选题七:针对TVM的神经网络训练计算图生成

* [TVM:Open Deep Learning Compiler Stack](https://tvm.apache.org/docs/) 
* [TVM in Github](https://github.com/apache/incubator-tvm)
* [TVM Community](https://discuss.tvm.apache.org/)
* [TVM for Pytorch](https://github.com/pytorch/tvm)
* [神经网络与计算图 I](https://medium.com/tebs-lab/deep-neural-networks-as-computational-graphs-867fcaa56c9)
* [神经网络与计算图 II](http://www.cs.cornell.edu/courses/cs5740/2017sp/lectures/04-nn-compgraph.pdf)
* [神经网络推导和训练基础](https://www.zybuluo.com/hanbingtao/note/433855)

### 具体要求

1. 深入阅读理解神经网络编译框架 TVM 的框架及文档，尤其是计算图部分代码，理解 TVM 框架中计算图的特征及设计思路，写出阅读报告，并能够给老师做汇报；
2. 深入阅读理解 Pytorch 对于 TVM 框架的编译流程，理解 Pytorch 针对 TVM 框架实现的支持训练的神经网络的编译方法，写出阅读分析报告，并能够给老师做汇报；
3. 参考 Pytorch 以 TVM 为目标进行编译的方法，实现基于 TVM 原生 IR 的支持训练的计算图生成，需实现特定算子对应的梯度算子。


##  选题八:HVML解释器参考实现

HVML（the Hybrid Virtual Markup Language）是一种全新的、通用的、数据驱动的、虚拟标记语言。HVML 主要用于基于外部数据生成并更新实际的 HTML/XML 文档。在设计上，HVML 和传统的脚本语言有很大的不同，由于抽象层次高，为这类语言开发解释器有一定的挑战。

有关 HVML 的规范草案以及介绍文章，可参阅：

- [漫谈 HVML：它的由来和未来](https://github.com/HVML/hvml-docs/blob/master/zh/brief-introduction-to-hvml-zh.md)
- [HVML 概览](https://github.com/HVML/hvml-docs/blob/master/zh/hvml-overview-zh.md)

### 具体要求

1. 理解 HVML 的设计原理和思路，发现其实际应用价值；
1. 就 HVML 的设计，提供补充或者完善意见；
1. 加入 HVML 解释器参考实现（<https://github.com/HVML/purring-cat>）项目组，参与关键模块（如 JSON 求值表达式解析及求值、解释执行模块、输出模块）的开发。
