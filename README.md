# A ROS 2-Based Heterogeneous Multi-Robot Autonomy Architecture for Collaborative 3D Mapping

A research-oriented robotics framework that enables **heterogeneous multi-robot teams (UGV + UAV)** to perform **collaborative 3D mapping** using a **ROS 2-based autonomy architecture**.  
This project focuses on a clean, reproducible pipeline for simulation-first development, multi-agent coordination, mapping data fusion, and producing a unified 3D representation (map/mesh) of the environment.

---

## Project Goals

- **Heterogeneous multi-robot autonomy**: integrate a UGV and UAV into one coordinated system
- **Collaborative 3D mapping**: fuse perception data into a shared global representation
- **Architecture-first design**: modular stack (simulation, bridge, autonomy, mapping, visualization)
- **Research-ready experiments**: reproducibility, metrics, ablations, and logging
- **Sim-to-real path**: structure the system so components can later transfer to physical robots

---

## Core Capabilities (Planned / In Progress)

###  Baseline (already achieved)
- ROS 2 ↔ Gazebo Fortress simulation working
- UGV model spawned and stable
- Sensor topics (e.g., LiDAR /scan, odometry /odom)
- Command interface (e.g., /cmd_vel) and bridge operational

###  Current development track
- Multi-robot spawning (UGV + UAV)
- Multi-agent coordination (task allocation / exploration strategy)
- Mapping pipeline (3D mapping + fusion)
- Mesh reconstruction / export
- Monitoring dashboard (“Autonomy OS” layer): agent health, stats, map progress, logs

---

## System Architecture (High Level)

**Simulation Layer**
- Gazebo Fortress world(s)
- Robot models (UGV / UAV), sensors, physics

**Middleware Layer**
- ROS 2 (Humble)
- Bridge nodes (Gazebo ↔ ROS 2)

**Autonomy Layer**
- Navigation / exploration behaviors
- Coordination policies (multi-agent logic)
- Safety constraints (collision avoidance, limits)

**Mapping Layer**
- Local mapping per robot
- Global map fusion / alignment
- 3D representation output (map/point cloud/mesh)

**Ops Layer (Autonomy OS)**
- Central monitoring UI + logging
- Robot status visualization
- Dataset capture for learning + evaluation

---

## Tech Stack

- **ROS 2 Humble**
- **Gazebo Fortress** (Ignition / Gazebo Sim)
- Python + C++ (as needed)
- Common ROS tools: tf2, nav_msgs, sensor_msgs, rosbag2
- Mapping libraries and packages (to be finalized per module)

---

## Repository Structure (proposed)

```text
.
├── docs/                  # architecture notes, diagrams, experiment logs
├── src/                   # ROS 2 packages (description, bringup, autonomy, mapping)
│   ├── mtrebot_description/
│   ├── <ugv_bringup_pkg>/
│   ├── <uav_bringup_pkg>/
│   ├── <multi_robot_coordination_pkg>/
│   └── <mapping_fusion_pkg>/
├── worlds/                # Gazebo worlds and assets
├── launch/                # top-level launch files (simulation + stack)
├── scripts/               # utilities: setup, logging, evaluation
└── README.md
