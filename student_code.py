import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        print("Asserting {!r}".format(fact))

        # If the fact doesn't exist, add to KB
        if isinstance(fact, Fact) and fact not in self.facts:
            self.facts.append(fact)
        elif isinstance(fact, Rule) and fact not in self.rules:
            self.rules.append(fact)
        else:
            print("either exists or not a fact or rule!")

    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
        print("Asking {!r}".format(fact))

        bindings = None
        lb = ListOfBindings()
#        print("lb len before:")
#        print(len(lb))

        for item in self.facts:
            bindings = match(item.statement, fact.statement, None)
            if bindings:
                lb.add_bindings(bindings, fact)

#        print("lb len after:")
#        print(len(lb))

        if len(lb) > 0:
            return lb
        else:
            return False
