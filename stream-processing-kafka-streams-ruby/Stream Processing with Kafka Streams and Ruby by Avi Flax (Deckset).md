autoscale: false
theme: Merriweather, 8
build-lists: true

[.header: text-scale(1.5)]
[.text: text-scale(1.5)]

# Stream Processing with Kafka Streams and Ruby

Avi Flax
September 2020

----

## The Product

[.header: text-scale(1.5)]
[.text: text-scale(1.5)]

![right](images/garage-01.jpg)

A **Parking Guidance & Information** (PGI) system

^
• The Product: a parking guidance system
• Installed in hundreds of multi-level parking structures around the world

----

[.header: text-scale(1.5)]
[.text: text-scale(1.4)]

## Components

![right](images/garage-01.jpg)

* **On-prem:**
	* Sensors + Servers
* **Cloud:**
	* Monitoring
	* Configuration
	* Analytics
	* Web UI

^
• These are some of the core components of the product
• Those cloud elements were implemented as a single-instance multi-tenant system
• The 
Hundreds of customers using that cloud-based Web app

----

## Analytics Pipeline

1. Get the data
2. Clean the data
3. Store the data


^
• The problems I needed to solve were part of that analytics feature
• Specifically, the pipeline that conveyed the crucial event data from the sites to the cloud-based system where the customers could query it, visualize it, etc.
• «reveal»
• The job of the pipeline was, at a high level, simple
• But there were a lot of details that made it not so simple

----

## Problems

* High latency
* Low reliability

## Goals

* **Low** latency
* **High** reliability

^
• The old pipeline had some big problems «reveal»
• Basically, it’d been designed and implemented when the number of customers was much smaller;
  • as the customer base grew it’d hit its scaling limit and was now overdue to be refactored.
• 1 nice thing; goals of new pipeline very clear: «reveal»

----

## Design + Technology Choices

----

![old diagram fit](images/old-system-landscape-slide.png)

^
• Basically just a set of cron scripts that polled the on-prem servers on a fixed schedule

----

![new diagram fit](images/new-system-landscape-slide.png)

----
