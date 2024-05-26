---
created: 2024-01-25 13:36:11-08:00
title: DevOps
updated: 2024-01-26 09:10:50-08:00
---

Integrated development and IT Operations as primary responsibility, with focus on automating the fiddly bits of IT.

# Jots

Gives a context for some of the bigger tech changes over the last couple decades

* A whole-ass [Microservice](Microservice.md) architecture is more complicated than a monolith, but its individual components are easier to update, deploy, or phase out completely.
* You can use an orchestrator like *Kubernetes* to configure, fire up, and tear down *Container* collections as a matter of routine, whereas doing the same with a monolith requires greater planning and communication.
* [Terraform](Terraform.md) and similar [Infrastructure as Code](Infrastructure%20as%20Code.md) tools, using a structured language to describe architecture, and [Git](Git.md) or whatever version control system you prefer to see the changing needs over time (and roll back if you screw up)

[YMMV](YMMV.md) because the added complexity means more brains dedicated to maintaining that whole thing — one team can manage one microservice, but with lots of services you'll end up needing a few teams — and a tiny shop would likely be better off having an architecture that can fit in fewer heads: monolith on a server is the easy example. Or they can pay somebody else to think about it, of course.

# Related

* [DevOps - Wikipedia](https://en.wikipedia.org/wiki/DevOps)
* [What is DevOps? | Atlassian](https://www.atlassian.com/devops)
* [DevOps Roadmap: Learn to become a DevOps Engineer or SRE](https://roadmap.sh/devops)