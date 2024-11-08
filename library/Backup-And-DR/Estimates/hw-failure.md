---
title: "Hardware failure estimates on mixed NVMe and SSD workstations"
---

Based on the search results, I'll explain the calculation of annual drive failure risk for your setup with 1 NVMe and 2 SSDs.

## Failure Rate Calculation

The annual failure rates for your drives are:

- NVMe drives: 1% annual failure rate\[4]
- SATA SSDs: 0.89% annual failure rate\[2]

To calculate the probability of at least one drive failing in a year, we use the following approach:

1. Calculate the probability of no failures occurring
2. Subtract that from 1 to get the probability of at least one failure

The mathematical calculation is:$$P(\text{at least one failure}) = 1 - P(\text{no failures})$$$$= 1 - [(1-0.01) \times (1-0.0089)^2]$$

The probability of at least one of your drives failing in a year is approximately 2.75%.

## Context

This calculation is supported by real-world data from large-scale studies. Backblaze's extensive research shows that modern SSDs are quite reliable, with failure rates consistently below 1%\[1]\[2]. NVMe drives show slightly higher failure rates than SATA SSDs, with an average annual replacement rate of 0.98%\[4].

&#x20;
