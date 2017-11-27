#!/usr/bin/env python3

import unittest

from pr.diverse_pr import PlanRecognitionProblem, PlanRecognitionProblemParser


class TestDiversePR(unittest.TestCase):


    def test_parse_benchmark(self):
        pass

    def test_pr_problem_parsing(self):
        domain_file = "blocks-test/domain.pddl"
        observations_file = "blocks-test/obs.pddl"
        hypotheses_file = "blocks-test/hyp.dat"
        template_file = "blocks-test/template.pddl"
        parser = PlanRecognitionProblemParser()
        pr_problem = parser.parse_pr_problem(domain_file,observations_file,hypotheses_file,template_file)
        self.assertIsNotNone(pr_problem)
