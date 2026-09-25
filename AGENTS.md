# Multi-Agent Workflow Orchestration

GitLogisticsWatch coordinates evaluation, safety verification, and compliance approval across specialized agent personas.

## Pipeline Architecture
1. **Step 1**: Ingest hierarchical engineering Bill of Materials (BOM) parts lists.
2. **Step 2**: Evaluate supplier lead-time variability and supplier delivery reliability.
3. **Step 3**: Calculate minimum safety stock and economic reorder points.
4. **Step 4**: Issue procurement warnings for single-sourced bottleneck components.

## Separation of Agents

Maker: SupplyChainPlanner who manages supplier purchase orders, lead-time tables, and parts catalogs.

Checker: ManufacturingDirector who audits production line readiness and authorizes procurement commitments.
