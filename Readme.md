# exPBS + exRHCR - Enhancement: Fallback Count Policy

## Introduction

The Fallback Count Policy is designed to enhance the adaptability of the system by dynamically monitoring and responding to the number of fallbacks during the execution of delta (Δ) Multi-Agent Path Finding (MAPF) queries. When the count of fallbacks exceeds a predefined threshold, the system triggers the regeneration of a fresh experience using the original Priority-Based Search (PBS) algorithm. This new experience is then utilized for the remaining queries in the current batch.

## Code Files Modified

The policy introduces a counter variable, known as the fallback count, which is integrated into the ex-RHCR algorithm. This counter is incremented within the MAPF solver algorithm, specifically within the ex-PBS step. The decision to generate a new experience is based on the comparison of the fallback count with a predefined threshold value (Θ).

- `L-MAPF/run_windowed_L-MAPF_test_kiva_warehouse.py` file is modified to check the threshold and break the current exPBS iteration if it exceeds the threshold
- `run_code_analysis.py` - The run_code_analysis.py file has been included to perform a customised version of the original experiment.


## Libraries Required
* Boost
* Google Sparsehash (included)

## Credits
Original PBS implementation adopted from [Hang Ma](https://www.cs.sfu.ca/~hangma/).

## Code
Compile in Ubuntu 20:
```bash
make executable
```

To Run 
```bash
cd L-MAPF && python3 run_code_analysis.py
```

This generates the result *CSVs* in the directory `L-MAPF`. Before running the experiment again, make sure to **save** the *CSVs* generated in the previous run.


 
 
## References
[^1]: [Madar et al., 2022] [Nitzan Madar, Kiril Solovey, and Oren Salzman. Leveraging Experience in Lifelong Multi-Agent Pathfinding. In Symposium on Combinatorial Search (SoCS), 2022.](https://arxiv.org/abs/2202.04382)

[^2]: [Li et al., 2021] [Jiaoyang Li, Andrew Tinka, Scott Kiesel, Joseph W. Durham, T. K. Satish Kumar and Sven Koenig. Lifelong Multi-Agent Path Finding in Large-Scale Warehouses. In Proceedings of the AAAI Conference on Artificial Intelligence (AAAI), 2021.](http://idm-lab.org/bib/abstracts/papers/aaai21b.pdf)

[^3]: [Ma et al., 2019] [Hang Ma, Daniel Harabor, Peter J Stuckey, Jiaoyang Li, and Sven Koenig. Searching with consistent prioritization for multi-agent path finding. In Conferences on Artificial Intelligence (AAAI), volume 33, pages 7643–7650, 2019.](http://idm-lab.org/bib/abstracts/papers/aaai19b.pdf)
