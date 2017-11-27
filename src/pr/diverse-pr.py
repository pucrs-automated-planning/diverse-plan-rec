#!/usr/bin/env python3

from pddl.pddl import Domain, Problem

class PlanRecognitionProblem:

    def __init__(self, domain, problem, hypotheses):
        assert isinstance(domain,Domain)
        assert isinstance(problem, Domain)
        self.domain = domain


class DiversePlanRec(object):

    def __init__(self):
        pass


