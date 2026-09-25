# Separation of Duties for GitLogisticsWatch

In accordance with compliance standards and zero-trust engineering principles, all critical operations require dual-party authorization.

## Role Definitions

### Maker
The SupplyChainPlanner who manages supplier purchase orders, lead-time tables, and parts catalogs.

### Checker
The ManufacturingDirector who audits production line readiness and authorizes procurement commitments.

## Enforcement Mechanism
No configuration, manifest, or policy change evaluated by GitLogisticsWatch may be merged without explicit validation by the independent Checker. The system enforces cryptographic integrity across both roles.
