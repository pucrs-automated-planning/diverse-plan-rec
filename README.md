# Plan Recognition using Diverse Planning [![Build Status](https://travis-ci.org/pucrs-automated-planning/prob-plan-recognition.svg?branch=master)](https://travis-ci.org/pucrs-automated-planning/prob-plan-recognition)

An implementation of the plan recognition using diverse planners from the [Plan Recognition as Planning Revisited](http://www.cs.toronto.edu/~shirin/Sohrabi-IJCAI-16.pdf) paper 


## Formal definitions from the paper


**Planning Problem:** A planning problem is a tuple $P = (F,A,I,G)$, where $F$ is a finite set of fluent symbols, $A$ is a set of actions with preconditions, $\mathcsc{PRE}(a)$, add effects, $\mathsc{ADD}(a)$, delete effects, $\mathsc{DEL}(a)$, and non-negative action costs, $\mathsc{COST}(a)$, $I \subseteq F$ defines the initial state, and $G \subseteq F$ defines the goal state.

**Plan Recognition Problem:** A plan recognition problem is a tuple $R = (F,A,I,O,\mathcal{G},\mathsc{PROB})$, where $(F,A,I)$ is the planning domain as defined above, $O = [o_1,...,o_m]$, where $o_i \in F$, $i \in [1,m]$ is the sequence of observations, $\mathcal{G}$ is the set of possible goals $G$, $G \subseteq F$ , and $\mathsc{PROB}$ is the goal priors or a probability distribution over $G$.

## Running PR using Diverse Planning

TODO

```bash
```