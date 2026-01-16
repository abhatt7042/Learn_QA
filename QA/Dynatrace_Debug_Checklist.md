# Dynatrace Bottleneck Debugging Checklist

A practical checklist to debug **performance bottlenecks** using **Dynatrace**. Use this during **performance testing, monitoring, or production troubleshooting**.

---

## 1. Initial Assessment

- [ ] Identify **performance symptom** (high response time, throughput drop, errors, CPU/memory spikes)  
- [ ] Check **time window** when issue occurred  
- [ ] Verify **system/environment** (Prod, QA, Staging)

---

## 2. Analyze Host & Infrastructure

- [ ] Check **CPU, memory, disk I/O, and network usage** on affected hosts  
- [ ] Look for **resource saturation** patterns  
- [ ] Check **top processes** consuming CPU/memory  
- [ ] Review **container metrics** if using Docker/Kubernetes  

---

## 3. Investigate Application Service

- [ ] Identify **slow services or endpoints** in Dynatrace Service Flow  
- [ ] Check **response time hotspots** and compare to baseline  
- [ ] Examine **throughput and error rates**  
- [ ] Review **service dependencies** for cascading issues  

---

## 4. Code-Level Analysis

- [ ] Enable **PurePath tracing** for affected transactions  
- [ ] Identify **slow methods/functions**  
- [ ] Check **database calls**, external APIs, or file I/O  
- [ ] Look for **high exception rates or retries**  

---

## 5. Database & Queries

- [ ] Check **SQL query execution times**  
- [ ] Identify **long-running queries** and frequent calls  
- [ ] Examine **deadlocks, locks, or contention**  
- [ ] Check **database connection pool usage**  

---

## 6. Frontend / User Experience

- [ ] Review **RUM (Real User Monitoring) metrics**  
- [ ] Identify **slow-loading pages or actions**  
- [ ] Check **third-party scripts or APIs** impacting load time  
- [ ] Examine **AJAX calls** and their response times  

---

## 7. Logging & Error Analysis

- [ ] Review **application logs** for exceptions and warnings  
- [ ] Correlate logs with **Dynatrace events and alerts**  
- [ ] Check **service-level error percentages**  

---

## 8. Optimization & Remediation

- [ ] Prioritize **high-impact bottlenecks** first  
- [ ] Review **caching strategies**  
- [ ] Optimize **database queries**  
- [ ] Tune **application server or container configurations**  
- [ ] Re-run Dynatrace analysis to confirm improvements  

---

## 9. Documentation

- [ ] Record **bottleneck root cause**  
- [ ] Document **fixes applied and results**  
- [ ] Share checklist with team for **knowledge sharing**  

---

**Note:** Always combine Dynatrace metrics with **logs, system monitoring, and baseline comparisons** to accurately identify bottlenecks.            
