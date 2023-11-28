# exPBS + exRHCR  - Enhancement: Depth Limit
exPBS and exRHCR implementation [Madar et al., 2022][^1].
<!-- --- -->
## Introduction
This repository contains a Depth Limit variation of the original implementation of exPBS and exRHCR by Madar et al. With a view on memory efficiency, we propose the usage of Iterative Deepening Search. In this approach, we maintain a local depth limit and increment it every time it is reached in the search, until its value reaches a pre-specified global depth limit. This way, we do not traverse in any branch indefinitely, and can find the solution, if it exists, with greater memory efficiency.

## Code Files Modified
* `driver.cpp` - The main file that runs the experiments. The `main` function has been modified to call the function `GICBSSearch::runGICBSSearchWrapper()` instead of `GICBSSearch::runGICBSSearch()`.
* `GICBSSearch.cpp`
  - The `GICBSSearch::runGICBSSearch()` function has been modified to include the depth limit parameter.
  - `GICBSSearch::runGICBSSearchWrapper()` and `GICBSSearch::resetGICBSSearch()` have been added to perform Iterative Deepening Search.
* `GICBSSearch.h` - The `GICBSSearch` class has been modified to include the parameters - `HL_DFS_height_limit`, `HL_DFS_height_limit_global`, and `HL_DFS_height_limit_increment`.
* `run_code_analysis.py` - The `run_code_analysis.py` file has been included to perform a customised version of the original experiment.
<!-- ## Abstract
In Lifelong Multi-Agent Path Finding (L-MAPF) a team of agents performs a stream of tasks consisting of multiple locations to be visited by the agents on a shared graph while avoiding collisions with one another.
L-MAPF is typically tackled by partitioning it into *multiple consecutive*, and hence *similar*, "one-shot" MAPF queries, as in the Rolling-Horizon Collision Resolution (RHCR) algorithm [Li et al., 2021][^2].
Therefore, a solution to one query informs the next query, which leads to similarity with respect to the agents' start and goal positions, and how collisions need to be resolved from one query to the next. Thus, experience from solving one MAPF query can potentially be used to speedup solving the next one.
Despite this intuition, current L-MAPF planners solve consecutive MAPF queries from scratch.
In this paper, we introduce a new RHCR-inspired approach called exRHCR, which exploits experience in its constituent MAPF queries. In particular, exRHCR employs a new extension of Priority-Based Search (PBS) [Ma et al., 2019][^3], a state-of-the-art MAPF solver. Our extension, called exPBS, allows to warm-start the search with the priorities between agents used by PBS in the previous MAPF instances.
We demonstrate empirically that exRHCR solves L-MAPF instances up to 39% faster than RHCR, and has the potential to increase system throughput for given task streams by increasing the number of agents a planner can cope with for a given time budget. -->


## Libraries Required
* Boost
* Google Sparsehash (included)

## Credits
Original PBS implementation adopted from [Hang Ma](https://www.cs.sfu.ca/~hangma/).

## Usage
Compile in Ubuntu 20:
```
make executable
```

To Run the Experiment:
```bash
cd L-MAPF && python3 run_code_analysis.py
```

This generates the result *CSVs* in the directory `L-MAPF`. Before running the experiment again, make sure to **save** the *CSVs* generated in the previous run.
<!-- * Run PBS or exPBS:

  Use the command
  ```shell
  ./driver --map <map_file_name.map> --agents <agents_file_name.agents> --agentNum <number_of_agents> --output <output_file_name.csv>  --experience <experience_option> --width_limit_hl <w> --fallback <fallback_option> --windowed_mapf <window_size>  --replan_rate <h> --to_save_P_matrix <save_solution_priorities> --cleaning_threshold <threshold>
  ```

  - `map`: (str, <map_file_name>.map) the map file (note that the map are undirected).
  - `agents`: (str, <agents_file_name>.agents) agents file represent the MAPF query.
  - `agentNum`: (int) number of agents.
  - `output`: (str, <output_file_name>.csv) output file name (if file exists the will not override it).
  - `experience`: (int) use experience (1) or not (0), other options are tested during developement (e.g., cleaning experience in regular MAPF).
  - `width_limit_hl`: (int) l, width limit parameter for WL-DFS search in the priority tree.
  - `fallback`: the FindFallback function, no fallback (0, default), upward fallback (0,1], original PBS fallback (2) or other experience (3, not relevant if no experience database used).
  - `windowed_mapf`: (int) w, window size for the W-MAPF query.
  - `replan_rate`: (int) h replan rate, this will override the .agent file to the next query file.
  - `to_save_P_matrix`: (int) save solution PT node priorities (matrix representation) to .priorities file (1) or not (0).
  - Other parameter from offline experience tests and original PBS implementation, **don't change it and use defaults**:
     - `cleaning_threshold`: (int) used for cleaning offline experience tests
     - `solver`: (str) used in original PBS paper
     - `priority`: (int) priority branching

  For more details, run:
  ```shell
  ./driver --help
  ```
 * Run exRHCR:

   Using a pythonic shell (in `L-MAPF` folder)
    ```shell 
    cd L-MAPF
    python3 ./<python_lifelong_shell> -a <number_of_agents> -c <create_and_save> -d <delta> -t <test_num> -l <ell>
    ```
    where:
      * `a`: (int) the number of agents
      * `c`: (int, 1 or 0) use stored example or create a new one and save (overwries existing files)
      * `d`: (int) delta, the lookahead exRHCR parameter
      * `t`: (int) test number
      * `l`: (int) the width dimit parameter for WL-DFS  -->
 
 
## References
[^1]: [Madar et al., 2022] [Nitzan Madar, Kiril Solovey, and Oren Salzman. Leveraging Experience in Lifelong Multi-Agent Pathfinding. In Symposium on Combinatorial Search (SoCS), 2022.](https://arxiv.org/abs/2202.04382)

[^2]: [Li et al., 2021] [Jiaoyang Li, Andrew Tinka, Scott Kiesel, Joseph W. Durham, T. K. Satish Kumar and Sven Koenig. Lifelong Multi-Agent Path Finding in Large-Scale Warehouses. In Proceedings of the AAAI Conference on Artificial Intelligence (AAAI), 2021.](http://idm-lab.org/bib/abstracts/papers/aaai21b.pdf)

[^3]: [Ma et al., 2019] [Hang Ma, Daniel Harabor, Peter J Stuckey, Jiaoyang Li, and Sven Koenig. Searching with consistent prioritization for multi-agent path finding. In Conferences on Artificial Intelligence (AAAI), volume 33, pages 7643–7650, 2019.](http://idm-lab.org/bib/abstracts/papers/aaai19b.pdf)
