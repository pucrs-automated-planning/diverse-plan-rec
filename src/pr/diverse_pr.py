#!/usr/bin/env python3

from pddl.pddl import Domain, Problem
from pddl.parser import Parser, parse_predicate_instance_list, parse_predicate_instance


class PlanRecognitionProblem:
    def __init__(self, domain, observations, hypotheses, template):
        assert isinstance(domain, Domain)
        assert isinstance(template, Problem)
        self.domain = domain
        self.observations = observations
        self.hypotheses = hypotheses
        self.template = template


class PlanRecognitionProblemParser:
    def __init__(self):
        self.parser = Parser(None)
        self.problem = None

    def _parse_domain(self,domain_file):
        self.parser.domFile = domain_file
        return self.parser.parse_domain()

    def _parse_observations(self,domain,observations_file):
        observations = []
        with open(observations_file, encoding='utf-8') as file:
            iter = self.parser._read_input(file)
            # while not iter.empty():
            #     observations.append()
            observations = parse_predicate_instance_list(iter)
        # TODO validate parsed actions

        return observations

    def _parse_hypotheses(self,domain,hypotheses_file):
        hypotheses = []
        with open(hypotheses_file, encoding="utf-8") as file:
            for hyp in file:
                preds = hyp.split(",")
                hyp_literals = [parse_predicate_instance(self.parser._read_input(p)) for p in preds]
                hypotheses.append(hyp_literals)
        # TODO validate hypotheses with domain
        return hypotheses

    def _parse_template(self,domain,template_file):
        self.parser.probFile = template_file
        return self.parser.parse_problem(domain)

    def parse_pr_problem(self, domain_file, observations_file, hypotheses_file, template_file):
        parser = Parser(domain_file,template_file)
        domain = self._parse_domain(domain_file)
        observations = self._parse_observations(domain, observations_file)
        hypotheses = self._parse_hypotheses(domain,hypotheses_file)
        template = parser.parse_problem(domain)
        return PlanRecognitionProblem(domain,observations, hypotheses, template)




class DiversePlanRec(object):

    def __init__(self):
        pass


