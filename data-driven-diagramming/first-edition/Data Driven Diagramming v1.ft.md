# Data Driven Diagramming v1

## Intro

### slide

Today I’d like to share some thoughts on something that may seem prosaic, maybe even mundane.

And maybe it is mundane, but it’s something I care about deeply. So I’m going to try to convince you that maybe you should care a little bit too.

## What Is

### slide

[various diagrams]

Diagrams are a powerful and widely used medium for teaching and learning about software systems.

They’re so commonplace that many of us rarely stop to think about how they are created and maintained.

Well, I’ve been creating and maintaining diagrams like these for decades.

Over time, I started asking myself: why am I always, inevitably, drawn towards diagrams and diagramming?

Every time I start a new job, or switch teams, I invariably look for diagrams that can help me learn about my new context — and often I don’t find any, so I create them myself.

What’s going on here?

## Interlude

### slide

[blank, or maybe a blurry diagram]

This was puzzling to me for a long time, because I don’t think of myself as a visual person.

In fact, let me tell you a story.

### slide

[screenshot of Ruby’s tweet]

In April 2016, I was scrolling through my Twitter timeline when I came across this tweet by Sam Ruby (who’s currently the president of Apache) which linked to a tweet by Blake Ross, one of the creators of Firefox.

### slide

[screenshot of Blake’s post]

Blake’s tweet linked to this essay he’d just written.
I followed the link and started reading, and I was astounded.

### slide

[??]

And that’s how I found out that I have a neurological condition called aphantasia — an impaired ability to visualize in my “mind’s eye”

### slide

[screenshot of my tweet]

Suddenly, lots of random idiosyncrasies, tics and quirks of mine fit together, made sense, had a unifying narrative.

In particular, I now, for the first time, had a plausible hypothesis for the quirks of my memory; specifically, how my memory works — or doesn’t.

### slide

[??]

Now, unfortunately, we don’t have time for a comprehensive discussion of how my memory works. But we can discuss one aspect that’s relevant: that I’m basically incapable of memorization.

It’s not that I’m unable to learn new information, and not that I’m unable to access information I’ve previously learned.

I can learn. Just not through memorization.

It’s almost as though I’m just missing certain kinds of indices that other people have. If our memories are data structures, then most people’s seem to be extremely sophisticated structures allowing for random access and multiple indices on the same data.

Whereas my memory seems to be similar to a simplistic tree; the only way to get to a given node seems to be to walk the tree.

The end-result is that I don’t know how to memorize anything intentionally. I see memorization as a kind of brute-force technique that is just incompatible with my wetware. Instead, the only way for me to retain anything usefully is to **really** learn it. To learn it as a system, as a network of connected information, a Web, etc. To **understand** it.

The thing is, though: to truly understand something takes time — often a lot of time.

### slide

[???]

In a world that often equates memory with intelligence, I have developed habits and strategies to compensate for my inability to memorize — for example, I rely heavily on reference materials while writing programs.

### slide

[screenshot of Dash]

For example, this is Dash, one of my favorite programming tools. It downloads and indexes API docs, for… **FINISH**

I’ve come to believe that I use diagrams similarly to these API docs — as a reference, as a sort of an external memory or external index for the systems I need to work with.

There’s another kind of visualization that should be familiar to most of you — a visualization that people often use to get their bearings in a new context, and to learn about that context.

### slide

[map or maps]

When a person enters a new geographical environment, they’ll often refer to maps to get their bearings in that environment and to navigate that environment, until they’ve eventually committed the geographical information they need regularly to memory — in other words, until they’ve learned that environment.

I believe that, for me, a diagram of a system is akin to a map: a way for me to get my bearings in that system, so I can get right to work and be effective well before I’ve attained a comprehensive understanding of that system.

Because I can and will eventually commit structures like these to memory — somehow, I learn them, and I can recall the relationships. Not visually, but semantically.


### slide

[??]

I think this is why I find diagrams so crucial when I’m in a new context — they enable fast and effective **reference** _and_ fast and effective **learning**.

I’d like to posit here today that while this may be _especially_ true for me, and maybe for others with aphantasia, I suspect this also holds true for neurotypical folks.

So basically, diagrams are a fast and effective medium for reference and learning, that can help people be more effective faster, in new contexts.

Great. Diagrams are awesome. End of talk, maybe?

## What Is

### slide

[??]

Not so fast.

Diagrams are awesome, but the most common approaches to creating maintaining, and publishing them are definitely not awesome. They’re highly lacking in awesomeness.

### slide

[scribbled diagrams on whiteboards]

Have any of you ever joined a new team and asked someone if any diagrams exist, only to have that person lead you over to a whiteboard and scribbling and freestyling some diagrammatic impressionist art?

I certainly have.

### slide

[pinned-up printouts of diagrams]

Have any of you ever joined a new team, looked for diagrams, found some promising ones pinned up to the wall on paper, but when you ask who made them and when, you just get shrugs? Or “oh, they left last year”?

I certainly have.

### slide

[?? screenshot of last-updated timestamp? Maybe papyrus? Old software books?]

Have you ever asked someone to work with you to create a diagram, and they declined because, according to them, “documentation is always out of date”

I certainly have.

### slide

[?? maybe screenshot of OmniGraffle pricing page?]

Have you ever rejoiced at actually finding the source file for a useful diagram that needs to be updated — only to be unable to change it, for lack of a proprietary and expensive software license?

I certainly… you get the idea.

### slide

[?? maybe video of tweaking layout?]

Have you ever struggled to get the elements of a diagram laid out evenly and consistently, cursing every moment of it, because what the hell, computers were supposed to eliminate this kind of drudgery years ago!

### slide

[??]

I’ve been creating and maintaining diagrams for decades, and I’ve been perennially frustrated by experiences like these.

I’d regularly look around to try to find new tools and techniques that might address these frustrations, but I never found anything satisfactory.

Until recently.

## What Could Be

### slide

[obligatory morpheus image macro]

What if I told you…

…that there’s a technique (**?**) that can radically transform how we create, maintain, and publish our diagrams?

A technique that many of us already use every day, when writing programs?

### slide

[??]

That’s right, it’s **data in text files!**

### slide

[??]

So yeah... as many of us might already know, in Clojure, and all Lisps, code is data.

We represent our code in text files using our language’s native data structure literals.

This makes it trivial to generate new code and to parse code — and once it’s parsed you can manipulate it, analyze it, project it, transform it, translate it, graph it, etc.

You can do all sorts of fun things!

### slide

[??]

Wouldn’t it be cool if we could express our diagrams as _data in text files_ so that we could then do some of these fun things with our diagrams?

## What Is

### slide

### slide

## What Could Be

### slide

### slide

## What Is

### slide

### slide