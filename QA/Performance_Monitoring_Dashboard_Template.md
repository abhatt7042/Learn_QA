# Performance Monitoring Dashboard Template

## 1. Dashboard Overview
**Dashboard Name:**  
**Application / Service:**  
**Environment:** (Prod / Pre-prod / QA)  
**Owner:**  
**Last Updated:**  

**Purpose:**  
Describe the dashboard goal (e.g., monitor latency, errors, and resource usage, detect performance regressions, support incident response).

---

## 2. Key Metrics (High Priority)
These are the metrics that should always be visible on a performance dashboard.

### 2.1 User Experience Metrics
| Metric | Purpose | Threshold | Notes |
|--------|---------|-----------|------|
| Response time (P95 / P99) | Identify slow requests | e.g., P95 < 500ms | Use per API / endpoint |
| Error rate | Detect failures | e.g., < 1% | HTTP 5xx / app errors |
| Apdex / Satisfaction score | Overall user experience | e.g., > 0.9 | Optional |

### 2.2 Throughput & Traffic
| Metric | Purpose | Threshold | Notes |
|--------|---------|-----------|------|
| Requests per second (RPS) | Monitor load | - | Helps correlate with latency |
| Concurrent users | Capacity tracking | - | Useful for stress tests |

### 2.3 Infrastructure Metrics
| Metric | Purpose | Threshold | Notes |
|--------|---------|-----------|------|
| CPU utilization | Detect CPU saturation | e.g., < 70% | per service or node |
| Memory utilization | Detect memory leaks | e.g., < 75% | per service or node |
| Disk I/O | Detect bottlenecks | - | Optional |
| Network throughput | Detect bandwidth limits | - | Optional |

### 2.4 Dependency Metrics
| Metric | Purpose | Threshold | Notes |
|--------|---------|-----------|------|
| DB latency | Identify DB bottlenecks | e.g., < 50ms | SQL / NoSQL |
| Cache hit ratio | Validate caching | e.g., > 90% | Redis / Memcached |
| External API latency | Detect third-party slowness | - | Optional |

---

## 3. Alerts & Thresholds
Define alerts for quick detection and response.

| Alert Name | Trigger | Severity | Action |
|-----------|---------|----------|--------|
| High latency | P95 > threshold | High | Investigate service logs |
| Error spike | Error rate > threshold | High | Check recent deployments |
| CPU saturation | CPU > threshold for 5 min | Medium | Scale up/out |
| DB latency spike | DB latency > threshold | Medium | Check query performance |

---

## 4. Dashboards / Views (Suggested Layout)
### View 1: **Overview**
- Response time (P95/P99)
- Error rate
- Throughput
- CPU/Memory summary

### View 2: **Service Health**
- Per-service response times
- Per-service error rates
- Per-service CPU/Memory

### View 3: **Dependency View**
- DB latency & throughput
- Cache hit ratio
- External API latency

### View 4: **Load Test / Baseline**
- Baseline vs current
- Load vs latency graph
- Bottleneck indicators

---

## 5. Notes / Best Practices
- Use **percentiles (P95/P99)** instead of averages for latency.
- Correlate spikes with deployments (use tags).
- Create **baseline dashboards** to detect regressions.
- Use **distributed tracing** to pinpoint slow services.

---

## 6. Data Sources
List where the metrics are coming from:

- APM tool: (Dynatrace / Datadog / AppDynamics / NewRelic)
- Logs: (Splunk / ELK / CloudWatch)
- Cloud metrics: (CloudWatch / Azure Monitor)

---

## 7. Example Dashboard Screenshot (Optional)
Add a placeholder or example image link if you want to show a sample dashboard.

---

