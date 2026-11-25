<!-- Profile Header -->
<h1 align="center">Vladislav Rybin</h1>
<p align="center">
  Senior Rust Engineer · Low-Latency Trading Systems · Concurrent & Systems Programming · Backend & Blockchain Infrastructure
</p>
<p align="center">
  <a href="https://www.linkedin.com/in/vladislav1rybin">LinkedIn</a> ·
  <a href="https://medium.com/@4pex1oh">Medium</a>
</p>

---

I write multithreaded Rust for trading systems. At Vortex Foundation I work on DEX execution across EVM chains and Solana: arbitrage and liquidation engines, exchange connectivity, and the node and backend infrastructure they run on.

### What I work on

- **Low latency and concurrency.** CPU-pinned threads outside the async runtime, staged pipelines over channels, lock-free synchronization checked with loom and miri, allocation-free hot paths, zero-copy parsing, p50/p99 tracking on critical paths.
- **Systems programming.** unsafe Rust, FFI between Rust and Go, a client for an exchange's custom application-layer protocol over TCP, Reth modifications for faster mempool processing.
- **Backend.** Tokio and Axum services, internal APIs, data pipelines for quantitative engineers, production observability.
- **DeFi execution.** DEX-DEX and DEX-CEX arbitrage, liquidations, 15+ DEX integrations with CLMM/DLMM liquidity unified into one pricing model, MEV protection through Flashbots and Jito, Solidity contracts including a Uniswap v4 hook.

### Open source

Merged PRs in [Foundry](https://github.com/search?q=author%3ASyzygy106+org%3Afoundry-rs+is%3Apr+is%3Amerged&type=pullrequests) and [Alloy](https://github.com/search?q=author%3ASyzygy106+org%3Aalloy-rs+is%3Apr+is%3Amerged&type=pullrequests).

### Stack

**Languages:** Rust, Solidity, Python  
**Rust:** Tokio, Axum, Alloy, Reth, loom, miri  
**Infrastructure:** PostgreSQL, Redis, Kafka, Docker, Kubernetes, Grafana  
**Chains:** Ethereum, Arbitrum, Base, Optimism, Polygon, zkSync, BNB Chain, Avalanche, Solana, Tron, TON  
**Protocols:** Uniswap V2-V4, Raydium, Orca, Meteora

### Writing

<!-- MEDIUM:START -->
- [NFTs For Non-Devs #2. The Mystery Box.](https://medium.com/@4pex1oh/nfts-for-non-devs-2-the-mystery-box-85a108116ca8?source=rss-a31c7ae79b1f------2) <sub>· Wed, 19 Nov 2025</sub>
- [NFTs For Non-Devs #1. The Classic Drop.](https://medium.com/@4pex1oh/article-2-the-classic-drop-c3c5ed859d8b?source=rss-a31c7ae79b1f------2) <sub>· Wed, 22 Oct 2025</sub>
- [What Are NFTs and Why Do They Matter?](https://medium.com/@4pex1oh/what-are-nfts-and-why-do-they-matter-14cde132ee47?source=rss-a31c7ae79b1f------2) <sub>· Mon, 06 Oct 2025</sub>
<!-- MEDIUM:END -->
