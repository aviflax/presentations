# Clojure/conj 2019 talk proposal: Data Driven Diagramming

## Abstract

The Clojure community generally believes that everything that *can* be expressed as data generally *should* be, which yields many benefits.

Why then are we still drawing our system architecture diagrams with tools and opaque binary formats that can capture only lines and boxes, rather than using accessible data that captures the full semantics of the domain, as we do in the business systems that we build?

The meager information that _is_ in most diagrams today is nearly impossible to reuse or leverage, leading to duplicative work, data drift, and out-of-date documentation.

In this talk I will describe many problems with the way system architecture is generally conveyed, and how many of those problems can be ameliorated by expressing our diagrams as data.

Finally I’ll show the (Clojure+FLOSS) tools and approach I’ve developed for defining our diagrams as data, and show people how easy it would be for them to get started doing the same.

## Main Ideas

* Diagrams are an excellent way to share knowledge about software systems
* The way system diagrams are created and maintained today has a ton of problems:
	* (I’ll enumerate the problems)
* Expressing the diagrams as data can ameliorate many of these problems
	* and it can make the practice of authoring and maintaining the diagrams far more effective, impactful, and efficient — especially over time
	* (I’ll show how with examples)
	* (I’ll briefly describe how this approach has benefited me, my co-workers, and my company)
* I’ve built some tools to enable this approach
	* (I’ll show them, briefly)
* But there are other options out there as well
	* (I’ll show some of them, briefly)
* Bonus: diagrams are great, but data > diagrams
	* We just wanted to create diagrams, but in service of that we ended up creating a unified, semantic model of all of our systems — as data
	* Turns out, that centralized semantic catalogue of our systems has massive value
	* Each department of a sufficiently large software product organization contains half of a poorly specified, poorly implemented, buggy catalogue of the software systems
	* Sufficiently large orgs need a centralized source of truth for this data
		* And a good way to maintain and improve it over time
	* So I’m evolving my diagramming framework
	* It’s going to become a toolkit for cataloguing and documenting software systems
	* Diagrams will be one of the kinds of documentation that can be authored, published, and maintained via the toolkit
	* But the central focus of the toolkit will be that centralized unified dataset
	* There’ll be, for example, a quick and easy way to deploy a Website that provides for interactive browsing and querying of the data via a browser, and for programmatic querying via HTTP
