---
layout: page_project
title: A Programming Framework for Robot Swarms Project
description: ""
permalink: /projects/ProgrammingFrameworkforRobotSwarms/
parent: Projects
navbar_active: Projects
nav_order: 2

thumb: /projects/thumbs/blank.jpg

link_url: Sample URL
link_caption: View More

gallery: true
galery_images:
    - {url: '/projects/gallery/ProgrammingFrameworkforRobotSwarms/1.jpg', caption: 'Coloured object identification and reaching concensus
'}

team: true
team_members:
    - {name: 'Nuwan Jaliyagoda'}
    - {name: 'Dilshani Karunarathna'}

supervisors: true
supervisor_members:
    - {name: 'Dr. Isuru Nawinne'}
    - {name: 'Prof. Roshan G. Ragel'}

resources: true
resource_list:
    - {text: 'Sample URL', url: 'https://example.com' }

---

Swarm robotics is a well-evolved research area over the past couple of decades. This work introduces a framework for programming swarm robots in a novel approach based on behavior categorization, pheromone communication, and state representation. The framework is packaged with a set of well defined and tested behaviors that are structured based on the level of interactions between robots. These behaviors can be combined and integrated to the user code when implementing new behaviors. Robots function in a user-defined state and perform actions attributed to that state. A behavior-based bottom-up design approach was used for designing these behaviors which eventually alleviate the debugging and implementation process.

This also includes necessary pair-behaviors, neighbor-cluster behaviors for aggregation and pattern formation global behaviors. If the users point out a need for more lower-level behaviors to create their algorithms, they could also add them to this library. For this, users should first provide the framework for selected users and get their feedback.
The efficacy of this work is validated using results obtained from a custom-built simulation platform. These results include tests involving an obstacle avoidance behavior associated with random movement, an object finding behavior and an implementation of aggregation and pattern formation behavior.
