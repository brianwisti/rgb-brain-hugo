---
aliases:
- LLM
created: 2024-01-19 15:57:31-08:00
title: Large Language Model
updated: 2024-02-01 06:47:47-08:00
---

A particular technology of [Artificial Intelligence](Artificial%20Intelligence.md)

Language models describe a language in terms of probability. Given these tokens, what are the most likely next tokens? That bit's like a Markov chain. LLMs apply billions of parameters to that probability, producing extremely plausible token prediction — at a high computational and energy cost — that can be refined based on responses to user prompts.

Token prediction is not the same as correctness. They only work with the data they have, and lack understanding of context. Great for summarizing text input or telling you what an answer should *look* like, but terrible for things like legal case history or "what does this weird growth on my face mean?" Unless maybe you trained it primarily on case history or weird face growths. But even then I wouldn't assume.

Couple problems with probability-based token generation:

* it's gonna give you something that looks like its training data, which puts a tight constraint on creative / novel token generation
* trends and biases from training data will be reflected in generated tokens

So it's pretty easy to end up with your LLM offering you racist oatmeal. Cleaning up training data can help, but even then you'll end up seeing responses that feel like microaggressions. 

[Retrieval Augmented Generation](Retrieval%20Augmented%20Generation.md) can improve the factual quality of generated tokens by providing access to external APIs.

## Related

* [Language model - Wikipedia](https://en.wikipedia.org/wiki/Language_model)
* [Large language model - Wikipedia](https://en.wikipedia.org/wiki/Large_language_model)
* [Markov chain - Wikipedia](https://en.wikipedia.org/wiki/Markov_chain)