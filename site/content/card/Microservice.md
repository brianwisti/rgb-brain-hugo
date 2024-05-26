---
created: 2024-01-25 14:33:16-08:00
title: Microservice
updated: 2024-02-25 19:14:21-08:00
---

Software architecture that focuses on services which are:

* independently deployable
* loosely coupled

A microservice's responsibilities should focus on a specific business capability, and be small enough for one small team to own it. Anything the service itself needs is provided by other processes and services on the network. Its output can be used by still more services. It shouldn't have to care about the details of either end.

I come across [UNIX Philosophy](UNIX%20Philosophy.md) sort of thinking that a microservice should have exactly one responsibility. Except I don't see it all that often, and the elevator pitch definition I found doesn't mention it. The important bit is that you can setup and teardown one service without messing up the other services.

But it should probably aim for as few responsibilities as is practical, with "one" being the platonic ideal.

## Related

* [What are microservices?](https://microservices.io)
* [Microservices - Wikipedia](https://en.wikipedia.org/wiki/Microservices)