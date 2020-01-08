# Sombrio

Sombrio ** is a scalable search engine for the dark web. The goal of the
project is to build a simple, robust search engine from scratch that can search
through the dark web content.

## Project Status

 The last time we tested (December 2016), the dark web did not provide  us
 enough meaningful results to serve a query.
However, each component was working and tested separately. Hence, this project can be
used as a foundation to add more interesting features and build a more complex
product.

## Architecture

![Sombrio Design](mgmt/doc/sombrio.png)

**Components**

- [Crawler:](crawler) Crawls the onion websites
- [Index Builder:](indexer) Builds index chunk
- [Index Server:](index-server) Stores replicated index chunk
- [MGMT:](mgmt) Serves as single master, schedules jobs for other servers and executes
  heartbeats messages
- [Front-End:](frontend) Serves a website with Google-like interface
- [Back-End:](webserver) Express server with caching and aggregation logic

**API**
- [API](mgmt/doc/api.md)
- [Sample flow](mgmt/doc/flow.md)

## Testing

Each component has its own Dockerfile that is ready to be built and tested.
