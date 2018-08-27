# Airport-schedule-py

This was a home work during Practical optimisation with Python course during which we solved variety of supply chain problems.

We used Python and Gurobi optimiser (student licence).

Task was described in 2.5 page free text in German (additional challange for me!). Please find summary of task contents below.

In this task we were planning operation of a airport as approach to solve scheduling problem. We had to optimise landings so that there are no accidents, buffer times between landings are taken into account and the penalty costs for late or early landing are minimal.

There is a number of planes. Each of them has the earliest possible landing time, best possible landing time (target) and latest possible landing time. 

We had to take into account that:

- there must be buffer times between landings.
- there are penalty costs for not meeting target landing times.

Files description:

- airlandx.txt - data sources, also available at http://people.brunel.ac.uk/~mastjjb/jeb/orlib/files/
- readin.Py - deals with importing above data sources in python readable format
- runscheduling.Py - IP model using Gurobi. First variables are defined, then constraints added , objective of the model to minimise cost is set and then results are specified.
