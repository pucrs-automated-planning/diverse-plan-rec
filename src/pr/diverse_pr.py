#!/usr/bin/env python3

from pddl.pddl import Domain, Problem
from pddl.parser import Parser, parse_predicate_instance_list, parse_predicate_instance
# from pddl.lisp_iterators import LispIterator
from pddl.lisp_parser import parse_lisp_iterator

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
            for obs in file:
                iter = parse_lisp_iterator(obs)
                act = parse_predicate_instance(self.parser._read_input(obs))
                observations.append(act)

            # iter = self.parser._read_input(file)
            # while not iter.empty():
            #     observations.append()
            # observations = parse_predicate_instance_list(iter)
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
        template_content = ""
        with open(template_file, encoding="utf-8") as file:
            for line in file:
                if line.find("<HYPOTHESIS>")>=0:
                    line = ""
                template_content+=line+"\n"
        self.parser.probInput = template_content
        return self.parser.parse_problem(domain,read_from_file=False)

    def parse_pr_problem(self, domain_file, observations_file, hypotheses_file, template_file):
        parser = Parser(domain_file,template_file)
        domain = self._parse_domain(domain_file)
        observations = self._parse_observations(domain, observations_file)
        hypotheses = self._parse_hypotheses(domain,hypotheses_file)
        template = self._parse_template(domain, template_file)
        return PlanRecognitionProblem(domain,observations, hypotheses, template)




class DiversePlanRec(object):

    def __init__(self, problem_folder):
        self.problem_folder=problem_folder
        domain_file = problem_folder+"/domain.pddl"
        observations_file = problem_folder+"/obs.dat"
        hypotheses_file = problem_folder+"/hyps.dat"
        template_file = problem_folder+"/template.pddl"
        parser = PlanRecognitionProblemParser()
        self.pr_problem = parser.parse_pr_problem(domain_file, observations_file, hypotheses_file, template_file)


    def build_planning_problem(self):
        domain = self.pr_problem.observations
        domain.predicates