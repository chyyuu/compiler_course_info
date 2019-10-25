
## 编译原理课拓展实验/自选实验
**拓展实验目录**

* [选题零 编译器for新语言or新硬件支持](#选题零-编译器for新语言or新硬件支持)
* [选题一 staitc-analysis-to-find-bugsrules](#选题一-staitc-analysis-to-find-bugsrules)
* [选题二 language-improvement-for-securitysafety](#选题二-language-improvement-for-securitysafety)
* [选题三 verification-for-system-correctness](#选题三-verification-for-system-correctness)
* [选题四 静态检查程序的验证](#选题四静态检查程序的验证)
* [选题五 编译器验证的翻译确认方法](#选题五编译器验证的翻译确认方法)
* [选题六 移植CompCert编译器至alpha架构](#选题六移植CompCert编译器至alpha架构)

**自选实验目录**

* [自选一 一种可重构包解析器硬件配置描述语言P3的编译器实现](#自选一一种可重构包解析器硬件配置描述语言P3的编译器实现)
* [自选二 基于同步语言的显示模块开发工具原型的设计与实现](#自选二基于同步语言的显示模块开发工具原型的设计与实现)
* [自选三 C语言子集的编译器](#自选三设计一个C语言的子集并完成此C语言子集的编译链接代码生成工作)
* [自选四 RUST语言子集的编译器](#自选四设计一个RUST语言的子集并完成此RUST语言子集的编译链接代码生成工作)
* [自选五 deductive verification能力的Decaf语言](#自选五在Decaf语言上加入deductiveverification能力)

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
6. 把java版的decaf编译器用rust语言 or go语言重写一遍，看看新语言写编译器是否更快捷，安全，可靠，高性能。

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
 - [Secure Virtual Architecture: A Safe Execution Environment for Commodity Operating Systems](http://llvm.org/pubs/2007-SOSP-SVA.pdf)， SOSP 2007

   - [SVA project](https://github.com/jtcriswell/SVA)

### 具体要求
1. 深入阅读上述列出的**一篇论文**，理解设计思路，写出阅读报告，并能够给老师做汇报
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

## 选题四：静态检查程序的验证
这里所说的静态检查程序，不是我们课程中介绍的用于静态语义分析的检查器，而是针对程序动态性质的静态检查。这些动态性质如，程序运行中是不是会发生除零，访问缓冲区是否会越界，等等。普通的找bug程序也通常是通过静态的方法检查动态运行中潜在的bug。与普通找bug的静态分析程序不同，我们这里强调的是要对静态检查程序进行验证。普通找bug程序往往是只能找到某一类bug中的一部分，不是全部，而且若是没找到bug的话，也不代表程序中没有此类bug。而对于经过验证的检查程序，我们的要求是：如果没找到bug的话，可以保证一定不存在此类bug。然而，“误报”是允许出现的，但要尽可能“减小误报率”。

以下论文介绍了一个基于CompCert编译器（ http://compcert.inria.fr ）实现的经过验证的静态检查工具verasco的设计：
1. [V. Astrauskas and P. Müller and F. Poli and A. J. Summers: Leveraging Rust Types for Modular Specification and Verification,OOPSLA, 2019.](http://pm.inf.ethz.ch/publications/getpdf.php?bibname=Own&id=AstrauskasMuellerPoliSummers19b.pdf) 
有关Prusti项目的源码，参见 https://github.com/viperproject/prusti-dev

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

## 自选实验

打分:

A~D档：对应于完成Decaf实验的 1）必做实验（占总评40%）；2）必做实验+PA4/PA5（占总评50%）；3）必做实验+PA4&PA5（占总评60%）；4）独一档（拓展实验，总评后加5分）。各档次最高得分同Decaf实验。自选实验可以不局限在下面的题目。所有选择自选实验的同学需要进行开题报告，且通过老师和助教的初审。

## 自选一：一种可重构包解析器硬件配置描述语言P3的编译器实现

P3是一种用于实现可重构网络数据包解析器的专用硬件配置描述语言，服务于高安全等级网络的实现。本选题的核心内容是实现P3语言的一个编译器。
主要的需求文档可参见[1]，其中包括P3语言的静态与动态语义的形式化定义，以及编译器中间语言和目标语言的参考语法。另外，感兴趣的同学可以进一步向老师索取P3语言及其编译结构的中文简介，以及一份P3程序样例及其对应的汇编级中间语言代码。

预期收获：1）独立开发小型编译器的经验；2）初步接触程序语言静态语义（类型系统）和动态语义的形式化定义；3）独立探索某些非常规领域语言特性的实现方法。

具体要求和分档情况：

1. 实现从P3源程序至汇编级中间语言代码的基本翻译过程，含最基本的类型检查（如作用域分析/检查），能将所提供的P3程序样例的最基本子集（具体应与老师协商）正确翻译至对应的汇编级中间语言代码。（A档）
2. 实现从P3源程序至汇编级中间语言代码的基本翻译过程，含最基本的类型检查（如作用域分析/检查），能将所提供的P3程序样例正确翻译至对应的汇编级中间语言代码。（B档）
3. 实现从P3源程序至汇编级中间语言代码的完整翻译过程，能将所提供的P3程序样例正确翻译至对应的汇编级中间语言代码，并实现对应于文档[1]中类型系统的完整类型检查。（C档）
4. 实现从P3源程序至汇编级中间语言代码的完整翻译过程，并实现对应于文档[1]中类型系统的完整类型检查，除能将所提供的P3程序样例正确翻译至对应的汇编级中间语言代码之外，能通过更多的样例程序测试，实现较高的覆盖率，基本可以被硬件设计者接受。更多的样例程序由硬件设计者提供或者自行设计，如果软件工程课的作业有需求，可考虑联合实验，探讨样例程序自动生成等课题。（D档）。

补充说明：

1. 实现语言不限；
2. 如果在交互式证明辅助工具Coq[2]环境下实现，可免去词法和语法分析的实现，仅对所提供代码的结构和功能进行简述即可。
3. 如果可以做到A档的要求，可作为托展实验选题。
4. A档和B档的差别主要是前者仅考虑P3语言最核心子集，可忽略翻译过程的一些细节，以便节省工作量和时间。

### Reference

[1] P3 Language Specification ( Draft). Available at:
   https://github.com/leeehh/P3_language_compiler/raw/master/P3_Compiler.pdf.

[2] Coq home, at http://coq.inria.fr/ .

## 自选二：基于同步语言的显示模块开发工具原型的设计与实现

传统的常规语言（如C语言）层次较低，不易使人们聚焦于问题本身，开发效率受到很大影响，并且其最大的不足是难于验证，于是基于模型/模型驱动的开发逐步兴起，在安全攸关领域由模型自动生成的代码（C代码为主）占比已据主导地位。比较著名的建模语言/工具如Simulink，Scade等。有一类建模语言称为同步语言 [1]，特别适合于实时控制系统的开发。所有同步语言均遵循同步假设（synchrony hypothesis），即每个周期内的计算（从输入值得到输出值）都是瞬间完成的。另外，同步语言的语义被要求具有确定性。同步假设以及确定性可以极大地简化实时系统的验证。著名的同步语言如Esterel，Lustre和 Signal。在基于同步语言的开发工具中，最著名的是Scade，其代码生成器将一种基于Lustre的建模语言翻译到C语言，该工具已渗透到我国航空、航天、轨道交通及核电等安全攸关领域。
L2C项目[2]致力于基于Lustre的语言到C语言的可信代码生成器（或称L2C编译器）的研发，在交互式证明辅助工具Coq环境下实现。目前，L2C项目缺乏显示（display）模块开发工具相关的研究。Display模块是实际系统中非常重要的环节，用于实现人机交互。本选题拟探索基于同步语言Lustre的显示模块开发工具原型的设计与实现。可以挂靠L2C项目来完成，也可以独立探索。如果是前者，可基于L2C编译器及其源语言[3]来实现你的设计。如果是后者，建议基于Lustre V6语言[4]及其编译器。

预期收获：1）独立开发小型编译工具的经验；2）了解同步编程的基本思想；3）独立探索基于同步模型的Display模块的实现方法。

具体要求和分档情况：

1. 自行设计或定制某种标记语言（如基于XML），与模型语言（类Lustre同步语言）以及图形库（如OpenGL）一起构建MVC（Model-View-Control）应用。目标是设计与实现此类应用的一个开发工具原型，为此需要实现解析过程、生成控制代码、与模型代码（目标C代码）以及图形库应用接口实现有机对接。能够实现基本框架设计，可以实现一个简单的示例（如简易计算器之类的，具体可与老师协商）。（A档）
2. 在A档基础上，支持Lustre语言的两类核心特性的建模：时钟算子（至少包含when和merge）和时态算子（包含pre/fby算子）。仅支持一个，划为B档；两个都支持，划为C档。
3. 如果能够在A档、B档或C档的工作基础上，进一步设计一种控件之间协同操作的描述语言或者定义规则，并且能够有办法检查在模型层和目标（C代码）层之间的一致性。这一工作应与老师协商后确定。（D档）。
4. D档所述的协同操作描述语言可以基于Lustre语言设计也可以定义独立的语言。对于前者，可基于L2C编译器也可以基于其它Lustre语言编译器（如Lustre v4/v6官方版）实现。对于后者，需自行构建相应的解析和分析程序。
5. D档需求所述的“检查在模型层和目标（C代码）层之间的一致性”，需要实现一个确认程序（validator），可借助各类方法和工具实现，如模型检验器（model checker）、自动求解器（如Z3）、符号执行或者直接编写静态检查程序。对于确认程序，不要求进行其正确性。若基于L2C编译器，可以考虑进一步的研究工作，实现一个确认程序，并证明其正确性（目标是在假设满足确认条件的前提下，可以证明模型层和目标层之间Display逻辑的语义等价关系），如有兴趣可与老师讨论具体方案。

补充说明：
1. 实现语言不限。
2. 如果可以做到A档的要求，可作为托展实验选题。
3. 文献[5]的一些内容可供参考（形式化的部分不必细读，领会论文要义即可）。


### Reference
[1] N. Halbwachs. Synchronous programming of reactive systems, a tutorial and commented bibliography. In Tenth International Conference on Computer-Aided Verification, CAV'98, Vancouver (B.C.), June 1998. LNCS 1427, Springer Verlag.

[2] L2C home, at http://soft.cs.tsinghua.edu.cn/l2c.

[3] Syntax of Lustre∗ for the Open Source L2C Compiler, at
   http://soft.cs.tsinghua.edu.cn/~wang/projects/L2C/Languages/LustreStar-v6.pdf .

[4] Lustre-V6 home, at http://www-verimag.imag.fr/Lustre-V6.html .

[5] Neelakantan R. Krishnaswami,Nick Benton, A Semantic Model for Graphical User Interfaces, ICFP'11, September 19-21, Tokyo.

## 自选三：设计一个C语言的子集并完成此C语言子集的编译链接代码生成工作

C语言是一种简洁的系统语言，用于操作系统等大型系统软件的实现。本选题的核心内容是实现C语言子集的一个基于RUST的编译器/链接器/汇编器，能把基于C语言子集编写的操作系统运行在RISC-V硬件模拟器上。

- 基于C语言的简单操作系统（可进一步裁剪语言和OS）xv6： https://github.com/mit-pdos/xv6-riscv-fall19/tree/xv6-riscv-fall19/kernel
- 一个C语言子集写的简化的compiler/xv6-derived kernel/simulator https://github.com/rswier/swieros

预期收获：1）开发小型编译器的经验；2）定义一个够用的C语言子集；3）探索一个完整编译系统的实现方法。

具体要求和分档情况：
0. 定义够用于编译kernel的C语言子集，用此子集简化OS。用RUST编写编译器。
1. 实现从C语言子集源程序至汇编级中间语言代码的基本翻译过程，含最基本的类型检查（如作用域分析/检查），能将所提供的程序样例正确翻译至对应的汇编级中间语言代码。（A档）
2. 实现从C源程序至汇编级中间语言代码的基本翻译过程，含最基本的类型检查（如作用域分析/检查），能将所50%的xv6可用C语言子集进行修改简化）的C代码部分正确翻译至对应的汇编级中间语言代码。（B档）
3. 实现从C源程序至汇编级中间语言代码的完整翻译过程，能将xv6（可用C语言子集进行修改简化）的全部C代码部分正确翻译至对应的汇编级中间语言代码，并实现类型系统的完整类型检查，能通过测试用例，确保生成的机器代码的正确性。（C档）
4. 实现从xv6源程序（包含C和asm语言）至汇编级中间语言代码的完整翻译过程，并实现类型系统的完整类型检查，能完成部分代码优化的功能实现，可在RISC-V硬件模拟器中运行。如果软件工程课的作业有需求，可考虑联合实验，探讨样例程序自动生成等课题。（D档）。

### Reference
 - https://norasandler.com/2017/11/29/Write-a-Compiler.html
 - https://github.com/onehr/crust
 - https://github.com/buchenglei/rust-simple-c-compiler
 - https://github.com/maekawatoshiki/rucc
 - https://github.com/cmr/lets-build-a-compiler
 - https://github.com/thepowersgang/rust-cc
 - https://github.com/buchenglei/rust-simple-c-compiler
 - https://github.com/asmoaesl/ox
 - https://norasandler.com/2017/11/29/Write-a-Compiler.html 
 - https://www.utam0k.jp/en/blog/2018/10/12/r9cc/
 
## 自选四：设计一个RUST语言的子集并完成此RUST语言子集的编译链接代码生成工作

RUST语言是一种新型系统语言，用于操作系统等大型系统软件的实现。本选题的核心内容是实现RUST语言子集的一个基于RUST的编译器/链接器/汇编器，能把基于RUST语言子集编写的操作系统运行在RISC-V硬件模拟器上。

- 基于RUST语言的简单操作系统（可进一步裁剪语言和OS）rcore： https://github.com/LearningOS/rcore_step_by_step

预期收获：1）开发小型编译器的经验；2）定义一个够用的RUST语言子集；3）探索一个完整编译系统的实现方法。

具体要求和分档情况：
0. 定义够用于编译kernel的RUST语言子集，用此子集简化OS。用RUST编写编译器。
1. 实现从RUST语言子集源程序至汇编级中间语言代码的基本翻译过程，含最基本的类型检查（如作用域分析/检查），能将所提供的程序样例正确翻译至对应的汇编级中间语言代码。（A档）
2. 实现从RUST语言子集源程序至汇编级中间语言代码的基本翻译过程，含最基本的类型检查（如作用域分析/检查），能将所40%的rcore可用RUST语言子集进行修改简化）的RUST代码部分正确翻译至对应的汇编级中间语言代码。（B档）
3. 实现从RUST语言子集源程序至汇编级中间语言代码的完整翻译过程，能将rcore（可用RUST语言子集进行修改简化）的全部RUST代码部分正确翻译至对应的汇编级中间语言代码，并实现类型系统的完整类型检查，能通过测试用例，确保生成的机器代码的正确性。（C档）
4. 实现从rcore源程序（包含RUST和asm语言）至汇编级中间语言代码的完整翻译过程，并实现类型系统的完整类型检查，能完成部分代码优化的功能实现，可在RISC-V硬件模拟器中运行。如果软件工程课的作业有需求，可考虑联合实验，探讨样例程序自动生成等课题。（D档）。


### Reference
 - https://github.com/msiemens/RusTiny
 - [Freie Universität BerlinDepartment of Mathematics and Computer Science Institute of Computer ScienceBachelor Thesis
Design of a Python-subset Compiler in Rust targeting ZPAQL](https://pothos.github.io/papers/bsc_thesis_zpaql_compiler.pdf2htmlEX.html)


## 自选五：在Decaf语言上加入deductiveverification能力
在 Decaf 语言上加入 deductive verification 能力

Deductive Verification 通过让程序员手动标注一些程序需要满足的性质（specification），来证明算法的正确性。
当然，证明要在编译阶段进行——运行阶段的话不就是几个 if 的事情吗？

例如二分查找算法
```java
    static int binsearch(int[] a, int v) {
        int l; l  = 0; int r; r  = a.length(); int mid;

        if (l == r) return -1;

        while (l + 1 < r) {
            mid = (l + r) / 2;
            if (v == a[mid])        return mid;
            else if (v < a[mid])    r = mid;
            else                    l = mid;
        }

        if (v == a[l]) return l;
        return -1;
    }
```

我们希望证明的是
> 在 a 有序的前提下,
> binsearch 要么因为找不到 v 而返回 -1,
> 要么返回一个下标 i 保证 a[i] 等于 v

那么 specification 可能写作注释中一样
```java
    static int binsearch(int[] a, int v)
        // requires isSorted(a)
        // ensures v == -1  ==>  ! Contains(a, v)
        // ensures v >= 0   ==>  v < a.length() && a[result] == v
    {
        int l; l  = 0; int r; r  = a.length(); int mid;

        if (l == r) return -1;

        while (l + 1 < r) {
            mid = (l + r) / 2;
            if (v == a[mid])        return mid;
            else if (v < a[mid])    r = mid;
            else                    l = mid;
        }

        if (v == a[l]) return l;
        return -1;
    }
```

你要完成的就是定义这样一套 specification 语言（嵌入在 Decaf 程序中），并且最后完成它们的验证。

注意我们的工作和普通实验一样，是在已有 Decaf 框架上加新东西，即这套 specification 的语言。
因此你最终的工作应当完全兼容原有 Decaf，方便测试评分。

预期收获：1）和普通实验一样，只不过你的新特性是这套 specification 语言；2）软件形式化验证的实操经验；3）完全兼容 Decaf 并且支持形式化验证，开箱可用的编译器！

具体要求和分档情况：
0. 定义 specification 语言（支持一阶公式 i.e. forall），完成直到中间代码发射的所有工作，验证变成简化的运行期的 if 检查（A档）
1. 定义 specification 语言（支持一阶公式），完成直到中间代码发射的所有工作，验证在编译期检查, 能验证没有递归和循环的程序（B档）
2. 定义 specification 语言（支持一阶公式），完成直到中间代码发射的所有工作，验证在编译期检查, 能验证有递归和循环的程序（C档）

### Reference
[1] The Calculus of Computation - Decision Procedures with Applications to Verification: 基础知识，尤其是第 5 章

[2] Dafny: 微软的实现的验证语言

[3] Why3: 法国人开发的验证语言

[4] Prusti (OOPSLA'19): 嵌入到 Rust 中而不是 decaf 中

[5] Software Foundations: 形式化验证的形式化学习资料

[6] [CMU 15-398](http://www.cs.cmu.edu/~emc/15-398/)

[7] [CMU 15-414](https://www.cs.cmu.edu/~15414/)

[8] [ENS semverif](https://www.di.ens.fr/~rival/semverif-2017/)

[9] [z3](https://github.com/Z3Prover/z3): 大家都喜欢的 z3

