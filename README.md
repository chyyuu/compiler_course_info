# README

# 清华大学编译原理课程（2021秋季）

计算机专业主干课， 编译程序（系统）是计算机系统的核心支撑软件， 贯穿程序语言、运行时系统、体系结构， 联系计算机科学和计算机系统的典范。

## 教师
- 王生原 wwssyy@tsinghua.edu.cn
- 陈  渝 yuchen@tsinghua.edu.cn
- 姚海龙 hailongyao@tsinghua.edu.cn

## 助教

- 寇明阳 唐适之 曾军 谢兴宇 刘润达 周智 陈之杨 杨耀良


## 教学目的
掌握编译程序/系统设计的基本原理；掌握“常见”语言机制的实现技术；经历开发一个小型编译程序的主要阶段；自学并使用自动构造工具；加深对计算机系统的理解；会将所学知识灵活应用。

## 先修课程/知识
- 《程序设计》（Java, C/C++，RUST，Scala,...）
- 《数据结构》
- 《形式语言与自动机》（optional）
- 《计算机组成原理》（optional）（MIPS, RISC-V, X86, ARM,...）

## 时间地点
2021-09-15 至 2021-12-22
- 每周三下午 1:30-3:05，二教403 陈

  


## 本课程学习流程（for拿清华学分的同学）
```
  for (i=1; i<=16; i++) {
    1. 预习(optional)
    2. 完成第i周作业(optional)
    3. 上课听讲，提问/被提问
    4. 在deadline前，按序完成compiler_lab实验
    5. 复习，做课后练习，if (碰到问题)　到微信/网络学堂上提问;
    }
  在考试周参加期末考试;
```
## 课程参考书
- Compilers：Principles, Techniques, and Tools， Alfred V.Aho, Ravi Sethi, Jeffrey D.Ullman, Addison Wesley, 2007（龙书）
- Crafting a Compiler, Charles N. Fischer, Ronald K.Cytron,  Richard J. LeBlanc, Jr., 2010.
- Modern Compiler Implementation in Java/C  Andrew W.Appel，2005    （虎书）
- Advanced Compiler Design and Implementation,Steven S. Muchnick, 1997（鲸书）
- The Theory of Parsing, Translation, and Compiling，John E. Hopcroft, Jefferey D. Ullman,    Volume 1 & Volume 2 Prentice-Hall Series in Automatic Computation，1972
- 国内的编译原理教材

## 基本实验
 - [labs of minidecaf compilers](https://decaf-lang.github.io/minidecaf-tutorial/) : 实验覆盖词法分析，语法分析，语义分析，后端代码生成等编译器的完整执行过程。
 - [2021编译课程在线小实验](http://121.36.13.33/)
   - [词法语法在线小实验](https://chyyuu.gitee.io/compiler-toolbox/)：在线实验包括：
     - [Regex => NFA](https://chyyuu.gitee.io/compiler-toolbox/regex2nfa)
     - [Regex => NFA => DFA](https://chyyuu.gitee.io/compiler-toolbox/nfa2dfa)
     - [Regex => NFA => DFA => Min-DFA](https://chyyuu.gitee.io/compiler-toolbox/min_dfa)
     - [Left factoring](https://chyyuu.gitee.io/compiler-toolbox/left_fact)
     - [Left recursion](https://chyyuu.gitee.io/compiler-toolbox/left_rec)
     - [First & Follow](https://chyyuu.gitee.io/compiler-toolbox/first_follow)
     - [LL(1)](https://chyyuu.gitee.io/compiler-toolbox/ll1)
     - [LL(1) Parser Visualization](https://www.cs.princeton.edu/courses/archive/spring20/cos320/LL1/)
     - [LR(0)/SLR(1)](https://chyyuu.gitee.io/compiler-toolbox/lr0)
     - [LR(1)](https://chyyuu.gitee.io/compiler-toolbox/lr1)
     - [LALR](https://chyyuu.gitee.io/compiler-toolbox/lalr)
   - [grammophone: analyzing and transforming context-free grammars](https://chyyuu.gitee.io/grammophone/)
   - [LL/LR/SLR/LALR parser live-demo](https://chyyuu.gitee.io/parser-demo/)
   - [2021 minidecaf compiler using python](http://121.36.13.33/py)
   - [2021 minidecaf compiler using CPP](http://121.36.13.33/cpp)
   - [2020 minidecaf compiler using python](http://121.36.13.33/dzy) 
## ReadingList 编译原理课扩展实验
希望看看编译技术如何用在科研方面或工程项目方面的同学可看看[相关论文和对应的project](https://github.com/chyyuu/compiler_course_info/blob/master/readinglist.md)

## [其他相关资源](https://github.com/chyyuu/compiler_course_info/blob/master/resources.md)
