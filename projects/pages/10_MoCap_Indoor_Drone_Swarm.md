---
layout: page_project
title: "MoCap Indoor Drone Swarm"
description: "An indoor drone swarm testbed using motion capture for precise localization, coordinated flight, and repeatable experiments"
permalink: /projects/mocap-indoor-drone-swarm/
parent: Projects
navbar_active: Projects
nav_order: 10

thumb: /projects/thumbs/drones.png

link_url: https://cepdnaclk.github.io/e21-3yp-Drone-Swarm/
link_caption: Project Page

api_url: https://api.ce.pdn.ac.lk/projects/v1/3yp/E21/Drone-Swarm

gallery: false
gallery_images:
  - { url: "#", caption: "" }

resources: true
resource_list:
  - { text: "Download for Windows (x64)", url: "https://d19306u9suswz7.cloudfront.net/latest/DroneSwarm-Windows-x64.exe" }
  - { text: "Download for Ubuntu (x64)", url: "https://d19306u9suswz7.cloudfront.net/latest/latest/DroneSwarm-Ubuntu-x64.tar.gz" }
---

This project develops an indoor testbed for coordinated drone-swarm experiments using a motion-capture (MoCap) system. The MoCap system provides precise position and orientation measurements for each drone, enabling the swarm to operate safely and consistently in a controlled indoor environment where GPS is unavailable.

The testbed supports the development and evaluation of multi-drone coordination methods, including formation control, trajectory tracking, collision avoidance, and collective motion. A shared localization and control workflow allows experiments to be repeated under comparable conditions while the behavior of individual drones and the overall swarm is observed.

The project aims to provide a practical platform for moving swarm algorithms from simulation to physical flight. It brings together motion capture, wireless communication, flight control, and experiment monitoring so that indoor drone-swarm behaviors can be tested and refined.
